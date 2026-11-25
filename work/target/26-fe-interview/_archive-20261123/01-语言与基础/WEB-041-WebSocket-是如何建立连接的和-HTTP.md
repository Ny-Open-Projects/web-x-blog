---
title: [WEB-041] WebSocket 是如何建立连接的？和 HTTP 什么关系？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-041：WebSocket 是如何建立连接的？和 HTTP 什么关系？
**答**：
- WebSocket 握手借道 HTTP：客户端发 Upgrade: websocket 的 GET 请求，带 Sec-WebSocket-Key；服务器回 101 Switching Protocols 和 Sec-WebSocket-Accept。
- 握手成功后协议切换，双方在同一条 TCP 连接上全双工通信，服务器可主动推送，无需轮询。
- 数据以帧为单位传输，开销远小于反复建 HTTP 请求；心跳（ping/pong）保活探测死连接。
- 注意混合内容限制：HTTPS 页面只能连 wss，ws 一般仅用于 http 本地调试；代理与网关需支持长连接与 Upgrade 头。

```javascript
// 服务端：ws 库实现握手后的全双工通信
const { WebSocketServer } = require('ws');
const wss = new WebSocketServer({ port: 8080 });

wss.on('connection', (ws, req) => {
  console.log('client connected:', req.headers['sec-websocket-key']); // 握手后的痕迹

  ws.send(JSON.stringify({ type: 'welcome', ts: Date.now() })); // 服务器主动推送

  ws.on('message', (raw) => {
    const msg = JSON.parse(raw);
    if (msg.type === 'ping') ws.send(JSON.stringify({ type: 'pong', ts: msg.ts })); // 应用层心跳应答
  });
});
```

```javascript
// 客户端：连接、收发、关闭
const socket = new WebSocket('wss://api.example.com/ws');

socket.addEventListener('open', () => {
  socket.send(JSON.stringify({ type: 'ping', ts: Date.now() }));
});
socket.addEventListener('message', (e) => {
  console.log('received:', JSON.parse(e.data));
});
socket.addEventListener('close', (e) => {
  console.log(`closed code=${e.code} reason=${e.reason}`); // 1000 正常关闭
});
socket.addEventListener('error', () => socket.close());
```
