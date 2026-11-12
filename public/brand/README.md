# TailorLM brand assets

Canonical source for the TailorLM mark, favicon and social card.

## Files

| 文件 | 用途 |
| --- | --- |
| `tailorlm-mark.svg` | 主 mark，64×64，深绿 + 焦橙 |
| `tailorlm-mark-mono.svg` | 单色版，`currentColor` |
| `tailorlm-mark-512.png` | GitHub org avatar / social |
| `og.png` | 1200×630 社交卡 |
| `README.md` | 本文件 |

新 logo 确认前，`public/favicon.svg` 和 `public/og.png` 是临时版本。

## 颜色

| 名称 | Hex |
| --- | --- |
| 深绿 | `#123C2F` |
| 焦橙 | `#D97745` |
| 米白 | `#F7F3EA` |
| 灰 | `#6C6A61` |

## 规则

- mark 必须在 16×16 下可辨认，且有一色版。
- 不用渐变、阴影、滤镜、细发丝线、3D。
- mark 内不放文字；wordmark 用站点字体 Fraunces，不塞进 SVG。
- 留白 ≥ mark 宽度的 1/4。
- 不拉伸、不旋转、不换色、不加特效。
- 不把 mark 当项目符号或底纹，除非有明确设计。

## 验收 SVG

- [ ] `viewBox="0 0 64 64"`，无 `width`/`height` 或固定 64
- [ ] 无 `<text>`、`<style>`、渐变、滤镜、mask、clipPath
- [ ] 只有 path/rect/circle/line/polyline/polygon
- [ ] 64px 下描边 ≥ 2px
- [ ] 16px 下可辨认
- [ ] 有单色版
- [ ] 无外部图片、无 base64
- [ ] 文件 < 10 KB

## 用在哪

- 页头：inline SVG 或 `/brand/tailorlm-mark.svg`
- favicon：`/brand/tailorlm-mark.svg`
- OG：`public/og.png`
- GitHub org avatar：在组织设置上传 `tailorlm-mark-512.png`
- Org profile：把 `tailorlm-mark-512.png` 复制到 `.github/profile/assets/`，保证渲染稳定
- Repo social preview：在仓库设置上传 `og.png`

## 上传流程

1. Gemini 输出 SVG 代码；
2. 发我，我清洗、压缩、做单色版和 16px 检查；
3. 我提交到 `tailorlm/public/brand/`；
4. 替换页头、favicon、OG；
5. 复制 PNG 到 `.github/profile/assets/`；
6. 你在 GitHub 组织设置和仓库设置里上传头像/社交预览。
