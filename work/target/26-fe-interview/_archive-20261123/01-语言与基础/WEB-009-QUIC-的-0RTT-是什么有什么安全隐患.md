---
title: [WEB-009] QUIC 的 0-RTT 是什么？有什么安全隐患？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-009：QUIC 的 0-RTT 是什么？有什么安全隐患？
**答**：
- 首次连接 QUIC + TLS 1.3 需要 1-RTT 完成握手；会话恢复时客户端可复用此前的密钥材料，在第一个包里就携带加密的请求数据，即 0-RTT。
- 收益：移动弱网下能省一个 RTT，首屏更快。
- 风险：0-RTT 数据没有防重放保护，攻击者可以截获并原样重发这个包；且其中的数据不是前向安全的。
- 工程约定：0-RTT 只用于幂等请求（GET、查询），涉及转账、下单的 POST 禁止放在 0-RTT 中，服务端要校验。

```javascript
// 服务端（Node.js）视角：对 0-RTT 早数据做防御性处理
// 浏览器 fetch 本身不暴露 0-RTT 控制，策略在服务端与 CDN 配置
const http2 = require('http2'); // QUIC 由 nginx/CDN 终结，应用仍走 HTTP/2
const server = http2.createServer((req, res) => {
  const isEarlyData = req.headers['x-early-data'] === '1'; // nginx 注入的标记
  if (isEarlyData && req.method === 'POST') {
    // 非幂等请求拒绝走 0-RTT，要求客户端完整握手后重发
    res.writeHead(425, { 'content-type': 'application/json' }); // 425 Too Early
    return res.end(JSON.stringify({ error: 'retry after handshake' }));
  }
  res.end(JSON.stringify({ ok: true }));
});
server.listen(8443);
```
