---
title: [NODE-693] 任务队列的优先级与并发控制怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-693：队列优先级怎么做？
**答**：
- 优先级队列：多队列分级（critical/high/low——消费者按优先级拉取）； starvation 防御（低优先级保底配额——高优先级持续时 low 至少 10% 产能）。
- 并发控制：消费者并发上限（下游保护——SCN-NODE-643 池隔离联动）、全局并发配额（跨队列总并发）。
- 任务抢占：高优先级插队（低优先级任务让位——可中断任务才可抢占，SCN-NODE-628 任务抢占）；抢占粒度（任务级非线程级——协作式）。
- 延迟任务：延迟队列（定时执行——MQ 延迟消息/Redis ZSET 轮询）。
- 追问钩子：为什么优先级队列要配「低优先级保底配额」——严格优先级下高优先级持续时 low 饿死（永远轮不到——报表/清理任务无限延迟）；保底配额（每 10 个 high 消费 1 个 low）让低优先级「慢但不死」——优先级的公平性兜底。

```javascript
// bullmq 优先级 + 保底
worker.on('completed', () => {
  if (++highRun % 10 === 0) lowQueueWorker.runOne();    // 每 10 high 跑 1 low（保底）
});
// 延迟队列（ZSET 轮询）
await redis.zadd('delayed', Date.now() + delayMs, taskId);
cron('*/1s', async () => {
  const due = await redis.zrangebyscore('delayed', 0, Date.now());
  due.forEach(dispatch); redis.zrem('delayed', due);
});
```
