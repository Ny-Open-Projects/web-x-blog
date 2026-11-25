---
title: [OPT-127] HTML/JS/CSS/API 四类资源的 HTTP 缓存分层策略矩阵怎么定？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-127：HTML/JS/CSS/API 四类资源的 HTTP 缓存分层策略矩阵怎么定？

**答**：
- HTML 入口：`no-cache` + ETag/Last-Modified 协商缓存，保证发版即刻生效；SPA 的 index.html 绝不能强缓存。
- 带 hash 的 JS/CSS/图片：`immutable, max-age=31536000` 强缓存一年，改内容必换文件名。
- API GET 数据：按数据时效分层——配置类 `max-age=60, stale-while-revalidate=300`；用户实时数据 `no-store` 或短 max-age。
- CDN 层再加一层 `s-maxage` 区分边缘缓存与浏览器缓存，回源率监控要跟上。

```nginx
# 一一对应：四类资源的缓存策略矩阵（Nginx）
# 1. HTML 入口：协商缓存，发版即时生效
location = /index.html {
    add_header Cache-Control "no-cache, must-revalidate";
    etag on;
}
# 2. 带 hash 的静态资源：一年强缓存 + immutable
location ~* \.(js|css|png|jpg|webp|woff2)$ {
    add_header Cache-Control "public, max-age=31536000, immutable";
}
# 3. API 分层：配置类可短缓存 + SWR，实时类禁缓存
location /api/config {
    add_header Cache-Control "public, max-age=60, stale-while-revalidate=300";
    proxy_pass http://backend;
}
location /api/user {
    add_header Cache-Control "private, no-store";
    proxy_pass http://backend;
}
# 4. CDN 边缘层：s-maxage 控制边缘，回源率走日志监控
# add_header Cache-Control "public, max-age=60, s-maxage=600";
```
