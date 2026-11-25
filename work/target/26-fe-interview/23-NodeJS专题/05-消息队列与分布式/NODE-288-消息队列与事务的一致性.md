---
title: [NODE-288] 消息队列与事务的一致性？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-288：消息队列与事务的一致性？
**答**:
- 核心难题：DB 事务与消息投递无法原子（两系统）——本地消息表（Outbox 模式）是标准解（NODE-282 延伸）：同事务写业务数据+outbox，独立进程 relay 投递。
- relay 设计：扫 outbox 未 sent 记录投递 → 标记 sent；幂等投递（消息 id）；失败重试+告警。
- 事务消息（RocketMQ 风格）：半消息 + 本地事务 + 确认/回查——等价于 Outbox 的 MQ 内建版。
- 反模式：事务里直接发 MQ（失败回滚但消息已发）或先发后写（消息先到数据未到）。

```javascript
// Outbox 模式完整实现
async function placeOrder(order) {
  await db.transaction(async (tx) => {
    await tx.orders.insert(order);                          // 业务数据
    await tx.outbox.insert({ id: event.id, type: 'order.created', payload: order, status: 'pending' });  // 同事务
  });                                                       // 原子：要么都成功
}
// relay 进程（独立实例）
setInterval(async () => {
  const pending = await db.outbox.where({ status: 'pending' }).orderBy('created_at').limit(100);
  for (const e of pending) {
    await producer.send({ topic: e.type, messages: [{ key: e.id, value: JSON.stringify(e.payload) }] });
    await db.outbox.update(e.id, { status: 'sent', sent_at: new Date() });
  }
}, 1000);   // at-least-once：消费端幂等（NODE-283）
```
