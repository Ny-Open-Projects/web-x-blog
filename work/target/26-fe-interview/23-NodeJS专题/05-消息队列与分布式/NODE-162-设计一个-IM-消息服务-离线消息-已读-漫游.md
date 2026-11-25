---
title: [NODE-162] 设计一个 IM 消息服务（离线消息/已读/漫游）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-162：设计一个 IM 消息服务（离线消息/已读/漫游）？
**答**：
- 可靠性三件套：**seq 序列号**（会话内单调递增，客户端按 seq 判缺）、**ACK 确认**（发送方 ACK 存 lastAckSeq）、**离线兜底**（投递超时未 ACK 落 offline 表，上线按 seq 补拉）。
- 消息去重：客户端生成 clientMsgId，服务端去重表拦截重发；服务端分配 seq 后才可投递。
- 漫游：消息按会话存 7 天 + 用户级同步 seq，换设备拉全量历史；已读回执只更新 lastReadSeq，不重发消息体。
- 架构：接入网关（WS 长连接，sticky，NODE-141）→ 投递队列 → 对端网关；跨机房按用户路由。

```mermaid
sequenceDiagram
    participant A as 发送方
    participant S as 接入网关
    participant Q as 投递队列
    participant B as 接收方网关
    A->>S: 发送消息 携带 clientMsgId
    S->>S: clientMsgId 去重
    S->>Q: 写入投递队列
    S-->>A: ACK 返回服务端 seq
    Q->>B: 投递到接收方连接
    B-->>S: 已送达回执
    Note over S: 超时未回执 转离线消息表
    A->>S: 按 seq 拉取漫游与补缺
```

```javascript
io.on('connection', (socket) => {
  const uid = socket.handshake.auth.uid;
  online.set(uid, socket.id);

  socket.on('msg', async ({ clientMsgId, to, body }) => {
    if (await redis.set(`msg:dedup:${clientMsgId}`, 1, 'PX', 86400000, 'NX') === null) return; // 去重
    const convKey = [uid, to].sort().join(':');
    const seq = await redis.incr(`seq:${convKey}`);   // 会话内单调 seq
    const msg = { seq, from: uid, to, body, ts: Date.now() };
    await mq.publish('im.deliver', msg);              // 先落队列，进程崩溃不丢
    socket.emit('msg:ack', { clientMsgId, seq });     // 给发送方确认
  });

  socket.on('msg:ack', ({ seq }) =>                   // 已送达游标
    db.user.update({ where: { id: uid }, data: { lastAckSeq: seq } }));
  socket.on('msg:read', ({ convKey, seq }) =>         // 已读游标
    redis.hset(`read:${uid}`, convKey, seq));
});
// 上线补拉：max(lastAckSeq, lastReadSeq) 之后的 offline 表记录逐条补投
```
