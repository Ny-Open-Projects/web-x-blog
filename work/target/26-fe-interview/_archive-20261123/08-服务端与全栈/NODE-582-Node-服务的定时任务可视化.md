---
title: [NODE-582] Node 服务的定时任务治理（可视化/依赖/误触发防护）如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-582：定时任务治理
**答**:
- 治理痛点：几十个 cron 散落各服务——谁在跑/跑了多久/失败没失败无人知（NODE-345 起步后的平台化）。
- 任务注册表：每个定时任务登记（名称/周期/owner/依赖/超时/重试策略——注册制 CI 校验代码 cron 与登记一致）、可视化面板（执行时间线/耗时趋势/结果状态——异常任务醒目）。
- 误触发防护：变更影响评估（改 cron 时间/频率的影响面提示——依赖它的下游）、重复触发防护（锁+fencing NODE-475）、手工触发入口（带参数 dry-run——先试跑再真跑）。
- 依赖编排：任务间依赖（DAG：A 完成才跑 B——链式任务）、数据就绪检查（依赖的数据到位才执行——前置检查）。
- 治理节奏：任务清单季度审计（僵尸任务下线/周期合理性）、失败任务根因分类（Top 失败原因改进）。
```javascript
// 任务注册（CI 校验一致性）
registerCron({
  name: 'nightly-settle', cron: '0 3 * * *', owner: 'trade-team',
  timeout: 30 * 60e3, retries: 2, fencing: true,                 // 高危任务
  deps: ['ledger.snapshot.ready'],                               // 数据就绪前置
  dryRun: true                                                   // 支持试跑
});
```
