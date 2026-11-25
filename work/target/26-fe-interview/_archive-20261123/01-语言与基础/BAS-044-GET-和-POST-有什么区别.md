---
title: [BAS-044] GET 和 POST 有什么区别？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-044：GET 和 POST 有什么区别？
**答**：
- 语义：GET 获取资源，安全幂等可被缓存；POST 提交数据，不幂等。
- 参数：GET 在 URL query 上，有长度限制且会进浏览器历史和服务器日志；POST 在 body，理论无限制。
- 本质上都是 HTTP 报文，"GET 只能传 2KB"是旧浏览器地址栏限制的误传，不是协议限制。

```javascript
await fetch('/api/list?page=1&size=20'); // GET：参数在 URL，可被缓存、可收藏
await fetch('/api/list', {               // POST：参数在 body
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ filters: { type: 'vip' } }),
});
```
