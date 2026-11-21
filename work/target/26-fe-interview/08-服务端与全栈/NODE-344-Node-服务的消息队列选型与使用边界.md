---
title: [NODE-344] Node 服务的消息队列选型与使用边界如何判断？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-344：Node 服务的消息队列选型与使用边界
**答**:
- 什么时候用 MQ：削峰（写流量突刺）、解耦（订单完成 → 积分/通知多个下游）、异步化（耗时任务出请求链路）、广播事件。不该用：请求-响应模式（该用 RPC/HTTP）、需要同步强一致结果的操作。
- 选型速查：Redis Stream（轻量、已有 Redis、要求不高）、BullMQ（Node 任务队列生态、延迟/重试/优先级开箱）、Kafka（高吞吐日志流/事件溯源）、RocketMQ/RabbitMQ（事务消息/路由复杂度）。中小业务 BullMQ + Redis 起步。
- 消息语义设计：at-least-once 为默认假设——消费者必须幂等（唯一键/状态机判断）；需要 exactly-once 的用事务消息或对账兜底（ARC-324）。
- 死信与重试：重试退避（指数 + 上限次数）→ 死信队列 + 告警 + 人工/自动补偿流程；毒消息（永远失败）隔离不阻塞队列。
- 可观测：队列深度/消费延迟（lag）告警、消费成功率、按 topic 分账。
```javascript
// BullMQ 任务定义
const queue = new Queue('report', { connection: redis });
await queue.add('gen', { userId, range }, { attempts: 5, backoff: { type: 'exponential', delay: 2000 },
  removeOnComplete: 1000, jobId: `report:${userId}:${range}` });  // jobId 幂等
new Worker('report', handler, { connection: redis, concurrency: 5 });
queue.on('failed', (job, e) => { if (job.attemptsMade >= 5) moveToDLQ(job); });
```
