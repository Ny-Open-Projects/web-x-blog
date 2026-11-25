---
title: [NODE-692] HTTP 缓存头策略（服务端控制）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-692：HTTP 缓存头怎么做？
**答**：
- 头策略分层：静态资源 immutable（SCN-ENG-241）、API 响应（私有数据 no-store / 可缓存数据 max-age + Vary）、HTML（no-cache 协商——SCN-ENG-241）。
- 协商缓存：ETag/Last-Modified（304 省传输——动态内容的轻量缓存）；ETag 生成（内容 hash——弱 ETag 用于动态）。
- Vary 的语义：Vary: Accept-Encoding/User-Agent（缓存键维度——多端响应不同时必须 Vary，否则串缓存）。
- 缓存与授权冲突：带 Authorization 的响应默认不可共享缓存（Cache-Control: private——CDN 不缓存用户数据，防越权缓存——安全第一）。
- 追问钩子：为什么「带 Authorization 的响应」必须 private 或 no-store——共享缓存（CDN/代理）会缓存 A 用户的响应并可能返回给 B 用户（越权缓存——严重数据泄露）；`Cache-Control: private` 限定仅浏览器缓存——授权与缓存的交互是服务端缓存策略的安全红线。

```javascript
res.set('Cache-Control', 'private, max-age=60');       // 用户数据：浏览器可缓存
res.set('Cache-Control', 'no-store');                  // 敏感数据：完全不缓存
res.set('ETag', etag(body));                           // 协商缓存
if (req.fresh) return res.status(304).end();           // 304 省传输
res.set('Vary', 'Accept-Encoding, X-Gray-Bucket');     // 灰度桶必须 Vary（SCN-OPS-216）
```
