# 域名备案与上线

## 备案前

- 域名已完成实名认证，且域名持有者与备案主体一致；
- 服务器在中国大陆，且托管服务商有备案资质；
- 网站内容已准备好：首页、服务、定价、流程、联系、隐私、条款；
- 网站不包含未备案的论坛、支付、用户上传等需要前置审批的功能；
- 关闭 80/443 对公网的直接访问，避免备案期间被访问。

## 备案中

- 通过服务器托管商提交 ICP 备案；
- 填写网站名称、域名、主体信息、负责人信息；
- 等待管局审核，通常 7–20 个工作日；
- 备案期间用本地 `pnpm dev` 或临时海外环境预览，不在大陆服务器上开站。

## 备案通过后

1. 在 `.env` 或构建环境设置：
   ```bash
   PUBLIC_ICP_BEIAN=京ICP备2026000000号-1
   ```
2. `pnpm build`，页脚会显示备案号并链接到 `beian.miit.gov.cn`。
3. 部署到服务器，配置 Nginx + TLS。
4. 按当地要求完成公安备案（通常 30 天内）。
5. 检查：
   ```bash
   curl -I https://tailorlm.mcocdaa.com
   curl -s https://tailorlm.mcocdaa.com | grep -o 'ICP备[^<]*'
   ```

## DNS

在 `mcocdaa.com` 添加：

```text
类型：A
主机记录：tailorlm
记录值：<服务器 IP>
```

如果走 CDN/代理，按服务商要求改成 CNAME。

## TLS

```bash
sudo certbot --nginx -d tailorlm.mcocdaa.com
```

或使用 Caddy 自动签发。
