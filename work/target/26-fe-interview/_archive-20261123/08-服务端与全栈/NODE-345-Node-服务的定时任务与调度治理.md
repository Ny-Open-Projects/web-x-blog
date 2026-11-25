---
title: [NODE-345] Node 服务的定时任务与调度治理（多实例防重复）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-345：Node 服务的定时任务与调度治理
**答**:
- 多实例问题：PM2 cluster/K8s 多副本下每个实例都会跑 cron → 重复执行。方案：分布式锁（Redis SET NX 抢占执行权）、专职调度实例（K8s CronJob 单副本）、调度平台（xxl-job 类，控制台可管）。
- 任务可靠性：任务幂等（抢锁也挡不住上轮未结束的重入——状态检查 + 版本）、超时保护（任务卡死自动标记失败）、错过触发补偿（misfire 策略：补跑一次或跳过记录）。
- 分类治理：轻任务进程内 node-cron + 锁；重任务进 MQ（cron 只负责投递，worker 池消费，ARC-344）；互斥任务串行化（锁粒度到任务名）。
- 可观测：每次执行记录（开始/结束/耗时/结果/影响行数），失败告警；任务列表平台化管理（启用/停用/改周期免发版）。
- 测试：任务逻辑抽纯函数（给定输入状态 → 断言输出），cron 只测触发。
```javascript
// 分布式锁 cron
nodeCron.schedule('0 3 * * *', async () => {
  const lock = await redis.set('lock:job:nightly-settle', runId, 'PX', 10 * 60e3, 'NX');
  if (!lock) return;                                            // 其他实例已执行
  try { await runSettle(); await logRun('done'); }
  catch (e) { await logRun('failed', e); alert('nightly-settle 失败'); }
});
```
