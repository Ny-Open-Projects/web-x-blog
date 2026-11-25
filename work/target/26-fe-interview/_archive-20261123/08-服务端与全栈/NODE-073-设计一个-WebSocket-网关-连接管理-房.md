---
title: [NODE-073] 设计一个 WebSocket 网关（连接管理、房间、广播）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-073：设计一个 WebSocket 网关（连接管理、房间、广播）？
**答**：
- 职责：连接鉴权（握手时验 JWT，拒绝时 401）、连接注册表（uid → socket）、**房间模型**（加入/退出/按房间广播）、心跳保活（ping/pong 清理僵尸连接）、横向扩展（多实例间用 **Redis Pub/Sub** 转发广播，本实例只发给自己持有的连接）。
- 关键设计：连接亲和——LB 需支持 sticky session（ws 长连接不能随意换实例）；广播合并与节流（高频消息合并批量发）；消息协议统一 `{type, payload, ts}`；下线事件驱动业务（房间人数同步）。
- 生产实现基于 `ws` 库（比 socket.io 轻，自己控制协议）。

```javascript
const { WebSocketServer } = require('ws');
const Redis = require('ioredis');
const sub = new Redis(), pub = new Redis();
const wss = new WebSocketServer({ server: httpServer, maxPayload: 64 * 1024 });
const rooms = new Map();      // roomId → Set<ws>
const sockets = new Map();    // ws → { uid, rooms, alive }

// 1. 连接鉴权：握手阶段校验 JWT
wss.on('connection', async (ws, req) => {
  const token = new URL(req.url, 'http://x').searchParams.get('token');
  let claims;
  try { claims = jwt.verify(token, JWT_SECRET); }
  catch { ws.close(4001, 'unauthorized'); return; }

  sockets.set(ws, { uid: claims.uid, rooms: new Set(), alive: true });
  ws.on('pong', () => { sockets.get(ws).alive = true; });

  ws.on('message', (raw) => {
    const msg = JSON.parse(raw);
    if (msg.type === 'join') joinRoom(ws, msg.room);
    else if (msg.type === 'leave') leaveRoom(ws, msg.room);
    else if (msg.type === 'chat') broadcast(msg.room, { type: 'chat', from: claims.uid, payload: msg.payload });
  });

  ws.on('close', () => {
    const s = sockets.get(ws);
    s.rooms.forEach((r) => leaveRoom(ws, r));
    sockets.delete(ws);
  });
});

// 2. 房间管理
function joinRoom(ws, roomId) {
  if (!rooms.has(roomId)) rooms.set(roomId, new Set());
  rooms.get(roomId).add(ws);
  sockets.get(ws).rooms.add(roomId);
  broadcast(roomId, { type: 'member_joined', payload: { count: rooms.get(roomId).size } });
}
function leaveRoom(ws, roomId) {
  rooms.get(roomId)?.delete(ws);
  sockets.get(ws)?.rooms.delete(roomId);
}

// 3. 广播：本地直发 + Redis Pub/Sub 跨实例
function broadcast(roomId, message) {
  const data = JSON.stringify({ ...message, ts: Date.now() });
  for (const ws of rooms.get(roomId) ?? []) {
    if (ws.readyState === 1) ws.send(data);            // OPEN 才发
  }
  pub.publish(`room:${roomId}`, data);                 // 通知其他实例
}
sub.subscribe('room:*'); // psubscribe 用于模式订阅
sub.on('pmessageBuffer', (_pattern, channel, data) => {
  const roomId = channel.toString().split(':')[1];
  for (const ws of rooms.get(roomId) ?? []) ws.send(data.toString());
});

// 4. 心跳：30s 一轮，两轮未 pong 判定僵尸连接
setInterval(() => {
  for (const [ws, s] of sockets) {
    if (!s.alive) { ws.terminate(); sockets.delete(ws); continue; }
    s.alive = false;
    ws.ping();
  }
}, 30000).unref();
```
