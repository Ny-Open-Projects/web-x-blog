---
title: [NODE-1015] 笔试题——实现 SLA 体系演练计划生成（SLA 演练排期）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1015：手写演练计划

**需求与边界**：
- 需求：SLA 演练计划（SCN-OPS-279/1015）——① SLA 演练场景（违约→通知→处置闭环——SCN-SLA-974）；② 演练排期（债务排序——SCN-OPS-279）；③ 演练执行（SCN-OPS-215）；④ 报告聚合（SCN-OPS-942）。
- 边界：① 场景的来源（SLA 违约案例——SCN-OPS-248）；② 盲演（SCN-OPS-215）；③ 覆盖度（SCN-OPS-279）。

**答**：
```javascript
async function slaDrillPlan() {
  const scenarios = slaBreachCases().map(c => ({       // 案例来源（SCN-OPS-248）
    name: `sla-drill-${c.id}`, inject: { breach: c.pattern },
    assert: { notified: '<5min', tracked: true } }));   // SCN-SLA-974 闭环
  const schedule = debtToSchedule(scenarios, { blind: true });   // 债务排序 + 盲演（SCN-OPS-279/215）
  const coverage = slaDrillCoverage(schedule);         // 覆盖度（SCN-OPS-279）
  return { schedule, coverage };
}
```

**评分点**:
- 违约案例 → 演练场景（SCN-OPS-248/974）。
- 债务排序 + 盲演（SCN-OPS-279/215）。
- 覆盖度（SCN-OPS-279）。
