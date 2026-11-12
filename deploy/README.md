# 部署

静态站，构建产物在 `dist/`。上线前先完成 ICP 备案，见 [`icp.md`](icp.md)。

## 方式 A：Nginx + 静态文件

```bash
pnpm install
PUBLIC_ICP_BEIAN="京ICP备2026000000号-1" pnpm build
```

把 `dist/` 同步到服务器：

```bash
rsync -av --delete dist/ user@server:/var/www/tailorlm/
```

服务器上启用站点：

```bash
sudo cp deploy/nginx.conf /etc/nginx/sites-available/tailorlm
sudo ln -s /etc/nginx/sites-available/tailorlm /etc/nginx/sites-enabled/tailorlm
sudo nginx -t && sudo systemctl reload nginx
sudo certbot --nginx -d tailorlm.mcocdaa.com
```

DNS：在 `mcocdaa.com` 加一条 `A` 记录，`tailorlm` → 服务器 IP。

## 方式 B：Docker

```bash
pnpm build
docker build -t tailorlm-site .
docker run -d --name tailorlm-site -p 8080:80 --restart unless-stopped tailorlm-site
```

反向代理到 `127.0.0.1:8080`，TLS 用 Caddy 或 Nginx + certbot。

## 检查

```bash
curl -I https://tailorlm.mcocdaa.com
curl -s https://tailorlm.mcocdaa.com | head
```

## 内容更新

- 定价表：`src/components/PricingTable.astro`
- 首页文案：`src/pages/index.astro`
- 服务/流程/联系：`src/pages/*.astro`
- 品牌色/字体：`src/styles/global.css`
