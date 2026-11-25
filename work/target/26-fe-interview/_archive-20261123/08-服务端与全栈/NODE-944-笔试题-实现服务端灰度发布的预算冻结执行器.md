---
title: [NODE-944] 笔试题——实现发布预算冻结执行器（错误预算自治理）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-944：手写预算冻结

**需求与边界**：
- 需求：预算冻结（SCN-OPS-944/229）——① 错误预算计算（SCN-SLA-737 燃尽）；② 冻结触发（预算烧完——SCN-OPS-229）；③ 冻结的解除（人工——SCN-OPS-227）；④ 冻结的审计（SCN-OPS-273）。
- 边界：① 冻结的范围（功能发布冻结——SCN-OPS-229 hard gate）；② 豁免通道（SCN-OPS-229）；③ 预算的月度重置（SCN-SLA-737）。

**答**：
```javascript
async function budgetFreeze(release) {
  const budget = errorBudget(release.slo, 30);         // SCN-SLA-737 燃尽
  if (budget.remaining <= 0) {
    await freezeFeatureReleases(release.app);          // 冻结（SCN-OPS-229 hard）
    audit({ action: 'BUDGET_FREEZE', app: release.app, burnRate: budget.burnRate });   // 审计
    return { frozen: true, resumeCondition: '人工确认（SCN-OPS-227）+ 预算重置（月度）' };
  }
  return { frozen: false, remaining: budget.remaining };
}
```

**评分点**:
- 预算燃尽复用（SCN-SLA-737）。
- 冻结触发 + 豁免（SCN-OPS-229）。
- 人工解除（SCN-OPS-227）。
- 审计（SCN-OPS-273）。
