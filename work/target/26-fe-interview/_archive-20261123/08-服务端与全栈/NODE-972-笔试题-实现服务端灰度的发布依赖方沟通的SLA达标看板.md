---
title: [NODE-972] 笔试题——实现沟通 SLA 达标看板（分级达标率）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-972：手写沟通看板

**需求与边界**：
- 需求：沟通看板（SCN-OPS-968/972）——① 分级达标率（SCN-OPS-964）；② 消费方维度（各消费方达标——SCN-OPS-891）；③ 趋势与违约（SCN-OPS-963）；④ 下钻（SCN-SLA-705）。
- 边界：① 达标率口径（SCN-OPS-964）；② 消费方的 ack 率（SCN-OPS-864）；③ 报告（SCN-OPS-728）。

**答**：
```javascript
async function commSlaBoard(month) {
  const byTier = await slaByTier(month);               // 分级达标（SCN-OPS-964）
  const byConsumer = await slaByConsumer(month);       // 消费方维度（SCN-OPS-891）
  const ackRate = await ackRateByConsumer(month);      // ack 率（SCN-OPS-864）
  return { byTier, byConsumer, ackRate,
    breaches: breaches(month), trend: vsLastMonth(byTier),   // 违约（SCN-OPS-963）
    drill: (c) => commDetail(c) };                     // 下钻（SCN-SLA-705）
}
```

**评分点**:
- 分级达标 + ack 率（SCN-OPS-964/864）。
- 违约清单（SCN-OPS-963）。
- 下钻（SCN-SLA-705）。
