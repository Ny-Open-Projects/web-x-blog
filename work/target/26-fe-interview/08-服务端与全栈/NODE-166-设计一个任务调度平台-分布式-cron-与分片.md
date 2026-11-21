---
title: [NODE-166] 设计一个任务调度平台（分布式 cron 与分片）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-166：设计一个任务调度平台（分布式 cron 与分片）？
**答**：
- 核心问题：多实例下同一 tick 重复执行 → **tick 锁**（Redis SET NX，TTL 覆盖执行窗口）+ 任务 jobId 唯一（BullMQ 天然去重）。
- 分片并行：任务按 `shard = id % total` 拆分，每实例领自己的区间，横向扩容提速。
- 编排：依赖任务用 DAG（上游成功才解锁下游）；错过 tick（实例重启）要补跑策略（跳过/立即补/按最新一次）。
- 可观测：每分片任务上报进度耗时，连续 N 次 tick 错过告警；任务幂等是底线（重试必然发生）。

```javascript
const cron = require('node-cron');
const INSTANCE = process.env.INSTANCE_ID;

cron.schedule('*/5 * * * *', async () => {
  const tick = new Date().toISOString().slice(0, 16);       // 分钟级 tick 标识
  const got = await redis.set(`cron:sync:${tick}`, INSTANCE, 'PX', 240_000, 'NX');
  if (!got) return;                                          // 多实例只有一台执行
  const total = await db.user.count();
  const SHARDS = 8;
  await Promise.all(Array.from({ length: SHARDS }, (_, s) =>
    taskQueue.add('sync', { shard: s, total },
      { jobId: `sync:${tick}:${s}`,                          // jobId 唯一 → 天然防重复入队
        attempts: 3, backoff: { type: 'fixed', delay: 2000 } })));
});

new Worker('sync', async (job) => {
  const { shard, total } = job.data;
  await db.user.findMany({ where: { id: { mod: { total, remainder: shard } } } })
    .then(syncBatch);                                        // 每实例领自己的分片
}, { concurrency: 4 });
```
