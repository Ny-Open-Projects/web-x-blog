---
title: [NODE-1001] 笔试题——实现 SLA 与发布联动决策审计（SLA 约束的发布决策）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1001：手写 SLA 发布联动

**需求与边界**：
- 需求：SLA 与发布联动（SCN-SLA-991/1001）——① SLA 约束的发布决策（预算烧穿禁止发布——SCN-OPS-944）；② 联动决策的审计（SCN-OPS-273）；③ 联动的闭环（SCN-OPS-227）；④ 联动的演练（SCN-OPS-269）。
- 边界：① 联动的触发（SCN-OPS-944）；② 联动的豁免（SCN-OPS-229）；③ 联动的消费（SCN-OPS-248）。

**答**：
```javascript
async function slaConstrainedRelease(release) {
  const budget = errorBudget(release.slo, 30);         // SCN-SLA-737
  const slaGate = await slaGates(release);             // SCN-SLA-991
  if (budget.remaining <= 0 || slaGate.fails.length) {
    audit({ release: release.id, blockedBy: 'SLA' });  // 审计（SCN-OPS-273）
    return { blocked: 'SLA_BUDGET_EXHAUSTED',
      action: '修复后重试或申请豁免（SCN-OPS-229）' };   // 联动决策
  }
  return { allowed: true };
}
```

**评分点**:
- SLA 约束发布决策（SCN-SLA-991/944）。
- 豁免 + 审计（SCN-OPS-229/273）。
- 闭环（SCN-OPS-227）。
