---
title: [OPS-025] HTTP 强跳 HTTPS 与 HSTS 怎么配置？有什么坑？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-025：HTTP 强跳 HTTPS 与 HSTS 怎么配置？有什么坑？
**答**：
- 强跳：Nginx 80 端口统一 301 到 https；同域名所有入口收敛到 443。
- HSTS（Strict-Transport-Security）：告诉浏览器"以后对该域只准 https"，消除首跳明文请求窗口，防 SSL 剥离攻击。
- 坑 1：HSTS 一旦下发对子域生效（includeSubDomains），某些纯 HTTP 的内部子域会直接打不开；坑 2：TTL 内无法回退 http，误配只能等过期或从 Chrome HSTS 清单移除。
- 建议节奏：先只给主域开 max-age=300 观察 → 逐步加到 31536000 → 最后确认所有子域 https 后再开 includeSubDomains 并提交 preload。

```nginx
# HTTP 强跳 + 渐进式 HSTS
server {
    listen 80;
    server_name example.com www.example.com;

    # ACME http-01 验证路径要保持 http 可达
    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }

    location / {
        return 301 https://$host$request_uri;
    }
}

server {
    listen 443 ssl http2;
    server_name www.example.com;

    ssl_certificate     /etc/nginx/ssl/www.example.com.fullchain.pem;
    ssl_certificate_key /etc/nginx/ssl/www.example.com.key.pem;
    ssl_protocols TLSv1.2 TLSv1.3;

    # HSTS：确认全站 https 稳定后再调大 max-age 并加 includeSubDomains
    add_header Strict-Transport-Security "max-age=31536000" always;

    # 谨慎阶段配置示例（观察两周无问题后升级）：
    # add_header Strict-Transport-Security "max-age=300" always;
}
```
