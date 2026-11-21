---
title: [NODE-079] 消息推送服务如何选型与实现（SSE vs WebSocket）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-079：消息推送服务如何选型与实现（SSE vs WebSocket）？
**答**：
- 选型：**单向服务器推送选 SSE**（通知、进度、行情——HTTP 语义、自动重连、文本协议、走标准代理）；**双向实时选 WebSocket**（聊天、协同编辑）；App/小程序离线场景再补长连接厂商通道/轮询兜底。
- SSE 实现要点：`content-type: text/event-stream`、`retry:` 指定重连间隔、**事件 id 支持断点续传**（客户端 `Last-Event-ID` 头补发漏掉的消息）、连接注册表 + Redis Pub/Sub 跨实例、心跳注释行（`: ping\n\n`）防代理超时断连。
- 通用架构：消息产生方 → MQ → 推送服务（按 uid 查在线连接）→ SSE/WS 下发；不在线则落库，上线后拉取。

```javascript
// SSE 推送服务：连接管理 + Last-Event-ID 续传 + 跨实例广播
const clients = new Map();   // uid → Set<res>

router.get('/events', async (ctx) => {
  const uid = ctx.state.user.uid;
  const lastEventId = Number(ctx.get('last-event-id') || 0);

  ctx.set({ 'content-type': 'text/event-stream', 'cache-control': 'no-cache',
            connection: 'keep-alive', 'x-accel-buffering': 'no' }); // 关闭 Nginx 缓冲
  ctx.status = 200;
  ctx.flushHeaders();

  // 1. 补发离线期间的消息（按 id 增量）
  const missed = await db.query('SELECT id, type, payload FROM notifications WHERE uid = ? AND id > ?', [uid, lastEventId]);
  for (const n of missed) {
    ctx.res.write(`id: ${n.id}\nevent: ${n.type}\ndata: ${JSON.stringify(n.payload)}\n\n`);
  }

  // 2. 注册连接
  if (!clients.has(uid)) clients.set(uid, new Set());
  clients.get(uid).add(ctx.res);

  // 3. 心跳：15s 一条注释行，防止代理 idle 超时断开
  const heartbeat = setInterval(() => ctx.res.write(': ping\n\n'), 15000);

  // 4. 断开清理
  ctx.req.on('close', () => {
    clearInterval(heartbeat);
    clients.get(uid)?.delete(ctx.res);
  });
});

// 业务侧推送：跨实例经 Redis Pub/Sub
async function notify(uid, type, payload) {
  const id = await db.query('INSERT INTO notifications (uid, type, payload) VALUES (?, ?, ?) RETURNING id',
    [uid, type, JSON.stringify(payload)]).then((r) => r[0].id);
  const online = clients.get(uid);
  if (online?.size) {
    for (const res of online) {
      res.write(`id: ${id}\nevent: ${type}\ndata: ${JSON.stringify(payload)}\n\n`);
    }
  } else {
    await pub.publish(`notify:${uid}`, JSON.stringify({ id, type, payload })); // 用户连在其他实例
    await pushOfflineChannel(uid, { id, type, payload });  // 离线：厂商通道/短信兜底
  }
}
```
