# TailorLM brand assets

TailorLM 的 mark、favicon 和社交卡。选定方案：**量尺括号（Tape Bracket）**。

`[ ]` 既是上下文窗口/张量边界，也是裁缝软尺；中间一道焦橙刻度对应“量体裁模”。

## Files

| 文件 | 用途 |
| --- | --- |
| `tailorlm-mark.svg` | 主 mark，透明底，深绿 + 焦橙，100 网格 |
| `tailorlm-mark-small.svg` | 小尺寸光学版，加粗、只留中点，16–28px 用 |
| `tailorlm-mark-mono.svg` | 单色版，`currentColor` |
| `tailorlm-mark-small-mono.svg` | 小尺寸单色版，16–28px 用 |
| `tailorlm-mark-512.png` | 透明底 512px mark |
| `tailorlm-avatar-512.png` | 深绿底头像，GitHub / 闲鱼 / 淘宝 |
| `tailorlm-avatar-light-512.png` | 米白底头像，浅色场景 |
| `tailorlm-favicon.svg` | favicon，深绿圆角底 + 米白括号 + 橙中点 |
| `tailorlm-favicon-32.png` | PNG favicon 兜底 |
| `../og.png` | 1200×630 社交卡，源文件 `../og.svg` |

`public/favicon.svg` 是 `tailorlm-favicon.svg` 的副本，保持根路径可用。

## 颜色

| 名称 | Hex |
| --- | --- |
| 深绿 | `#123C2F` |
| 焦橙 | `#D97745` |
| 米白 | `#F7F3EA` |
| 灰 | `#6C6A61` |

## 用法

- 页头 / 正文 mark：≥ 32px 用 `tailorlm-mark.svg`；16–28px 用 `tailorlm-mark-small.svg`。
- favicon：`tailorlm-favicon.svg`；16px 下只保留括号和中点，不再加细节。
- 头像：GitHub 组织、闲鱼、淘宝用深绿底 `tailorlm-avatar-512.png`；浅色背景用 `tailorlm-avatar-light-512.png`。
- 单色印刷 / 深色底：用 `tailorlm-mark-mono.svg`，颜色继承 `currentColor`。
- 安全留白：mark 四周至少留 mark 宽度的 1/4，不贴边。
- 不拉伸、不旋转、不换色、不加阴影/渐变/描边特效；不把 mark 当底纹或项目符号。
- mark 内不放文字；wordmark 用站点字体 Fraunces，由 HTML 排版，不塞进 SVG。

## 验收

- [x] `viewBox="0 0 100 100"`，无固定 `width`/`height`（PNG 除外）
- [x] 无 `<text>`、`<style>`、渐变、滤镜、mask、clipPath、外链、base64
- [x] 只有 path / rect
- [x] 64px 下主 mark 描边 3.84px；小尺寸版 6.4px
- [x] 16px 下用 `tailorlm-mark-small.svg` 可辨认
- [x] 有单色版、深底头像、浅底头像
- [x] SVG 文件均 < 1 KB

## 来源

方案由 Gemini 生成的 SVG 打样页（100 网格、单色几何）选出，人工做了三处调整：

1. 焦橙只保留中点刻度，并缩进到括号内缘，避免把括号切断；
2. 增加 16–28px 光学版（加粗、去掉上下刻度）；
3. 补深绿/米白头像底和 favicon 圆角底。
