---
title: [NODE-968] 笔试题——实现通知 SLA 看板（通知时效达标率）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-968：手写通知 SLA

**需求与边界**：
- 需求：通知 SLA 看板（SCN-OPS-964/968）——① 通知时效达标率（P0/P1/P2 分级——SCN-OPS-964 分级）；② 趋势与基线（SCN-SLA-708）；③ 违约清单（SCN-OPS-963）；④ 看板的下钻（SCN-SLA-705）。
- 边界：① 达标率的口径（通知延迟——SCN-OPS-964）；② 分级的动态（SCN-OPS-663）；③ 报告（SCN-OPS-728）。

**答**：
```javascript
async function notifySlaBoard(month) {
  const events = await notifyEvents(month);
  const byTier = groupBy(events, e => e.slaTier);      // 分级（SCN-OPS-964）
  const compliance = Object.fromEntries(Object.entries(byTier).map(([tier, list]) =>
    [tier, list.filter(e => e.delay <= SLA_TIERS[tier].maxDelay).length / list.length]));
  const breaches = events.filter(e => e.delay > SLA_TIERS[e.slaTier].maxDelay);
  return { compliance, breaches, trend: vsLastMonth(compliance),   // 趋势（SCN-SLA-708）
    drill: (b) => notifyDetail(b) };                   // 下钻（SCN-SLA-705）
}
```

**评分点**:
- 分级达标率（SCN-OPS-964）。
- 违约清单 + 下钻（SCN-OPS-963/705）。
- 趋势（SCN-SLA-708）。
