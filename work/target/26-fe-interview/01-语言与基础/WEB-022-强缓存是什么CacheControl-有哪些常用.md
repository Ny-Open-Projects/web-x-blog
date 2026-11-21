---
title: [WEB-022] 强缓存是什么？Cache-Control 有哪些常用指令？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-022：强缓存是什么？Cache-Control 有哪些常用指令？
**答**：
- 强缓存：浏览器本地直接使用缓存，不发请求（DevTools 里显示 from disk/memory cache），响应头是 `Cache-Control`（优先级高于 `Expires`）。
- `max-age=N` 相对秒数有效期；`no-cache` 不走强缓存但仍可协商缓存；`no-store` 彻底不缓存。
- `private` 仅浏览器可缓存（代理/CDN 不缓存），`public` 都可缓存；`immutable` 表示有效期内绝不变化，连重验证都不需要。
- `max-age=0, must-revalidate` 等价于每次都协商，是 HTML 的常见配置。

```javascript
// Express 展示典型静态资源缓存策略
const express = require('express');
const app = express();

// 带 hash 的静态资源：一年强缓存 + immutable，文件名变了缓存自然失效
app.use(
  '/static',
  express.static('dist', {
    setHeaders(res) {
      res.setHeader('Cache-Control', 'public, max-age=31536000, immutable');
    },
  })
);

// HTML 本身：永远协商，保证用户拿到最新入口
app.get('/', (req, res) => {
  res.setHeader('Cache-Control', 'no-cache');
  res.sendFile('index.html', { root: 'dist' });
});
app.listen(3003);
```
