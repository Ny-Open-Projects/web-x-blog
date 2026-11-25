---
title: [NODE-117] HTTP 管线化与队头阻塞是怎么回事？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-117：HTTP 管线化与队头阻塞是怎么回事？
**答**：
- HTTP/1.1 一条连接同一时刻只能有一个请求在途（响应必须按序返回）→ **应用层队头阻塞**；管线化允许连发但响应仍按序，慢响应堵住全部，实际被浏览器禁用。
- 对策一：连接池并发（`maxSockets`，NODE-116）——空间换时间，连接数有上限。
- 对策二：**HTTP/2 多路复用**——一条 TCP 连接上多个 stream 交错传输，真并行；但 TCP 层丢包会阻塞所有 stream（传输层队头阻塞），HTTP/3/QUIC 才根治。
- 服务端启示：给 BFF 的下游接口尽量上 HTTP/2；响应慢的大接口考虑流式或拆分。

```javascript
const http2 = require('http2');
// HTTP/2 客户端：单连接多路复用
const session = http2.connect('https://upstream.internal');
function h2get(path) {
  return new Promise((resolve, reject) => {
    const stream = session.request({ ':path': path }); // 无需等前一个响应
    let data = '';
    stream.setEncoding('utf8');
    stream.on('data', (c) => (data += c));
    stream.on('end', () => resolve(data));
    stream.on('error', reject);
  });
}
// 三个请求在同一连接上真并行（HTTP/1.1 需要 3 条连接或串行）
const [a, b, c] = await Promise.all([h2get('/a'), h2get('/b'), h2get('/c')]);

// 对照：HTTP/1.1 + 连接池
const agent = new http.Agent({ keepAlive: true, maxSockets: 10 });
// Promise.all 三个 http.get({ agent }) → 最多同时占 3 条连接，每连接仍串行
```
