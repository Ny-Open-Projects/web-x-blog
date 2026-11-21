---
title: [AV-025] 什么是信令？为什么 WebRTC 不规定信令协议？（高频压轴）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-025：什么是信令？为什么 WebRTC 不规定信令协议？（高频压轴）
**答**：
- 信令 = 在建连前交换"元信息"的通道：SDP（媒体能力）、ICE candidate（网络地址）、加入/离开房间等业务消息。
- W3C 故意不规定信令协议，因为业务形态千差万别（会议/直播/IoT），任何协议都能用（WebSocket/HTTP/甚至二维码）。
- 自研信令服务典型实现：WebSocket 房间服务器，消息类型 join/offer/answer/candidate/leave，按 roomId 广播或单播。
- 信令必须先于媒体工作：没有信令，双方互相不知道对方的 SDP 与候选地址。
- 生产要求：信令通道要可靠（见第九章），且信令服务器是唯一"中心点"，它挂了所有人无法建连。

```javascript
// 极简信令服务器（Node ws）+ 客户端封装
// server.js
import { WebSocketServer } from 'ws';
const wss = new WebSocketServer({ port: 8080 });
const rooms = new Map(); // roomId -> Set<ws>
wss.on('connection', (ws) => {
  ws.on('message', (raw) => {
    const msg = JSON.parse(raw);
    if (msg.type === 'join') {
      ws.roomId = msg.roomId;
      if (!rooms.has(msg.roomId)) rooms.set(msg.roomId, new Set());
      rooms.get(msg.roomId).add(ws);
      // 通知房间内其他人
      rooms.get(msg.roomId).forEach((c) => {
        if (c !== ws) c.send(JSON.stringify({ type: 'peer-joined', from: msg.uid }));
      });
      return;
    }
    // offer/answer/candidate/leave：转发给指定对端或全房间
    rooms.get(ws.roomId)?.forEach((c) => {
      if (c !== ws && (!msg.to || c.uid === msg.to)) c.send(raw);
    });
  });
  ws.on('close', () => ws.roomId && rooms.get(ws.roomId)?.delete(ws));
});
```

```javascript
// client.js 信令客户端
class Signaling {
  constructor(url) {
    this.ws = new WebSocket(url);
    this.handlers = new Map();
    this.ws.onmessage = (e) => {
      const msg = JSON.parse(e.data);
      this.handlers.get(msg.type)?.(msg);
    };
  }
  on(type, fn) { this.handlers.set(type, fn); }
  send(msg) { this.ws.send(JSON.stringify(msg)); }
}
const sig = new Signaling('wss://sig.example.com');
sig.on('offer', async ({ sdp, from }) => { /* 触发 answer 流程 */ });
```
