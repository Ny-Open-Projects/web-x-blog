---
title: [ENG-270] CI 资源的容量规划（Runner 规模/排队治理）怎么做的？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-270：CI 容量规划怎么做的？
**答**：
- 容量模型：并发需求 = PR 速率 × 平均并发流水线 + 发布/定时任务峰值；Runner 规模按 P99 排队时长目标反推（排队 < 2min）。
- 弹性策略：常驻 Runner 保底 + 云上弹性 Runner 峰值扩容；spot 实例省钱但要有重试（被回收）。
- 排队治理：排队 P95 超标时先查「浪费型任务」（无变更全量跑/重复触发），再扩容——扩容是最后手段。
- 成本可见：CI 费用按团队分账（构建时长 × 机器单价），让「无变更全量构建」这类浪费显形。
- 追问钩子：为什么排队超标先查浪费再扩容——排队问题常被「加机器」掩盖真因（某团队 CI 配置全量跑）；浪费治理通常零成本解决 30%+ 排队，扩容的钱留到治理后仍不够时再花。

```javascript
const capacity = {
  model: (prRate, avgPipelineMin) => prRate * avgPipelineMin / 60,  // 并发需求
  target: { queueP95: '2min' },
  elastic: { baseline: 20, burst: 'cloud-spot', retryOnSpotKill: true },
  audit: (team) => wasteTasks(team),   // 无变更全量/重复触发 → 治理优先于扩容
  cost: chargebackByTeam(),
};
```
