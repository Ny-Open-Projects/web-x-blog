---
title: [WEB-023] 协商缓存 ETag 和 Last-Modified 的原理与优先级？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-023：协商缓存 ETag 和 Last-Modified 的原理与优先级？
**答**：
- 服务器下发 ETag（资源指纹）与 Last-Modified（修改时间）；浏览器再次请求时带上 `If-None-Match` 与 `If-Modified-Since`。
- 服务器两把钥匙都收到时优先比对 ETag，命中才继续看 Last-Modified；ETag 优先级更高。
- Last-Modified 秒级精度，1 秒内多次修改检测不出；分布式机器 mtime 不一致会误判；ETag 内容寻址更准但计算有成本。
- 有的场景可以只用 ETag，或自定义 ETag 生成规则（如版本号 + 文件哈希）。

```javascript
// 同时使用 ETag 与 Last-Modified 的协商缓存实现
const http = require('http');
const fs = require('fs');

http
  .createServer((req, res) => {
    const filePath = './app.js';
    const stat = fs.statSync(filePath);
    const body = fs.readFileSync(filePath);
    const etag = `W/"${stat.size}-${stat.mtimeMs}"`; // 弱 ETag：按大小+时间生成

    const inm = req.headers['if-none-match'];
    const ims = req.headers['if-modified-since'];

    // ETag 优先：匹配则直接 304；不匹配再看 Last-Modified
    if (inm === etag || (inm === undefined && ims && new Date(ims).getTime() === Math.floor(stat.mtimeMs / 1000) * 1000)) {
      res.writeHead(304);
      return res.end();
    }
    res.writeHead(200, {
      ETag: etag,
      'Last-Modified': stat.mtime.toUTCString(),
      'Cache-Control': 'no-cache',
    });
    res.end(body);
  })
  .listen(3004);
```
