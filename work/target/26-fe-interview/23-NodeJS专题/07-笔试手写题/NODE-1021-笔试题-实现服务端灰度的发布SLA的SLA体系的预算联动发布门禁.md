---
title: [NODE-1021] 笔试题——实现 SLA 预算联动发布门禁（预算 → 发布）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1021：手写预算联动

**需求与边界**：
- 需求：预算联动（SCN-OPS-944/1021）——① 预算检查（SCN-OPS-944）；② 联动门禁（SCN-OPS-229）；③ 联动的豁免（SCN-OPS-229）；④ 联动的审计（SCN-OPS-273）。
- 边界：① 预算的燃尽（SCN-SLA-737）；② 豁免（SCN-OPS-229）；③ 审计（SCN-OPS-273）。

**答**：
```javascript
async function budgetGate(release) {
  const budget = errorBudget(release.slo, 30);         // SCN-SLA-737
  if (budget.remaining <= 0) {
    const waived = release.waiver?.valid;              // 豁免（SCN-OPS-229）
    audit({ release: release.id, budget: 'exhausted', waived });   // 审计（SCN-OPS-273）
    return waived ? { allowed: true, waived } : { blocked: 'BUDGET_EXHAUSTED' };
  }
  return { allowed: true };
}
```

**评分点**:
- 预算检查（SCN-SLA-737）。
- 豁免 + 审计（SCN-OPS-229/273）。
