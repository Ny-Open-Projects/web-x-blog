---
title: [WEB-018] 304 Not Modified 是怎么工作的？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-018：304 Not Modified 是怎么工作的？
**答**：
- 304 属于协商缓存流程：浏览器带着缓存的校验头（`If-None-Match` 对应 ETag，或 `If-Modified-Since` 对应 Last-Modified）去问服务器。
- 资源没变，服务器返回 304 且无响应体，浏览器直接用本地缓存；变了则返回 200 + 新资源。
- 304 只在响应里有 `Cache-Control: no-cache` 或缓存过期时才会触发，`max-age` 未到期不会发请求。
- 304 的收益是省流量不省请求：请求仍然发生，弱网下仍有延迟，强缓存才是零请求。

```javascript
// Node.js 原生实现协商缓存，观察 304 的产生条件
const http = require('http');
const crypto = require('crypto');

const resource = { body: JSON.stringify({ version: 42 }), type: 'application/json' };
const etag = crypto
  .createHash('sha256')
  .update(resource.body)
  .digest('hex')
  .slice(0, 16);

http
  .createServer((req, res) => {
    res.setHeader('Cache-Control', 'no-cache'); // 每次都要协商，允许 304
    if (req.headers['if-none-match'] === etag) {
      res.writeHead(304); // 资源未变：无响应体
      return res.end();
    }
    res.writeHead(200, { 'Content-Type': resource.type, ETag: etag });
    res.end(resource.body);
  })
  .listen(3001);
// 第一次请求 200 带 ETag；第二次请求带 If-None-Match，命中则返回 304
```
