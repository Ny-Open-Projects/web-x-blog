---
title: [NODE-437] Node 服务的对账调度（批量任务编排）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-437：对账调度与批量任务编排
**答**:
- 对账是批量任务链：数据准备（双方流水切片，注意切片边界与时区 ARC-481）→ 比对 → 差异处理 → 报告。编排器管理依赖顺序（准备完成才比对）、重跑幂等（同一天重跑不重复补偿 ARC-382）、失败断点续跑（第 3 步失败只重跑第 3 步）。
- 任务依赖编排：DAG 声明（prepare → diff → compensate → report），各步独立幂等任务（状态表记录每步完成状态）；调度器支持手动重跑指定步。
- 数据切片策略：按日切片（T+1），大表切片再分片（并行处理 + 单片失败重试）；切片边界用左闭右开防重复遗漏（跨边界记录用 ID 或时间戳锚定）。
- 慢查询防护：对账大查询走只读副本 + 限流（对账不能拖垮在线 DB NODE-385）；窗口错峰（凌晨执行，避开业务高峰）。
- 观测：每步耗时/差异率趋势（差异率突增 → 新 bug 信号）、对账延迟（T+1 什么时候完成）。
```javascript
const reconcileDag = dag({
  prepare: () => sliceFlows(day),
  diff: { depends: 'prepare', run: () => compare(day) },
  compensate: { depends: 'diff', run: r => autoFix(r.diff), guard: r => r.diffRate < 0.05 }, // 大差异人工
  report: { depends: 'compensate', run: () => pushReport(day) }
});
// 状态表：{ day, step, status, startedAt } → 断点续跑：重跑时跳过 done 步
```
