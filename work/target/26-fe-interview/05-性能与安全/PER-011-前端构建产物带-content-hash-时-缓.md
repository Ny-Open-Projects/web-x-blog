---
title: [PER-011] 前端构建产物带 content hash 时，缓存策略如何设计？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-011：前端构建产物带 content hash 时，缓存策略如何设计？

**答**：
- 带内容 hash 的 JS/CSS/图片：内容变则文件名变，可以放心 `max-age=31536000, immutable` 一年强缓存。
- HTML 是资源引用的入口，必须 `no-cache` 每次协商，否则发布后用户拿到的还是旧引用。
- `immutable` 让浏览器在 max-age 内**不再发起协商请求**，节省大量 304 往返。
- 注意发布顺序：先传带新 hash 的静态资源，再更新 HTML，避免出现引用不存在的资源。

```nginx
# 构建产物形如 app.a1b2c3.js：内容一变文件名就变，可放心长缓存
location /assets/ {
    add_header Cache-Control "public, max-age=31536000, immutable";
}

# HTML 引用了带 hash 的资源，自身必须每次协商，保证发布后立刻生效
location / {
    try_files $uri $uri/ /index.html;
    add_header Cache-Control "no-cache";
}
```
