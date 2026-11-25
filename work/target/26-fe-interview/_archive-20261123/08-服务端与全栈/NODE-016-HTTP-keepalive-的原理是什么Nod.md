---
title: [NODE-016] HTTP keep-alive 的原理是什么？Node 服务端与客户端分别如何管理连接？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-016：HTTP keep-alive 的原理是什么？Node 服务端与客户端分别如何管理连接？
**答**：
- keep-alive 复用一条 TCP 连接发送多个 HTTP 请求，省去每次 TCP 三次握手 + TLS 握手（HTTPS 场景一次握手可达 1-2 RTT）。HTTP/1.1 默认开启。
- 服务端：`server.keepAliveTimeout`（默认 5s，**小于常见 LB 的空闲超时会引发 502**，Nginx 后要调大，如 65s）与 `headersTimeout`（防慢速攻击）。Node 19+ 默认开启 keep-alive。
- 客户端：`http.Agent` 维护连接池，`maxSockets` 控制并发（默认 Infinity 会对同一 host 打满 fd），BFF 调用下游必须配 Agent，否则高并发下 TIME_WAIT 爆炸。

```javascript
const http = require('node:http');

// 服务端：连接参数调优
const server = http.createServer((req, res) => {
  res.writeHead(200, { connection: 'keep-alive' });
  res.end('ok');
});
server.keepAliveTimeout = 65000;   // 必须大于 LB/Nginx 的空闲超时，避免 502
server.headersTimeout = 66000;     // 必须 > keepAliveTimeout
server.maxHeadersCount = 100;      // 限制头数量
server.listen(3000);

// 客户端（BFF 调用下游）：连接池 Agent
const agent = new http.Agent({
  keepAlive: true,
  keepAliveMsecs: 30000,   // 空闲连接保活 30s
  maxSockets: 100,         // 对同一 host 最多 100 并发连接
  maxFreeSockets: 10,      // 空闲保留 10 条
  timeout: 5000,
});

function callDownstream(path) {
  return new Promise((resolve, reject) => {
    const req = http.request(
      { host: 'localhost', port: 3000, path, agent, timeout: 3000 },
      (res) => {
        let data = '';
        res.on('data', (c) => (data += c));
        res.on('end', () => resolve(JSON.parse(data)));
      },
    );
    req.on('timeout', () => req.destroy(new Error('downstream timeout')));
    req.on('error', reject);
    req.end();
  });
}
callDownstream('/health').then(console.log);
```
