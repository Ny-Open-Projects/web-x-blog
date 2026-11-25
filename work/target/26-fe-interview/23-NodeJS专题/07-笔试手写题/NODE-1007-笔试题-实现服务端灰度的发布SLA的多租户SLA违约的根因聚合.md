---
title: [NODE-1007] 笔试题——实现租户违约根因聚合（跨租户模式识别）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1007：手写根因聚合

**需求与边界**：
- 需求：跨租户违约聚合（SCN-SLA-993/1007）——① 跨租户违约聚合（多租户同时违约——系统性问题信号，SCN-SLA-993）；② 根因聚合（SCN-OPS-716）；③ 系统性问题的处置（SCN-OPS-227）；④ 聚合的告警（SCN-OPS-276）。
- 边界：① 聚合的阈值（多租户同时违约——SCN-SLA-1000 公平性）；② 根因的分类（SCN-OPS-716）；③ 聚合的消费（SCN-OPS-227）。

**答**：
```javascript
async function crossTenantBreachAggregation(breaches) {
  if (breaches.length >= 3 && sameTimeWindow(breaches)) {   // 多租户同时（SCN-SLA-1000）
    const causes = classifyDrift(breaches.map(b => b.drift));   // 根因聚合（SCN-OPS-716）
    alert({ type: 'SYSTEMIC_BREACH', tenants: breaches.length, causes,
      note: '多租户同时违约——系统性问题（SCN-OPS-276）' });   // 告警
    return { systemic: true, causes, action: improvementsFor(causes) };   // 处置（SCN-OPS-227）
  }
  return breaches.map(individualHandle);               // 个体处置（SCN-SLA-993）
}
```

**评分点**:
- 多租户同时违约聚合（SCN-SLA-1000/993）。
- 根因聚合 + 系统性告警（SCN-OPS-716/276）。
- 处置分流（SCN-OPS-227）。
