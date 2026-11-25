---
title: [NODE-987] 笔试题——实现 SLA 与错误预算对齐（内部 SLO 支撑外部 SLA）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-987：手写 SLO-SLA 对齐

**需求与边界**：
- 需求：SLO-SLA 对齐（SCN-SLA-703/987）——① SLO 严于 SLA（内部目标比外部承诺严——缓冲，SCN-SLA-703）；② SLO 预算监控（SCN-SLA-737）；③ 预算烧完的处置（SCN-OPS-944）；④ 对齐的巡检（SCN-SLA-975）。
- 边界：① 对齐的校验（SLO ≥ SLA——SCN-SLA-703）；② 预算与 SLA 违约的关联（SCN-SLA-963）；③ 对齐的报告（SCN-OPS-728）。

**答**：
```javascript
async function sloSlaAlignment() {
  for (const sla of allSlas()) {
    const slo = internalSlo(sla.metric);
    if (slo.target > sla.slo.target || slo.compliance <= sla.compliance)
      alert({ type: 'SLO_NOT_STRICTER', metric: sla.metric,
        fix: `SLO 需严于 SLA（SCN-SLA-703）——调 SLO 或 SLA` });   // 对齐校验
    const budget = errorBudget(slo, 30);               // 预算（SCN-SLA-737）
    if (budget.remaining <= 0)
      await breachNotify({ consumer: sla.consumer, metric: sla.metric });   // 预算烧穿 → SLA 违约预警（SCN-SLA-963）
  }
}
```

**评分点**:
- SLO 严于 SLA 校验（SCN-SLA-703）。
- 预算烧穿 → 违约预警（SCN-SLA-737/963）。
- 巡检（SCN-SLA-975）。
