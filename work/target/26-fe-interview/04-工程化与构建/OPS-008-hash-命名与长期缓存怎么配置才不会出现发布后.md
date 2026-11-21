---
title: [OPS-008] hash 命名与长期缓存怎么配置才不会出现"发布后用户看不到新版本"？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-008：hash 命名与长期缓存怎么配置才不会出现"发布后用户看不到新版本"？
**答**：
- 分层策略：带 content hash 的静态资源（js/css/图片）设 `Cache-Control: public, max-age=31536000, immutable`（一年+不可变）；index.html 设 `no-cache`，每次协商校验。
- immutable 告诉浏览器连条件请求都不发，彻底消除"304 但还是旧文件"的窗口。
- 文件内容变了但文件名没变（如配置 json、图片覆盖式更新）绝对不能加 immutable，会永久卡死旧内容。
- 发布后"看不到新版"的根因几乎都是 index.html 被中间层（CDN/代理/浏览器）缓存了，排查顺序：CDN → 网关 → 浏览器。

```nginx
# 静态资源缓存分层：hash 资源一年 immutable，入口 html 永远协商
server {
    listen 80;
    server_name www.example.com;
    root /data/web/current;

    # 1. 指纹资源：文件名含 8 位以上 hash，内容永不变化
    location ~* ^/assets/.+\.[0-9a-f]{8,}\.(js|css|woff2|png|jpg|svg)$ {
        expires 1y;
        add_header Cache-Control "public, max-age=31536000, immutable";
        access_log off;
    }

    # 2. 非指纹资源（如 config.json、favicon）：短缓存 + 必须协商
    location ~* \.(json|ico|txt)$ {
        add_header Cache-Control "no-cache";
        expires epoch;
    }

    # 3. 入口：no-cache 保证每次拿到最新版本清单
    location = /index.html {
        add_header Cache-Control "no-cache, no-store, must-revalidate";
        add_header Pragma "no-cache";
        add_header ETag on;
    }

    location / {
        try_files $uri $uri/ /index.html;
    }
}
```
