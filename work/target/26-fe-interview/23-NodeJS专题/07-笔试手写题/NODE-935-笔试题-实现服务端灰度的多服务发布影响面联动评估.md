---
title: [NODE-935] 笔试题——实现多服务发布影响面联动评估（组合风险）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-935：手写组合风险

**需求与边界**：
- 需求：组合风险评估（SCN-OPS-202/935）——① 组合变更风险评估（多服务同时发布——组合爆炸防御，SCN-OPS-258）；② 风险矩阵（服务组合 × 依赖——SCN-NODE-915）；③ 分级处置（高风险组合 → 分批——SCN-OPS-202）；④ 评估进评审（SCN-OPS-261）。
- 边界：① 组合的枚举限制（同时发布 ≤2 服务——SCN-OPS-258）；② 风险因子显式（SCN-OPS-202）；③ 评估的自动化（SCN-OPS-261 材料前置）。

**答**：
```javascript
function comboRiskAssessment(plans) {
  if (plans.length > 2) return { blocked: '并发发布 >2——组合爆炸防御（SCN-OPS-258）' };
  const combos = cartesian(plans.map(p => p.services));   // 组合（SCN-NODE-915 矩阵）
  const risks = combos.map(c => ({
    combo: c, riskScore: sum(c.map(s => s.riskScore)) * crossFactor(c),   // 组合风险（SCN-OPS-202）
  }));
  return {
    risks: risks.sort((a, b) => b.riskScore - a.riskScore),
    action: risks.some(r => r.riskScore > THRESHOLD) ? 'SPLIT_BATCHES' : 'PROCEED',   // 分批（SCN-OPS-202）
    material: forReviewBoard(risks),                   // 评审（SCN-OPS-261）
  };
}
```

**评分点**:
- 组合爆炸防御（≤2 服务——SCN-OPS-258）。
- 组合风险矩阵（SCN-NODE-915）。
- 分批处置（SCN-OPS-202）。
- 评审材料（SCN-OPS-261）。
