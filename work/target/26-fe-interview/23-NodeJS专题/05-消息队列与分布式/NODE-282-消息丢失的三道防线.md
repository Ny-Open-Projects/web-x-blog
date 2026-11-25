---
title: [NODE-282] 消息丢失的三道防线？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-282：消息丢失的三道防线？
**答**:
- 生产端：确认机制（Kafka acks=all / RabbitMQ publisher confirm / BullMQ 等待 add resolve）+ 本地消息表（先落库后投递，定时补偿未确认消息）。
- Broker 端：持久化（Kafka replication/刷盘、RabbitMQ durable queue+persistent message）。
- 消费端：手动 ack（处理成功后才 ack，失败重回队列/死信）——at-least-once 语义，配合幂等消费（NODE-283）。
- 三道防线的组合保证 at-least-once；恰好一次需要幂等（业务层唯一键）。

```javascript
// 本地消息表（生产端可靠性）
async function publishWithOutbox(event) {
  await db.outbox.insert({ id: event.id, payload: event, status: 'pending' });   // 先落库
  try {
    await producer.send({ topic: event.type, messages: [{ key: event.id, value: JSON.stringify(event) }] });
    await db.outbox.update(event.id, { status: 'sent' });
  } catch { /* 定时任务扫 pending 超过 1min 的记录补偿投递 */ }
}
// 消费端：手动 ack
await consumer.run({ eachMessage: async ({ message }) => {
  await process(JSON.parse(message.value));
  // 处理成功才 offset 提交（kafkajs 默认 autoCommit false 时手动）
  // 失败：重试队列 → 死信（NODE-286）
}});
```
