---
title: [NODE-993] 笔试题——实现租户违约分级处置（金租户优先处理）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-993：手写违约分级

**需求与边界**：
- 需求：租户违约分级（SCN-SLA-993/891）——① 租户等级 × 违约级别的处置矩阵（金 P0 优先——SCN-OPS-891）；② 处置的时效（金租户即时——SCN-OPS-210）；③ 处置的审计（SCN-OPS-220）；④ 处置的闭环（SCN-OPS-227）。
- 边界：① 分级的时效（SCN-OPS-210）；② 处置的资源（SCN-NODE-678）；③ 处置的闭环（SCN-OPS-227）。

**答**：
```javascript
const HANDLING_MATRIX = {                       // 租户等级 × 违约级别（SCN-OPS-891）
  'gold-P0': { escalate: 'immediate', team: 'gold-team' },
  'bronze-P1': { escalate: 'next-day', team: 'shared' },
};
async function handleTenantBreach(breach) {
  const handling = HANDLING_MATRIX[`${breach.tier}-${breach.level}`] ?? HANDLING_MATRIX['bronze-P0'];
  await escalate(handling.team, { breach, within: handling.escalate });   // 时效（SCN-OPS-210）
  await track(breach);                                 // 闭环（SCN-OPS-227）
  audit({ breach: breach.id, handling });              // 审计（SCN-OPS-220）
}
```

**评分点**:
- 租户等级×违约矩阵（SCN-OPS-891）。
- 分级时效（SCN-OPS-210）。
- 闭环 + 审计（SCN-OPS-227/220）。
