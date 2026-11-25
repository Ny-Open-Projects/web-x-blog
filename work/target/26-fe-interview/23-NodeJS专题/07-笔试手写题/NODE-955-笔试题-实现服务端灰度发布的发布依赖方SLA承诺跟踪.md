---
title: [NODE-955] 笔试题——实现发布 SLA 承诺跟踪（依赖方 SLA 达标）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-955：手写 SLA 跟踪

**需求与边界**：
- 需求：SLA 跟踪（SCN-SLA-703/955）——① 依赖方 SLA 定义（可用性/延迟承诺——SCN-SLA-703）；② 实际达标跟踪（月度达标率——SCN-SLA-740 聚合）；③ 违约的处置（SLA 条款——SCN-SLA-703）；④ SLA 报告（SCN-OPS-728）。
- 边界：① SLA 的双端口径（SCN-OPS-714 快照）；② 违约的归因（SCN-SLA-716 叙事）；③ 报告的分发（SCN-OPS-728）。

**答**：
```javascript
async function slaTracking(consumer, month) {
  const actual = await metrics.monthly(consumer, month);   // 实际达标（SCN-SLA-740）
  const breaches = actual.filter(m => m.compliance < m.slo.compliance);   // 违约
  return {
    compliance: actual.compliance, breaches,
    per: breaches.map(b => ({ metric: b.key, actual: b.compliance, slo: b.slo.compliance })),
    report: await slaReportPdf(consumer, month),       // 报告（SCN-OPS-728 签名快照）
    action: breaches.length ? '按 SLA 条款处置' : null,
  };
}
```

**评分点**:
- SLA 定义与达标跟踪（SCN-SLA-703/740）。
- 违约处置（SCN-SLA-703）。
- 报告签名快照（SCN-OPS-728）。
- 归因叙事（SCN-SLA-716）。
