---
title: [NODE-287] 延迟任务与定时任务实现？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-287：延迟任务与定时任务实现？
**答**:
- 延迟任务三方案：BullMQ delay（Redis zset 时间轮思想，支持任意延迟）、DB 轮询（status+due_time 扫描，可靠但秒级精度）、时间轮算法（大量高频延迟任务）。
- 定时任务：node-cron 单机（cluster 下多实例重复触发——加分布式锁或单实例跑）、BullMQ repeatable（jobId 幂等，多实例安全）、外部调度器（K8s CronJob/XXL-Job）。
- 可靠性：任务执行幂等 + 错过补偿（重启后补跑漏掉的 tick）。
- 大规模场景：分层时间轮（月/日/时/分/秒）+ DB 持久化兜底。

```javascript
// BullMQ repeatable + 分布式安全
const queue = new Queue('reports');
await queue.add('daily-report', {}, {
  repeat: { pattern: '0 2 * * *' },        // cron：每天 02:00（BullMQ 多实例幂等：同 jobId 去重）
  jobId: 'daily-report',                    // 显式 jobId：重复添加不会叠加
});
// Worker 幂等：报告生成按日期唯一
async function handler(job) {
  const date = new Date().toISOString().slice(0, 10);
  if (await reportRepo.exists(date)) return;   // 幂等
  await generate(date);
}
// DB 轮询兜底方案（可靠优先时）
setInterval(async () => {
  const due = await db.query('UPDATE task SET status="running" WHERE due_time <= NOW() AND status="pending" LIMIT 100 RETURNING *');
  due.forEach(run);                            // 行锁抢占，多实例安全
}, 5000);
```
