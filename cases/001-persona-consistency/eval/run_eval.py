#!/usr/bin/env python3
"""Run the TailorLM persona-consistency eval against an OpenAI-compatible endpoint.

Usage:
    python3 eval/run_eval.py --model Qwen/Qwen3-4B-Instruct \
        --base-url http://127.0.0.1:8000/v1

The endpoint can be vLLM, TrainFlow Inferer, or any OpenAI-compatible server.
"""

from __future__ import annotations

import argparse
import json
import os
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path

CASE_DIR = Path(__file__).resolve().parents[1]
DEFAULT_CASES = CASE_DIR / "eval" / "cases.jsonl"
DEFAULT_SYSTEM = CASE_DIR / "system_prompt.md"
DEFAULT_OUT = CASE_DIR / "results" / "responses.jsonl"


def post_chat(base_url: str, api_key: str, model: str, messages: list[dict], temperature: float, max_tokens: int) -> str:
    url = base_url.rstrip("/") + "/chat/completions"
    body = json.dumps(
        {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
    ).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            payload = json.load(response)
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"HTTP {exc.code} from {url}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise SystemExit(f"Cannot reach {url}: {exc}") from exc
    return payload["choices"][0]["message"]["content"]


def contains(text: str, needle: str) -> bool:
    return needle.casefold() in text.casefold()


def check_final(text: str, checks: dict) -> list[str]:
    failures: list[str] = []
    for needle in checks.get("must_include", []):
        if not contains(text, needle):
            failures.append(f"missing: {needle}")
    any_of = checks.get("must_include_any", [])
    if any_of and not any(contains(text, needle) for needle in any_of):
        failures.append(f"missing any: {any_of}")
    limit = checks.get("max_chars")
    if limit and len(text) > limit:
        failures.append(f"too long: {len(text)} > {limit}")
    return failures


def check_all(text: str, checks: dict) -> list[str]:
    return [f"forbidden: {needle}" for needle in checks.get("must_not_include", []) if contains(text, needle)]


def load_cases(path: Path) -> list[dict]:
    cases: list[dict] = []
    with path.open(encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            line = line.strip()
            if not line:
                continue
            try:
                cases.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise SystemExit(f"{path}:{line_no}: invalid JSON: {exc}") from exc
    return cases


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://127.0.0.1:8000/v1")
    parser.add_argument("--api-key", default=os.environ.get("OPENAI_API_KEY", "EMPTY"))
    parser.add_argument("--model", required=True)
    parser.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    parser.add_argument("--system", type=Path, default=DEFAULT_SYSTEM)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--max-tokens", type=int, default=512)
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    system = args.system.read_text(encoding="utf-8").strip()
    cases = load_cases(args.cases)
    if args.limit:
        cases = cases[: args.limit]

    args.out.parent.mkdir(parents=True, exist_ok=True)
    passed: Counter[str] = Counter()
    total: Counter[str] = Counter()
    failed = 0

    with args.out.open("w", encoding="utf-8") as out:
        for index, case in enumerate(cases, 1):
            messages = [{"role": "system", "content": system}]
            replies: list[str] = []
            for turn in case["turns"]:
                messages.append({"role": "user", "content": turn})
                reply = post_chat(
                    args.base_url,
                    args.api_key,
                    args.model,
                    messages,
                    args.temperature,
                    args.max_tokens,
                )
                messages.append({"role": "assistant", "content": reply})
                replies.append(reply)

            checks = case.get("checks", {})
            final = replies[-1] if replies else ""
            problems = check_final(final, checks)
            for reply in replies:
                problems.extend(check_all(reply, checks))

            dimension = case.get("dimension", "unknown")
            total[dimension] += 1
            ok = not problems
            if ok:
                passed[dimension] += 1
            else:
                failed += 1

            out.write(
                json.dumps(
                    {
                        "id": case["id"],
                        "dimension": dimension,
                        "turns": case["turns"],
                        "replies": replies,
                        "passed": ok,
                        "failures": problems,
                        "model": args.model,
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )

            status = "PASS" if ok else "FAIL"
            print(f"[{index}/{len(cases)}] {status} {case['id']} ({dimension})")
            for problem in problems:
                print(f"  - {problem}")

    print("\nSummary")
    print(f"{'dimension':<12} {'passed':>6} {'total':>6} {'rate':>7}")
    for dimension in sorted(total):
        rate = passed[dimension] / total[dimension] if total[dimension] else 0.0
        print(f"{dimension:<12} {passed[dimension]:>6} {total[dimension]:>6} {rate:>6.0%}")

    overall_total = sum(total.values())
    overall_passed = sum(passed.values())
    if overall_total:
        print(f"{'overall':<12} {overall_passed:>6} {overall_total:>6} {overall_passed / overall_total:>6.0%}")
    print(f"\nresponses: {args.out}")
    if failed:
        print(f"failed cases: {failed}")


if __name__ == "__main__":
    main()
