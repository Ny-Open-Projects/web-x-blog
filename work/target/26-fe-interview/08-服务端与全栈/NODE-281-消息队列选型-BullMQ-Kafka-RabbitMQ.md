---
title: [NODE-281] 消息队列选型：BullMQ/Kafka/RabbitMQ？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-281：消息队列选型：BullMQ/Kafka/RabbitMQ？
**答**:
- BullMQ（Redis 基座）：任务队列（延迟任务/重试/优先级/限流）——中小规模异步任务首选，运维零成本（已有 Redis）。
- RabbitMQ：AMQP 路由能力（topic/exchange），多消费者分发/死信队列成熟——企业消息总线。
- Kafka：高吞吐日志流、按分区顺序、消费组回溯——事件溯源/大数据管道；不适合"每个消息精确一个任务"语义。
- 选型口诀：任务编排 BullMQ、业务路由 RabbitMQ、事件流/回溯 Kafka；Node 生态三者都有成熟 client（bullmq/amqplib/kafkajs）。

```javascript
// BullMQ：延迟任务 + 重试
import { Queue, Worker } from 'bullmq';
const emailQueue = new Queue('email', { connection: redis });
await emailQueue.add('send', { to, tpl }, {
  delay: 60000,                                   // 1 分钟后投递
  attempts: 5,
  backoff: { type: 'exponential', delay: 1000 },  // 指数退避重试
  removeOnComplete: 1000, removeOnFail: 5000,     // 保留策略
});
new Worker('email', async (job) => sendEmail(job.data), { connection: redis, concurrency: 10 });
// Kafka：事件流
await producer.send({ topic: 'order-events', messages: [{ key: orderId, value: JSON.stringify(event) }] });
```
