---
title: [NODE-028] 如何实现一个生产级静态文件服务？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, 20]
type: 笔试题
---

## NODE-028：如何实现一个生产级静态文件服务？
**答**：
- 核心要素：① **路径穿越防护**——`path.normalize` + `startsWith(root)` 校验，杜绝 `../../etc/passwd`；② **协商缓存**——`ETag`（mtime+size 哈希）与 `Last-Modified`，命中 `If-None-Match` 回 304；③ **强缓存**——带 hash 的资源下发 `Cache-Control: public, max-age=31536000, immutable`；④ **Range 断点续传**（206 Partial Content）；⑤ MIME 映射；⑥ 正确用 `sendFile` 流式发送。
- 高频追问：为什么 hash 资源用 immutable（浏览器不再发 revalidate 请求）；`Content-Length` 与 gzip 的关系（压缩后需重新计算，交给流）。

```javascript
const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');

const ROOT = path.join(__dirname, 'public');
const MIME = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.png': 'image/png', '.json': 'application/json' };

http.createServer((req, res) => {
  let pathname = decodeURIComponent(new URL(req.url, 'http://x').pathname);
  if (pathname === '/') pathname = '/index.html';

  // 1. 路径穿越防护
  const filePath = path.normalize(path.join(ROOT, pathname));
  if (!filePath.startsWith(ROOT)) { res.writeHead(403).end(); return; }

  fs.stat(filePath, (err, stat) => {
    if (err || !stat.isFile()) { res.writeHead(404).end('Not Found'); return; }

    // 2. 协商缓存：ETag = mtime + size
    const etag = `"${crypto.createHash('md5').update(`${stat.mtimeMs}-${stat.size}`).digest('hex')}"`;
    res.setHeader('etag', etag);
    res.setHeader('last-modified', stat.mtime.toUTCString());
    if (req.headers['if-none-match'] === etag) { res.writeHead(304).end(); return; }

    const ext = path.extname(filePath);
    res.setHeader('content-type', MIME[ext] || 'application/octet-stream');
    // 3. hash 文件强缓存（文件名包含 [hash] 时）
    if (/\.[0-9a-f]{8,}\./.test(pathname) || pathname.startsWith('/assets/')) {
      res.setHeader('cache-control', 'public, max-age=31536000, immutable');
    } else {
      res.setHeader('cache-control', 'no-cache'); // html 每次协商
    }

    // 4. Range 断点续传
    const range = req.headers.range;
    if (range) {
      const [, startStr, endStr] = range.match(/bytes=(\d*)-(\d*)/) || [];
      let start = startStr ? parseInt(startStr) : stat.size - parseInt(endStr);
      let end = endStr ? parseInt(endStr) : stat.size - 1;
      if (start >= stat.size) { res.writeHead(416).end(); return; }
      res.writeHead(206, { 'content-range': `bytes ${start}-${end}/${stat.size}`, 'content-length': end - start + 1 });
      return fs.createReadStream(filePath, { start, end }).pipe(res);
    }

    res.setHeader('content-length', stat.size);
    fs.createReadStream(filePath).pipe(res);   // 流式发送，内存恒定
  });
}).listen(3000);
```
