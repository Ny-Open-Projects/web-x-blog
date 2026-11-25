---
title: [NODE-963] 笔试题——实现 SLA 违约自动通知（违约→通知→处置）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-963：手写违约通知

**需求与边界**：
- 需求：违约通知（SCN-SLA-703/963）——① 违约检测（SCN-SLA-955 达标跟踪）；② 自动通知（消费方 + 内部——SCN-OPS-612）；③ 处置流程（SLA 条款——SCN-SLA-703）；④ 通知的闭环（确认——SCN-OPS-864）。
- 边界：① 违约的归因（SCN-SLA-716）；② 通知的降噪（SCN-OPS-320）；③ 处置的跟踪（SCN-OPS-227）。

**答**：
```javascript
async function slaBreachNotify(breach) {
  const attribution = await anomalyAttribution(breach);   // 归因（SCN-SLA-716）
  await notify({ to: [breach.consumer.ownerRole, 'oncall-mgr'],   // 双向（SCN-OPS-612）
    payload: { breach, attribution }, ackRequired: true });   // 闭环（SCN-OPS-864）
  await scheduleRemediation(breach);                   // 处置（SCN-SLA-703）
  audit({ breach: breach.id, notified: true });        // 审计
}
```

**评分点**:
- 违约检测 + 双向通知（SCN-SLA-955/OPS-612）。
- 归因（SCN-SLA-716）。
- 处置跟踪（SCN-SLA-703/227）。
