# TailorLM

[![CI](https://github.com/tailorlm/tailorlm/actions/workflows/ci.yml/badge.svg)](https://github.com/tailorlm/tailorlm/actions/workflows/ci.yml)

**Custom models, fitted to your business.**

TailorLM is a post-training studio for open-source LLMs. We start with a diagnostic, then build the data, evaluation, and training plan that fits the task. Acceptance is measured on a held-out test set — not on a loss curve.

[中文](#中文) · [Services](#services) · [How we work](#how-we-work) · [Contact](#contact)

## Services

| | |
| --- | --- |
| **Diagnostic** | Decide whether training is the right fix, and define the baseline, metrics, and budget. |
| **Data & evaluation** | Turn raw material into trainable data and a held-out test set. |
| **LoRA experiment** | Validate the direction on a small budget before scaling. |
| **Full delivery** | Adapter or model, evaluation report, inference example, and deployment notes. |

## How we work

1. **Diagnose.** Reproduce the failure, check data rights, and define what “better” means.
2. **Baseline.** Measure the current model on a fixed test set.
3. **Experiment.** Start with a small, high-quality sample; scale only if there is a measurable signal.
4. **Deliver.** Adapter/model, evaluation report, failure cases, and known limitations.

We do not sell GPU time, and we do not promise “train until satisfied.”

## This repository

Source of the TailorLM website: Astro 7, static output, no UI framework.

```bash
pnpm install
pnpm dev
pnpm build
```

Deployment: see [`deploy/README.md`](deploy/README.md).

## 中文

**量体裁模。** TailorLM 为有明确任务和数据的团队做开源 LLM 后训练：先诊断，再训练，用可复现的评测验收。

- **诊断**：判断是否真的需要训练，定义基线、指标和预算。
- **数据与评测**：把资料变成可训练、可验证的数据。
- **LoRA 小试验**：小预算验证方向，有信号再扩大。
- **完整交付**：模型或 adapter、评测报告、推理示例和部署说明。

不卖 GPU 租赁，不承诺“训到满意”。

## Contact

contact@mcocdaa.com · [github.com/tailorlm](https://github.com/tailorlm)
