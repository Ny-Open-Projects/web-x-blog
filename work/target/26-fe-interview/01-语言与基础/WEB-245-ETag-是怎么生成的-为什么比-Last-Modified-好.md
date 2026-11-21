---
title: [WEB-245] ETag 是怎么生成的？为什么比 Last-Modified 好？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 缓存]
type: 面试题
---

## WEB-245：ETag 是怎么生成的？为什么比 Last-Modified 好？

**答**：
- ETag 生成：默认常用「内容 hash」（强校验，内容变即变）或「mtime+size」（弱校验）；Nginx 默认 `mtime+content-length`，Nginx 配 `etag on` 自动带。
- 优于 Last-Modified 的三点：精度到内容级（1 秒内多次修改可识别）；mtime 变但内容不变时不误判；分布式文件系统 mtime 不可靠时 hash 更稳。
- 弱校验器：`ETag: W/"abc"` 表示内容等价即可（如 gzip 后语义相同），用于协商。
- 代价：强校验要读内容算 hash，动态内容/大文件开销大，很多服务端框架对动态响应用 mtime 版本号替代。
- 坑：负载均衡多机 mtime 不同 → 同一资源 ETag 不一致 → 缓存命中率抖动，需统一 hash 策略。

```javascript
// Node Express 手动生成内容 ETag
const crypto = require('crypto');
app.get('/data.json', (req, res) => {
  const body = JSON.stringify(data);
  const etag = `"${crypto.createHash('md5').update(body).digest('hex')}"`;
  res.set('ETag', etag);
  if (req.headers['if-none-match'] === etag) return res.sendStatus(304);
  res.json(data);
});
```
