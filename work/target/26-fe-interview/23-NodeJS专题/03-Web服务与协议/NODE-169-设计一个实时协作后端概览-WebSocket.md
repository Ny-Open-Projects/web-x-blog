---
title: [NODE-169] 设计一个实时协作后端概览（WebSocket + CRDT）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-169：设计一个实时协作后端概览（WebSocket + CRDT）？
**答**：
- 分工：**合并交给客户端 CRDT 库**（如 Yjs，更新可交换/可合并，乱序到达也正确），服务端只做中继、排序、持久化——服务端不做 OT 变换，复杂度大幅下降。
- 数据流：op 到达 → 合并进房间状态 → 广播给同房间其他人 → 防抖持久化（合并 2s 内更新）。
- 房间与连接：WS 网关（NODE-073）+ sticky（NODE-141）；presence（光标/选区）高频小消息走独立频道，不进 CRDT 不持久化。
- 离线与快照：客户端本地 pending 队列 + 上线 sync（状态向量 diff）；定期快照加速新加入者初始化。

```javascript
const Y = require('yjs');
const rooms = new Map(); // docId → { ydoc, persistTimer }

io.on('connection', (socket) => {
  socket.on('doc:join', async ({ docId }) => {
    socket.join(docId);
    const room = rooms.get(docId) ?? await loadRoom(docId); // DB/快照恢复
    rooms.set(docId, room);
    socket.emit('doc:sync', Y.encodeStateAsUpdate(room.ydoc)); // 全量初始化
  });

  socket.on('doc:op', ({ docId, update }) => {
    const room = rooms.get(docId);
    Y.applyUpdate(room.ydoc, update);            // CRDT 合并：天然支持乱序并发
    socket.to(docId).emit('doc:op', { update }); // 广播给其他人
    debouncedPersist(docId, 2000);               // 防抖持久化合并更新
  });

  socket.on('doc:presence', ({ docId, cursor }) =>
    socket.to(docId).emit('doc:presence', { uid: socket.uid, cursor })); // 不持久化
});
```
