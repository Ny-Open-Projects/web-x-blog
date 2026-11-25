---
title: [NODE-017] 如何防护大请求体与慢速攻击（Slowloris）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-017：如何防护大请求体与慢速攻击（Slowloris）？
**答**：
- 大请求体：**永远不要无限制 `data` 拼接**。策略：校验 `content-length` 上限 + 流式累加计数超限即 `req.destroy()` 并回 413；文件上传用流式直写磁盘/对象存储。
- 慢速攻击（Slowloris）：攻击者慢慢发 header 或 body，占住连接不释放，耗尽 `maxConnections`。对策：`server.headersTimeout`/`requestTimeout`（Node 18+ 默认 300s，建议收紧到 30s）、`server.maxRequestsPerSocket`、前置 Nginx `client_body_timeout`。
- 服务级兜底：`server.maxConnections` 限总量、连接空闲计时器踢出慢连接。

```javascript
const http = require('node:http');

const server = http.createServer((req, res) => {
  const declared = Number(req.headers['content-length'] || 0);
  if (declared > 5 * 1024 * 1024) {          // 声明超 5MB 直接拒绝
    res.writeHead(413).end();
    return req.destroy();
  }
  let size = 0;
  req.on('data', (chunk) => {
    size += chunk.length;
    if (size > 5 * 1024 * 1024) {            // 实际超限（chunked 无 content-length 时靠这里）
      res.writeHead(413).end();
      req.destroy();                          // 立即断开，不再读剩余数据
    }
  });
  req.on('end', () => res.writeHead(200).end('ok'));
});

server.requestTimeout = 30000;      // 整个请求 30s 内必须完成（防慢速 body）
server.headersTimeout = 25000;      // header 必须 25s 内发完（防 Slowloris 慢发头）
server.maxHeadersCount = 200;
server.maxConnections = 2000;       // 最大并发连接兜底
server.listen(3000);

// 每个连接加空闲超时：60s 无数据就踢掉
server.on('connection', (socket) => {
  socket.setTimeout(60000, () => socket.destroy());
});
```
