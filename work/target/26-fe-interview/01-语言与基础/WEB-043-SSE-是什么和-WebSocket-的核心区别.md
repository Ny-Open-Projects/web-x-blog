---
title: [WEB-043] SSE 是什么？和 WebSocket 的核心区别？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-043：SSE 是什么？和 WebSocket 的核心区别？
**答**：
- SSE（Server-Sent Events）基于普通 HTTP 长连接，`Content-Type: text/event-stream`，服务器单向持续推送，浏览器用内置 EventSource 接收。
- 天然走 HTTP：自动重连（带 `Last-Event-ID` 续传）、代理友好、无需特殊网关配置；WebSocket 是独立协议，双向但重。
- 只能服务器到客户端单向推送；需要客户端上报的交互场景用 WebSocket 或 SSE+fetch 组合。
- 典型场景：AI 流式输出、行情推送、通知feed；连接数受浏览器同域 HTTP 连接限制（HTTP/1.1 下约 6 条）。

```javascript
// 服务端：Node 原生实现 SSE
const http = require('http');

http
  .createServer((req, res) => {
    if (req.url !== '/events') return res.end();
    res.writeHead(200, {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',        // 禁止中间层缓存流
      Connection: 'keep-alive',
    });

    let id = 0;
    const timer = setInterval(() => {
      // 消息格式固定：id / event / data 字段，两条空行表示一条消息结束
      res.write(`id: ${++id}\n`);
      res.write(`event: tick\n`);
      res.write(`data: ${JSON.stringify({ now: Date.now() })}\n\n`);
    }, 1000);

    req.on('close', () => clearInterval(timer)); // 客户端断开要清理，防句柄泄漏
  })
  .listen(8090);
```

```javascript
// 客户端：EventSource 自动重连并携带 Last-Event-ID
const es = new EventSource('/events');

es.addEventListener('tick', (e) => {
  console.log('tick:', JSON.parse(e.data), 'lastId:', e.lastEventId);
});
es.onmessage = (e) => console.log('default event:', e.data);

// 断线后 EventSource 自动重连；需要自控时可 close 后手动重建
setTimeout(() => es.close(), 30000);
```
