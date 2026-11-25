---
title: [NODE-1004] 笔试题——实现跨服务 SLA 一致性（上游 SLA 支撑下游 SLA）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1004：手写跨服务一致

**需求与边界**：
- 需求：跨服务 SLA（SCN-SLA-1004/915）——① 依赖图 SLA 传播（下游 SLA 需上游 SLA 支撑——SCN-NODE-915 矩阵）；② 一致性校验（下游 SLA > Σ上游 SLA——数学不一致告警）；③ 修复建议（上游升 SLA/下游降——SCN-SLA-965）；④ 巡检（SCN-SLA-975）。
- 边界：① SLA 传播的建模（SCN-NODE-915）；② 校验的数学（误差预算传播——SCN-SLA-703）；③ 巡检的周期（SCN-SLA-975）。

**答**：
```javascript
async function crossServiceSlaCheck(depsGraph) {
  for (const [svc, deps] of Object.entries(depsGraph)) {
    const downstreamSla = slaOf(svc);
    const upstreamBudget = deps.reduce((b, d) => b * slaOf(d).compliance, 1);   // 误差预算传播（SCN-SLA-703）
    if (upstreamBudget < downstreamSla.compliance)
      alert({ type: 'SLA_MATH_INCONSISTENT', svc,
        note: `上游预算 ${upstreamBudget} < 下游承诺 ${downstreamSla.compliance}`,
        fix: '升上游 SLA 或降下游承诺（SCN-SLA-965）' });   // 修复（SCN-SLA-965）
  }
}
```

**评分点**:
- 依赖图 SLA 传播（SCN-NODE-915）。
- 误差预算传播数学（SCN-SLA-703）。
- 修复建议（SCN-SLA-965）。
