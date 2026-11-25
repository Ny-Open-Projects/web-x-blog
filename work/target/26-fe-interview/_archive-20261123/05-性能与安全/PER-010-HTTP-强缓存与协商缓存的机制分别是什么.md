---
title: [PER-010] HTTP 强缓存与协商缓存的机制分别是什么？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-010：HTTP 强缓存与协商缓存的机制分别是什么？

**答**：
- **强缓存**：浏览器直接用本地副本，不发请求。由 `Cache-Control: max-age`（HTTP/1.1，优先）或 `Expires`（绝对时间，受本地时钟影响）控制。
- **协商缓存**：缓存过期后携带标识询问服务器，资源没变则返回 304 只传 header。标识用 `ETag/If-None-Match` 或 `Last-Modified/If-Modified-Since`。
- 常用指令：`no-cache`（可以缓存但每次协商）、`no-store`（完全不缓存）、`public/private`、`immutable`（期内不再协商）。
- 前端工程的关键是按"文件是否带 hash"分配策略，而不是一刀切。

```nginx
server {
    listen 80;

    # HTML 入口：每次都协商，保证发布后立即生效
    location = /index.html {
        add_header Cache-Control "no-cache";
        etag on;   # 协商缓存标识，配合 If-None-Match 返回 304
    }

    # 接口数据：完全禁缓存，防止读到脏数据
    location /api/ {
        proxy_pass http://backend;
        add_header Cache-Control "no-store";
    }
}
```
