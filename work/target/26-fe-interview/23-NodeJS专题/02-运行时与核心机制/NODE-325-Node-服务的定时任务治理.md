---
title: [NODE-325] Node 服务的定时任务治理？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-325：Node 服务的定时任务治理？
**答**:
- 治理问题：多实例重复执行、任务漂移（机器时钟）、长任务阻塞后续 tick、任务雪崩（整点集中）。
- 方案：分布式锁（Redis SETNX + 心跳续期）或 BullMQ repeatable（jobId 幂等）；任务注册表（name/cron/owner/超时/幂等键）平台化管理。
- 错峰：整点任务加随机抖动（0~60s）；重任务切分片（按 id range 并行）。
- 可观测：任务执行历史（开始/结束/耗时/结果）——失败任务告警+手动重跑入口。

```javascript
// 分布式锁定时任务
async function runCron(name, fn) {
  const lock = await redis.set(`cron:${name}:${dayKey()}`, instanceId, { nx: true, px: 10 * 60000 });
  if (!lock) return;                                 // 其他实例已抢到
  const hb = setInterval(() => redis.expire(`cron:${name}:${dayKey()}`, 600000), 60000);   // 心跳续期
  try {
    const started = Date.now();
    await fn();
    taskHistory.record(name, { ms: Date.now() - started, ok: true });
  } catch (e) { taskHistory.record(name, { ok: false, err: String(e) }); alert(name); }
  finally { clearInterval(hb); }
}
// 整点错峰：schedule('0 * * * *') → 每实例 + Math.random()*60s 抖动
```
