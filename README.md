# TailorLM

[![CI](https://github.com/tailorlm/tailorlm/actions/workflows/ci.yml/badge.svg)](https://github.com/tailorlm/tailorlm/actions/workflows/ci.yml)

> 状态：商业站代码已就绪，等经营主体/备案后部署。个人主页：https://mcocdaa.com

TailorLM 的公开官网：开源 LLM 后训练、评测与交付。

- 商业站：待经营主体/备案后上线
- 个人主页：https://mcocdaa.com
- 组织：https://github.com/tailorlm
- 联系：contact@mcocdaa.com

## 技术栈

- Astro 7，静态输出
- 手写 CSS 设计系统，无 UI 框架
- 字体：Fraunces + Inter（本地打包）

## 开发

```bash
pnpm install
pnpm dev
```

## 构建

```bash
pnpm build
pnpm preview
```

## 部署

见 [`deploy/README.md`](deploy/README.md)。

## 内容边界

这个仓库只放公开官网内容：

- 服务、定价、流程、联系方式
- 隐私政策、服务条款
- 公开文档
- 不放假案例、假 logo、假评价
- 不放客户数据、内部定价逻辑、合同

首版没有公开客户案例；首批 3 个客户按共创价合作，项目完成后按约定脱敏发布。

## 上线前提

个人备案不能承载报价/售卖页面。TailorLM 商业站需要个体工商户或公司主体 + ICP 备案后再部署；个人主页见 https://mcocdaa.com。部署流程见 [`deploy/icp.md`](deploy/icp.md)。
