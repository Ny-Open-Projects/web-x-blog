---
title: [NODE-660] 实时协作服务端（OT/CRDT 权威服务器）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-660：实时协作服务端怎么做？
**答**：
- 架构选型：中心化服务器（权威序——OT 变换或 CRDT 合并，服务器是真相源）vs P2P（Yjs 纯 CRDT——服务器只做中继持久化）；协作产品主流是「CRDT 文档 + 服务器权威持久化」。
- 服务器职责：连接管理（房间分组——SCN-NODE-650 WS 网关）、操作校验（权限——SCN-OPS-609 权限矩阵）、合并与版本管理（Yjs update 合并——增量 update 广播）、持久化（防抖落库 + 快照——文档大时 snapshot 压缩）。
- 一致性：服务器序即最终序（客户端按服务器序重放）；离线合并（CRDT 天然支持——上线后 update 交换）。
- 规模：房间隔离（房间间无共享状态——水平拆分天然）；大房间（只读观察者与编辑者分离——观察者不参与合并）。
- 追问钩子：为什么协作服务器选「CRDT 合并」而非「OT 变换」成为主流——OT 需要服务器维持变换上下文（每个操作对历史所有操作变换——复杂且服务端串行是瓶颈）；CRDT 的 update 可乱序合并（服务器只做转发+持久化，无需理解操作语义）——服务器从「变换计算器」降级为「中继器」，水平扩展免费。

```javascript
import * as Y from 'yjs';
io.on('connection', (socket) => {
  socket.join(roomId);
  const doc = getRoomDoc(roomId);                      // 房间级 Y.Doc
  doc.on('update', (u) => socket.to(roomId).emit('update', u));   // 广播增量
  socket.on('update', (u) => Y.applyUpdate(doc, u));   // 合并（乱序安全）
});
// 持久化（防抖）
debounce(() => Y.encodeStateAsUpdate(doc), 3000);      // 快照落库
```
