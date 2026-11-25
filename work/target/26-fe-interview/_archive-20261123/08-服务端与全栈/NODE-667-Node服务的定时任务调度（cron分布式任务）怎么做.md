---
title: [NODE-667] 定时任务调度（cron/分布式任务）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-667：定时任务怎么做？
**答**：
- 分布式调度问题：多实例各跑一遍 cron（重复执行）——解法：leader election（选主——只有 leader 跑）或分布式锁（SCN-NODE-652 锁 + 幂等双保险——幂等是锁失效的保险）。
- 任务调度框架：agenda/bullmq repeatable（DB/Redis 驱动——持久化、错过补跑）、原生 cron（node-cron——轻量但无持久化）。
- 可靠性：错过调度补跑（misfire 处理——服务重启期间错过的任务补跑还是跳过——按业务语义声明）、任务幂等（SCN-NODE-655）、任务超时（跑飞的任务杀掉——孤儿任务防御）。
- 优先级与隔离：重任务独立 worker 进程（不占 API 实例资源——SCN-NODE-634 并发模型）。
- 追问钩子：为什么定时任务「幂等」比「分布式锁」更根本——锁可能失效（过期/GC 停顿），双跑仍会发生；幂等任务双跑零副作用（对账任务重跑结果一致）——锁是性能优化（避免重复计算），幂等才是正确性保证——两者都要，但幂等优先级更高。

```javascript
// bullmq repeatable + 分布式锁双保险
const queue = new Queue('jobs', { connection });
await queue.add('daily-report', {}, { repeat: { pattern: '0 2 * * *' } });
worker.on('active', async (job) => {
  const locked = await redis.set(`cron:${job.name}:${job.id}`, 1, 'PX', 300_000, 'NX');
  if (!locked) throw new Error('SkippedDuplicate');    // 双跑跳过（幂等兜底）
});
```
