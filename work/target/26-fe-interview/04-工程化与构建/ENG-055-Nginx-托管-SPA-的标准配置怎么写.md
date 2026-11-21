---
title: [ENG-055] Nginx 托管 SPA 的标准配置怎么写？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-055：Nginx 托管 SPA 的标准配置怎么写？
**答**：
- try_files $uri $uri/ /index.html 是 SPA 灵魂：路径找不到文件时回退 index.html，交给前端路由，刷新不 404。
- 缓存分层：带 contenthash 的静态资源 immutable 长缓存；index.html 必须 no-cache。
- gzip/brotli 压缩文本资源，图片等已压缩类型跳过。
- 开启 sendfile、tcp_nopush 提升静态文件吞吐。

```nginx
server {
  listen 80;
  server_name example.com;
  root /usr/share/nginx/html;
  index index.html;

  # SPA 路由兜底：找不到文件回退 index.html
  location / {
    try_files $uri $uri/ /index.html;
  }

  # 带 hash 的静态资源：一年 immutable
  location /assets/ {
    add_header Cache-Control "public, max-age=31536000, immutable";
  }

  # index.html 不缓存，保证发版即时生效
  location = /index.html {
    add_header Cache-Control "no-cache";
  }

  gzip on;
  gzip_types text/css application/javascript application/json;
  gzip_min_length 1024;
}
```
