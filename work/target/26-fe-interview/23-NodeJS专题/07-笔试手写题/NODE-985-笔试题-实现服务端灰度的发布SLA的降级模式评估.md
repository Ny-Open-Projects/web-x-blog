---
title: [NODE-985] 笔试题——实现 SLA 降级模式评估（降级对 SLA 的影响）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-985：手写降级评估

**需求与边界**：
- 需求：降级评估（SCN-NODE-778/985）——① 降级对 SLA 指标的影响（降级期间的 SLA 判定——降级值是否算违约）；② 降级模式分级（哪些降级豁免 SLA——SCN-OPS-329 声明）；③ 评估的报告（SCN-OPS-985）；④ 评估的审计（SCN-OPS-273）。
- 边界：① 降级的豁免声明（SCN-OPS-329 降级矩阵声明 SLA 豁免）；② 降级期间的指标标记（SCN-NODE-690）；③ 评估的消费（SLA 变更——SCN-SLA-965）。

**答**：
```javascript
async function degradedSlaAssessment(degradation, sla) {
  const exempt = degradationMatrix[degradation.type]?.slaExempt ?? false;   // 豁免声明（SCN-OPS-329）
  const metrics = await metricsDuring(degradation.window);
  const impacted = sla.metrics.filter(m => metrics[m] > m.slo && !exempt);   // 降级期间违约（豁免除外）
  return {
    exempt, impacted,
    verdict: exempt ? 'SLA_EXEMPT（SCN-OPS-329 声明）' : impacted.length ? 'BREACH' : 'OK',
    propose: exempt ? null : slaChangeFlow(sla, { adjust: impacted }),   // SLA 变更（SCN-SLA-965）
  };
}
```

**评分点**:
- 降级豁免声明（SCN-OPS-329）。
- 降级期间指标标记（SCN-NODE-690）。
- SLA 变更提案（SCN-SLA-965）。
