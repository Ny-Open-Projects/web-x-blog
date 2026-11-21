---
title: [OPS-020] 为什么 index.html 一定不能被 CDN 缓存？各层分别怎么配置？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-020：为什么 index.html 一定不能被 CDN 缓存？各层分别怎么配置？
**答**：
- index.html 是"版本清单"：它引用哪些 hash chunk 决定了用户看到的功能。它若被缓存，新版本发布后用户拿到旧 html，请求的旧 chunk 可能已被清理，直接白屏/404。
- 正确姿势：CDN 对 html 跟随源站 Cache-Control（no-cache），或对 html 路径设置"不缓存"规则；源站 Nginx 也要显式 no-cache。
- 各家 CDN 配置方式不同，但共性是"按文件后缀/路径配置缓存 TTL，html 必须为 0 或遵循源站"。
- 验证方法：curl -I 看响应头里 CDN 加的缓存标记（如 X-Cache: MISS/HIT、Ali-Swift-Swift-Time）与 Cache-Control 实际值。

```nginx
# 源站 Nginx：为不同资源声明正确的缓存策略，CDN 按此遵循
server {
    listen 80;
    server_name www.example.com;
    root /data/web/current;

    # html 入口：CDN 不可缓存，浏览器每次协商
    location ~* \.html$ {
        add_header Cache-Control "no-cache";
        add_header CDN-Cache-Control "no-store" always;  # 部分支持该头的 CDN 可识别
    }

    # 指纹资源：边缘与浏览器都长缓存
    location /assets/ {
        add_header Cache-Control "public, max-age=31536000, immutable";
    }

    # API 与页面路由：绝不缓存
    location /api/ {
        proxy_pass http://backend;
        add_header Cache-Control "no-store";
    }

    location / {
        add_header Cache-Control "no-cache";
        try_files $uri $uri/ /index.html;
    }
}
```
