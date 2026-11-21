---
title: [OPT-022] 接口的 HTTP 缓存如何在实战中配置？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-022：接口的 HTTP 缓存如何在实战中配置？

**答**：
- 强缓存：`Cache-Control: max-age=60` 在有效期内不发请求，适合基本不变的字典数据。
- 协商缓存：服务端下发 `ETag`，浏览器带 `If-None-Match` 回验，命中返回 304 只传头不传体，适合更新频繁但内容可对比的数据。
- 中间层：`s-maxage` 控制 CDN/代理缓存时长，`private` 防止公共缓存存储带用户身份的响应。
- 鉴权、个性化接口一律 `Cache-Control: private, no-store`，避免缓存投毒与串号。

```javascript
// 一一对应：Express 接口缓存三件套实战
import express from 'express';
import { createHash } from 'node:crypto';
const app = express();

// 1. 字典数据：强缓存 5 分钟
app.get('/api/dict', (_req, res) => {
  res.set('Cache-Control', 'public, max-age=300');
  res.json(DICT);
});

// 2. 列表数据：协商缓存，内容不变只回 304
app.get('/api/notes', (req, res) => {
  const body = JSON.stringify(getNotes(req.query.uid));
  const etag = 'W/"' + createHash('md5').update(body).digest('hex') + '"';
  res.set('ETag', etag);
  if (req.headers['if-none-match'] === etag) return res.sendStatus(304);
  res.set('Cache-Control', 'private, max-age=0, must-revalidate');
  res.send(body);
});

// 3. 用户隐私接口：任何层都不缓存
app.get('/api/me', (req, res) => {
  res.set('Cache-Control', 'private, no-store');
  res.json(getMe(req));
});

app.listen(3000);
```
