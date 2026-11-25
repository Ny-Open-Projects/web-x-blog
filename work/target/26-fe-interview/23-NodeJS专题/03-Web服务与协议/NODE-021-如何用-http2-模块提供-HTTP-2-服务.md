---
title: [NODE-021] 如何用 http2 模块提供 HTTP/2 服务？带来了什么收益？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-021：如何用 http2 模块提供 HTTP/2 服务？带来了什么收益？
**答**：
- HTTP/2 核心收益：**二进制分帧、多路复用**（一个 TCP 并发多个 stream，解决 HTTP/1.1 队头阻塞与 6 连接限制）、**头部压缩 HPACK**、**服务器推送**（已废弃趋势）。
- 浏览器只支持 **H2 over TLS**（h2），明文 h2c 一般用于内部 gRPC。Node 用 `http2.createSecureServer`（`allowHTTP1: true` 可同时兼容 HTTP/1.1 老客户端）。
- 注意点：多路复用让**单条 TCP 更容易被打满**（丢包时全队头阻塞），所以配合 TLS1.3/QUIC（HTTP/3）是演进方向；服务端实现关注 `stream` 事件而非 `request` 事件。

```javascript
const http2 = require('node:http2');
const fs = require('node:fs');

const server = http2.createSecureServer({
  key: fs.readFileSync('localhost+2-key.pem'),
  cert: fs.readFileSync('localhost+2.pem'),
  allowHTTP1: true, // 兼容不支持 h2 的老客户端降级为 HTTP/1.1
  settings: { maxConcurrentStreams: 100 }, // 每连接最大并发流
});

server.on('stream', (stream, headers) => {
  const path = headers[':path'];           // HTTP/2 伪头部 :method :path :authority
  if (path === '/api/data') {
    stream.respond({
      'content-type': 'application/json; charset=utf-8',
      ':status': 200,
    });
    // 分多次 write 即多个 data 帧，浏览器可提前渲染——多路复用的直观体验
    stream.write(JSON.stringify({ part: 1 }));
    setTimeout(() => stream.end(JSON.stringify({ part: 2 })), 100);
  } else {
    stream.respond({ ':status': 404 });
    stream.end();
  }
});

server.on('sessionError', (err) => console.error('h2 session error:', err.code));
server.listen(8443);
// curl -k --http2 https://localhost:8443/api/data
```

---

## 四、Express 与 Koa
