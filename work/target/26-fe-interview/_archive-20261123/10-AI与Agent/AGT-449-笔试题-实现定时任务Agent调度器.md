---
title: [AGT-449] 笔试题——实现定时 Agent 调度器（cron+价值过滤+幂等去重+补跑）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-449：手写主动式 Agent 调度：定时触发、无变化不打扰、幂等防重、错峰补跑

**需求与边界**：
- 输入：注册的任务（cron/事件触发、检查函数、深度函数、通知渠道）；输出：调度执行框架。
- 边界要求：① 触发后先便宜检查，无新信息不深度执行不通知；② 通知幂等键（同事件不重复推）；③ 错过的执行按策略补跑（只补最后一次）；④ 全局并发上限（多任务同时触发不压垮）。

**答**：
```javascript
class SchedulerAgent {
  constructor({ maxConcurrent = 3 }) {
    this.jobs = []; this.running = 0; this.queue = [];
  }
  register({ id, cron, check, deep, notify, catchUp = 'last' }) {
    this.jobs.push({ id, cron, check, deep, notify, catchUp });
  }
  async fire(job, trigger) {
    if (this.running >= this.maxConcurrent)
      return this.queue.push({ job, trigger });   // 全局并发上限
    this.running++;
    try {
      // 1. 幂等：同 job 同周期只执行一次
      const key = `${job.id}:${periodKey(trigger)}`;
      if (!await lock.try(key)) return;
      // 2. 便宜检查：无新信息不打扰
      const fresh = await job.check(trigger);
      if (!fresh.changed) return;
      // 3. 深度执行（预算内）
      const report = await job.deep(fresh, {
        budget: { maxCost: TASK_CAP } });
      // 4. 通知（幂等键防重推）
      await job.notify(report, { dedupeKey: key });
    } finally {
      this.running--;
      const next = this.queue.shift();
      if (next) this.fire(next.job, next.trigger);
    }
  }
  onMissed(job, lastFire, now) {                  // 错过补跑
    const missed = periodsBetween(lastFire, now, job.cron);
    if (job.catchUp === 'last' && missed.length)
      return this.fire(job, missed.at(-1));       // 只补最后一次
    return null;                                  // 或忽略
  }
}
// 触发类型：cron 定时 / event 事件（price<X）/ state 状态（连续异常升级）。
```

**评分点**:
- "便宜检查→深度执行"两级架构（无变化不打扰是主动 Agent 的核心纪律）。
- 周期幂等锁 + 通知 dedupeKey 双重防重。
- 并发上限与排队（多任务不压垮）。
- 补跑策略可配（last 语义合理：过期报告无价值）。
