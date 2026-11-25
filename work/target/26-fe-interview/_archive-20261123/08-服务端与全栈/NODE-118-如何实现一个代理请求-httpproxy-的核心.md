---
title: [NODE-118] 如何实现一个代理请求（http-proxy 的核心思想）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, 20]
type: 笔试题
---

## NODE-118：如何实现一个代理请求（http-proxy 的核心思想）？
**答**：
- 反向代理本质：原样转发请求行/头/body，把上游响应回写客户端；body 全程 **pipe 流式**，不落内存，天然支持大文件与 SSE。
- 关键改写：`host` 头（changeOrigin）、`x-forwarded-for`（真实 IP 链，追加而非覆盖）、`x-request-id`（链路透传）。
- 错误处理三态：上游连接失败 → 502；客户端中途断开 → destroy 上游连接防泄漏；响应头已发再出错 → 只能断开连接。
- nginx/http-proxy 的增量能力：负载均衡、缓存、重写规则、WebSocket upgrade 透传——思想一致。

```javascript
const http = require('http');
const crypto = require('crypto');

const server = http.createServer((req, res) => {
  const upstream = http.request({
    host: '127.0.0.1', port: 9000,
    method: req.method, path: req.url,
    headers: {
      ...req.headers,
      host: 'upstream.internal', // changeOrigin：改写 Host 头
      'x-forwarded-for': [req.headers['x-forwarded-for'], req.socket.remoteAddress]
        .filter(Boolean).join(', '), // 真实 IP 链：追加
      'x-forwarded-proto': 'https',
      'x-request-id': req.headers['x-request-id'] ?? crypto.randomUUID(),
    },
  }, (pRes) => {
    res.writeHead(pRes.statusCode ?? 502, pRes.headers);
    pRes.pipe(res); // 响应流式回写
  });
  req.pipe(upstream); // 请求体流式转发
  upstream.on('error', () => {
    if (!res.headersSent) { res.statusCode = 502; res.end('Bad Gateway'); }
    else res.destroy();
  });
  req.on('aborted', () => upstream.destroy()); // 客户端断开掐上游，防连接泄漏
});
server.listen(8000);
```
