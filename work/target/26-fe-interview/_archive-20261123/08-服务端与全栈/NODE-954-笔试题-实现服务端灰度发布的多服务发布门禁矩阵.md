---
title: [NODE-954] 笔试题——实现多服务发布门禁矩阵（组合+单服务双层）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-954：手写双层门禁

**需求与边界**：
- 需求：双层门禁（SCN-OPS-954/922）——① 单服务门禁（各服务独立——SCN-OPS-859）；② 组合门禁（组合风险——SCN-OPS-935）；③ 双层的判定（单服务全过 + 组合过——SCN-OPS-954）；④ 矩阵的报告（SCN-OPS-261）。
- 边界：① 双层的顺序（单服务→组合——SCN-OPS-954）；② 豁免的双层语义（SCN-OPS-229）；③ 矩阵的消费（发布计划——SCN-OPS-251）。

**答**：
```javascript
async function dualLayerGates(plans) {
  const perService = await Promise.all(plans.map(p => releaseGates(p)));   // 单服务（SCN-OPS-859）
  const serviceFails = perService.filter(r => r.blocked);
  if (serviceFails.length) return { blocked: true, serviceFails };   // 单服务先过
  const combo = comboRiskAssessment(plans);            // 组合风险（SCN-OPS-935）
  if (combo.action === 'SPLIT_BATCHES')
    return { blocked: true, note: '组合高风险——分批（SCN-OPS-202）' };
  return { pass: true, plan: topologicalBatches(plans) };   // 拓扑（SCN-OPS-251）
}
```

**评分点**:
- 单服务→组合双层（SCN-OPS-859/935）。
- 分批处置（SCN-OPS-202）。
- 拓扑输出（SCN-OPS-251）。
