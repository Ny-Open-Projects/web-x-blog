---
title: [WEB-341] Vary 头是怎么工作的？为什么 gzip 场景必须配它？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 缓存]
type: 面试题
---

## WEB-341：Vary 头是怎么工作的？为什么 gzip 场景必须配它？
**答**：
- Vary 告诉缓存（浏览器/CDN）：响应按这些请求头的不同取值分开缓存，key 是 URL+Vary 指定头的组合。
- Accept-Encoding: gzip 场景不配 Vary，CDN 会把 gzip 内容发给不支持压缩的客户端（经典事故）。
- 移动端按 UA 出不同内容也依赖 Vary: User-Agent，但会造成缓存碎片，能不分就别分。

```javascript
const cacheKey = (url, vary, headers) =>
  url + '|' + vary.map(h => headers[h.toLowerCase()]).join('|');
const vary = ['Accept-Encoding'];
console.log(cacheKey('/a.js', vary, { 'accept-encoding': 'gzip' }));
// /a.js|gzip 与 /a.js|identity 是两份缓存
```
