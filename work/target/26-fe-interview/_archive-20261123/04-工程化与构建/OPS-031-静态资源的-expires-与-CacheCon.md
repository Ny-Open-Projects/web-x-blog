---
title: [OPS-031] 静态资源的 expires 与 Cache-Control 怎么按资源类型精细化配置？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-031：静态资源的 expires 与 Cache-Control 怎么按资源类型精细化配置？
**答**：
- 用 map 按类型统一决策，比散落的多个 location 好维护：指纹资源长缓存 immutable，普通图片中等缓存，html/json 短或不缓存。
- expires 指令与 Cache-Control 的 max-age 是两种写法，同用时 Cache-Control 优先，建议统一用 add_header 显式声明，可读性好。
- CDN 边缘缓存与浏览器缓存是两层，可用 CDN-Cache-Control/边缘扩展头差异化（边缘长、浏览器短）。
- 配完用 curl -I 逐类验证，并纳入发布前置检查，防止改配置把 html 改成强缓存。

```nginx
# 按扩展名映射缓存策略
map $uri $cache_policy {
    default                                    "no-cache";
    ~*\.html$                                  "no-cache";
    ~*\.(json)$                                "no-cache";
    ~*\.(jpg|jpeg|png|webp|gif|ico)$           "public, max-age=2592000";        # 图片 30d
    ~*\.(woff2|woff|ttf|eot)$                  "public, max-age=31536000";       # 字体 1y
    ~*\/assets\/.+\.[0-9a-f]{8,}\.(js|css)$    "public, max-age=31536000, immutable";
    ~*\.(js|css)$                              "public, max-age=86400";          # 非指纹 1d
}

server {
    listen 80;
    server_name www.example.com;
    root /data/web/current;

    location / {
        add_header Cache-Control $cache_policy;
        try_files $uri $uri/ /index.html;
    }

    # 边缘节点可以比浏览器缓存更久（对 html 也缓存 60s，抗突发回源）
    location = /index.html {
        add_header Cache-Control "no-cache";
        add_header CDN-Cache-Control "max-age=60";
    }
}
```
