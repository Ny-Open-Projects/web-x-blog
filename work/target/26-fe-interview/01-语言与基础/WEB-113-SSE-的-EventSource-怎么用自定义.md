---
title: [WEB-113] SSE 的 EventSource 怎么用？自定义重试与断点续传如何实现？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-113：SSE 的 EventSource 怎么用？自定义重试与断点续传如何实现？
**答**：
- 服务端响应 `text/event-stream`，消息格式为 `event/data/id/retry` 字段，`\n\n` 分隔一条消息；data 可多行。
- `retry: 毫秒` 由服务端下发，浏览器断线后按它自动重连，比 WebSocket 的手写退避省心。
- 自动续传：重连时 EventSource 自动带上 `Last-Event-ID` 请求头（值为最后收到的 id），服务端据此从断点续发，天然防丢。
- 限制：只支持服务端单向推送、仅 GET、依赖 HTTP/1.1 时受浏览器 6 连接限制（HTTP/2 无此问题）。

```javascript
// Node 服务端
const http = require('http');
let seq = 0;
http.createServer((req, res) => {
  if (req.url === '/stream') {
    res.writeHead(200, {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive',
    });
    const lastId = Number(req.headers['last-event-id'] || 0); // 断点续传起点
    seq = Math.max(seq, lastId);
    res.write('retry: 3000\n\n');                             // 断线后 3 秒重连
    const timer = setInterval(() => {
      res.write(`id: ${++seq}\nevent: msg\ndata: ${JSON.stringify({ seq, ts: Date.now() })}\n\n`);
    }, 1000);
    req.on('close', () => clearInterval(timer));
  }
}).listen(3000);

// 浏览器客户端
const es = new EventSource('/stream');
es.addEventListener('msg', (e) => console.log('收到', e.data, 'lastEventId', e.lastEventId));
es.onerror = () => console.log('连接断开，浏览器将按 retry 自动重连'); // 无需手写重连
```
