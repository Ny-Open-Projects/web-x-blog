---
title: [NODE-1030] 笔试题——实现多服务预算联动（跨服务错误预算）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1030：手写预算联动

**需求与边界**：
- 需求：预算联动（SCN-SLA-737/1030）——① 跨服务预算传播（下游预算 × 上游预算——SCN-SLA-1004 数学）；② 联动冻结（下游预算烧穿 → 上游冻结，SCN-OPS-944）；③ 联动的审计（SCN-OPS-273）；④ 联动的巡检（SCN-SLA-975）。
- 边界：① 传播的数学（SCN-SLA-1004）；② 冻结的联动（SCN-OPS-944）；③ 巡检（SCN-SLA-975）。

**答**：
```javascript
async function crossServiceBudget(depsGraph) {
  for (const [svc, deps] of Object.entries(depsGraph)) {
    const budget = deps.reduce((b, d) => b * errorBudget(d).remaining, 1);   // 预算传播（SCN-SLA-1004）
    if (budget <= 0) {
      await freezeFeatureReleases(svc);                // 联动冻结（SCN-OPS-944）
      alert({ type: 'CROSS_SERVICE_BUDGET', svc, deps: deps.map(d => d) });
      audit({ svc, budget: 'exhausted' });             // 审计（SCN-OPS-273）
    }
  }
}
```

**评分点**:
- 跨服务预算传播（SCN-SLA-1004 数学）。
- 联动冻结（SCN-OPS-944）。
- 巡检 + 审计（SCN-SLA-975/OPS-273）。
