---
title: [NODE-1010] 笔试题——实现 SLA 与降级矩阵联动校验（降级预案覆盖 SLA）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1010：手写联动校验

**需求与边界**：
- 需求：SLA 与降级矩阵（SCN-SLA-975/OPS-329）——① 降级矩阵覆盖 SLA 指标（SLA 指标有对应降级策略——SCN-OPS-329）；② 降级豁免声明（SCN-OPS-985）；③ 校验的门禁（SCN-OPS-229）；④ 校验的周期（月度——SCN-SLA-975）。
- 边界：① 矩阵的数据源（SCN-OPS-329）；② 豁免的声明（SCN-OPS-985）；③ 门禁（SCN-OPS-229）。

**答**：
```javascript
async function slaDegradeAlignment(sla, degradeMatrix) {
  const uncovered = sla.metrics.filter(m =>
    !degradeMatrix.strategies?.[m] && !slaExempt(m));   // 未覆盖（SCN-OPS-329）
  if (uncovered.length)
    return { gap: uncovered, fix: uncovered.map(m =>
      `为 ${m} 补降级策略（SCN-OPS-329）或声明 SLA 豁免（SCN-OPS-985）`) };
  return { covered: true };
}
```

**评分点**:
- 降级矩阵覆盖校验（SCN-OPS-329）。
- 豁免声明（SCN-OPS-985）。
- 门禁 + 周期（SCN-OPS-229/975）。
