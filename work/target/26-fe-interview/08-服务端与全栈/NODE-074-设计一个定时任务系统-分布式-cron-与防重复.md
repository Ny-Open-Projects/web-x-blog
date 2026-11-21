---
title: [NODE-074] 设计一个定时任务系统（分布式 cron 与防重复执行）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-074：设计一个定时任务系统（分布式 cron 与防重复执行）？
**答**：
- 多实例部署时 `setInterval`/`node-cron` 会在每个实例都触发——必须**分布式互斥**。三层方案：① **Redis 分布式锁**（`SET NX EX`，NODE-041 的 withLock，简单可靠）；② BullMQ 的 **Repeatable Jobs**（任务入 Redis 队列，worker 抢占消费，天然不重复 + 失败重试 + 延迟队列）；③ 独立调度中心（xxl-job/Quartz 集群）。
- 设计要点：任务幂等（抢不到锁直接跳过，业务侧也用状态机防重）、错过触发（misfire）补跑策略、超时强制释放锁（看门狗续期）、任务执行日志与告警。
- 面试口径：先答"为什么不能裸跑 node-cron"，再给锁方案与队列方案的取舍（轻量用锁，重任务用队列）。

```javascript
const { Queue, Worker } = require('bullmq');
const cronParser = require('cron-parser');

// 方案一：BullMQ Repeatable Job（推荐）
const schedulerQueue = new Queue('scheduler', { connection: redisOpts });

async function registerCron(name, cron, payload) {
  // upsert：按 jobId 幂等注册，重启/多实例不重复
  await schedulerQueue.upsertJobRepeatable(name, { pattern: cron, tz: 'Asia/Shanghai' });
  await schedulerQueue.add(name, payload, { repeat: { pattern: cron }, jobId: name });
}
await registerCron('daily-report', '0 2 * * *', { type: 'report' });
await registerCron('clean-expired', '*/10 * * * *', { type: 'clean' });

new Worker('scheduler', async (job) => {
  // BullMQ 保证同一 repeatable job 同一时刻只有一个 worker 在跑
  console.log(`执行 ${job.name}`, job.data);
  if (job.name === 'daily-report') await sendDailyReport();
  if (job.name === 'clean-expired') await cleanExpiredTokens();
}, { connection: redisOpts, concurrency: 5, lockDuration: 60000 });

// 方案二：Redis 锁互斥（轻量场景，node-cron + 锁）
const cron = require('node-cron');
cron.schedule('0 2 * * *', async () => {
  const lockKey = 'cron:daily-report:' + new Date().toISOString().slice(0, 10); // 每天一个锁
  const token = crypto.randomUUID();
  const ok = await redis.set(lockKey, token, 'EX', 3600, 'NX');   // 拿锁才执行，1h 自动释放
  if (!ok) return console.log('其他实例已在执行，跳过');
  try {
    await sendDailyReport();
  } catch (err) {
    await redis.del(lockKey);   // 失败释放锁，允许重试
    throw err;
  }
});
```
