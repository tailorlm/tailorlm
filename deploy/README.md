# Deployment

Static Astro site. The build output is in `dist/`.

## Nginx

```bash
pnpm install
pnpm build
rsync -av --delete dist/ user@server:/var/www/tailorlm/
```

Install [`nginx.conf`](nginx.conf) and enable the site:

```bash
sudo cp deploy/nginx.conf /etc/nginx/sites-available/tailorlm
sudo ln -s /etc/nginx/sites-available/tailorlm /etc/nginx/sites-enabled/tailorlm
sudo nginx -t && sudo systemctl reload nginx
sudo certbot --nginx -d tailorlm.example.com
```

Point the domain's `A`/`AAAA` records at the server before requesting a certificate.

## Docker

```bash
pnpm build
docker build -t tailorlm-site .
docker run -d --name tailorlm-site -p 8080:80 --restart unless-stopped tailorlm-site
```

Put a reverse proxy in front of `127.0.0.1:8080` and terminate TLS with Caddy or Nginx + certbot.

## Checks

```bash
curl -I https://tailorlm.example.com
curl -s https://tailorlm.example.com | grep -o '<title>[^<]*'
```
