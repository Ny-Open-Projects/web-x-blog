---
title: [NODE-759] 笔试题——实现协作服务器（Yjs 合并 + 持久化 + 房间管理）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-759：手写协作服务器

**需求与边界**：
- 需求：协作服务端（SCN-NODE-660）——① 房间 Doc 管理（加载/缓存/LRU 淘汰）；② update 合并广播（Y.applyUpdate——乱序安全）；③ 持久化防抖落库（快照压缩）；④ 权限校验（读写分离——SCN-OPS-609）。
- 边界：① 大文档快照（encodeStateAsUpdate 全量 vs 增量 update——快照压缩）；② 房间空闲回收（LRU——内存治理，SCN-NODE-672）；③ 观察者与编辑者分离（观察者只广播）。

**答**：
```javascript
const rooms = new LRUCache({ max: 1000, dispose: persistRoom });   // 房间 LRU（空闲回收）
io.use(auth);                                          // SCN-NODE-649 鉴权
io.on('connection', async (socket) => {
  const { roomId, perm } = socket.handshake.auth;
  const doc = rooms.get(roomId) ?? loadRoom(roomId);   // 加载或创建（缓存）
  socket.join(roomId);
  socket.emit('init', Y.encodeStateAsUpdate(doc));     // 全量初始状态
  socket.on('update', (u) => {
    if (!perm.write) return;                           // 只读校验（SCN-OPS-609）
    Y.applyUpdate(doc, u);                             // 合并（乱序安全——SCN-NODE-660）
    socket.to(roomId).emit('update', u);               // 广播增量
  });
});
// 持久化防抖（dispose 时 + 定时）
const persistRoom = debounce((doc, roomId) =>
  db.save(roomId, Y.encodeStateAsUpdate(doc)), 3000);  // 快照落库
```

**评分点**:
- 房间 LRU 管理（空闲回收——内存治理）。
- Y.applyUpdate 乱序安全合并（CRDT 服务器即中继——SCN-NODE-660）。
- 权限校验（只读拒绝写——SCN-OPS-609）。
- 防抖持久化 + 全量 init（新连接同步）。
