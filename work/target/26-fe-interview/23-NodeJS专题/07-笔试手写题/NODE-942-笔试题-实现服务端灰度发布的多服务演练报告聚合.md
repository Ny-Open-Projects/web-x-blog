---
title: [NODE-942] 笔试题——实现多服务演练报告聚合（覆盖度全景）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-942：手写演练聚合

**需求与边界**：
- 需求：演练聚合（SCN-OPS-279/931）——① 多服务演练报告聚合（SCN-OPS-931）；② 覆盖度全景（服务×故障模式矩阵——SCN-OPS-279）；③ 债务清单（SCN-OPS-279）；④ 聚合的告警（覆盖度下降——SCN-OPS-279）。
- 边界：① 聚合的维度（服务/故障模式/时间——SCN-OPS-279）；② 债务的排序（风险×时间——SCN-联想-327 利息模型）；③ 报告的消费（演练排期——SCN-OPS-279）。

**答**：
```javascript
async function drillCoverageMatrix(services, failureModes, drills) {
  const matrix = {};                                   // 服务×故障模式
  for (const s of services)
    matrix[s] = failureModes.map(m => ({
      mode: m, drilled: drilledRecently(s, m, 30), result: drillResult(s, m),
    }));
  const debt = matrix.flat().filter(c => !c.drilled)   // 债务（SCN-OPS-279）
    .sort((a, b) => b.risk * monthsSince(a) - a.risk * monthsSince(b));   // 利息模型（SCN-联想-327）
  const coverage = drilledCount / totalCells;
  if (coverage < 0.8) alert({ type: 'DRILL_COVERAGE_LOW', coverage });   // 告警
  return { matrix, coverage, debt, schedule: debtToSchedule(debt) };   // 演练排期
}
```

**评分点**:
- 服务×故障模式矩阵（SCN-OPS-279）。
- 债务利息排序（SCN-联想-327）。
- 覆盖度告警（SCN-OPS-279）。
- 演练排期输出。
