# TailorLM brand assets

The TailorLM mark is the **Tape Bracket**: a pair of measuring-tape brackets with a single burnt-orange centre tick. `[ ]` reads as a context window or tensor boundary; the tick reads as a tailor's measure.

## Files

| File | Use |
| --- | --- |
| `tailorlm-mark.svg` | Primary mark, transparent, deep green + burnt orange, 100 grid |
| `tailorlm-mark-small.svg` | Optical small-size version, bolder, centre tick only, 16–28px |
| `tailorlm-mark-mono.svg` | One-colour version, `currentColor` |
| `tailorlm-mark-small-mono.svg` | Small one-colour version, 16–28px |
| `tailorlm-mark-512.png` | 512px transparent mark |
| `tailorlm-avatar-512.png` | Dark-green avatar for GitHub / marketplaces |
| `tailorlm-avatar-light-512.png` | Cream avatar for light surfaces |
| `tailorlm-favicon.svg` | Favicon: green rounded square, cream brackets, orange tick |
| `tailorlm-favicon-32.png` | PNG favicon fallback |
| `../og.png` / `../og-en.png` | 1200×630 social cards; sources `../og.svg`, `../og-en.svg` |

`public/favicon.svg` is a copy of `tailorlm-favicon.svg` so the root path keeps working.

## Colour

| Name | Hex |
| --- | --- |
| Deep green | `#123C2F` |
| Burnt orange | `#D97745` |
| Cream | `#F7F3EA` |
| Grey | `#6C6A61` |

## Usage

- Header / body mark: use `tailorlm-mark.svg` at 32px or larger; use `tailorlm-mark-small.svg` at 16–28px.
- Favicon: `tailorlm-favicon.svg`. At 16px the mark keeps only the brackets and centre tick.
- Avatar: use the dark-green `tailorlm-avatar-512.png` for GitHub and marketplaces; use the cream version on light surfaces.
- One-colour print or dark backgrounds: `tailorlm-mark-mono.svg` / `tailorlm-mark-small-mono.svg`; colour inherits from `currentColor`.
- Clear space: at least 1/4 of the mark width on every side.
- Do not stretch, rotate, recolour, add shadows, gradients, or outline effects.
- Do not use the mark as a repeated pattern or bullet.
- No text inside the mark. The wordmark is set in Fraunces in HTML, not embedded in the SVG.

## Acceptance

- [x] `viewBox="0 0 100 100"`; no fixed `width`/`height` (PNG excepted)
- [x] No `<text>`, `<style>`, gradients, filters, masks, clip paths, external links, or base64
- [x] Only `path` / `rect`
- [x] Primary mark stroke is 3.84px at 64px; small version is 6.4px
- [x] The small version is legible at 16px
- [x] One-colour, dark-avatar, and light-avatar versions exist
- [x] Every SVG is under 1 KB

`og.svg` and `og-en.svg` are layout files and may contain `<text>`; they are not marks.

## Source

Selected from a Gemini-generated SVG exploration (100 grid, single-colour geometry), then edited:

1. Burnt orange is kept only for the centre tick, inset from the bracket so the bracket stays continuous.
2. A bolder small-size version removes the upper and lower ticks.
3. Dark/cream avatar backgrounds and a rounded favicon were added.

## 中文

选定方案：**量尺括号**。`[ ]` 同时是上下文窗口/张量边界和裁缝软尺；中间一道焦橙刻度对应“量体裁模”。

- 32px 以上用 `tailorlm-mark.svg`；16–28px 用 `tailorlm-mark-small.svg`。
- GitHub/闲鱼/淘宝头像用深绿底 `tailorlm-avatar-512.png`；浅色场景用米白底。
- 单色印刷用 `tailorlm-mark-mono.svg`；favicon 用 `tailorlm-favicon.svg`。
- 不拉伸、不旋转、不换色、不加阴影/渐变；mark 内不放文字。
