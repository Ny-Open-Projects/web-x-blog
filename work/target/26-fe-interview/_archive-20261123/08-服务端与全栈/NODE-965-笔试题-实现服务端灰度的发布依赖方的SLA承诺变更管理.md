---
title: [NODE-965] 笔试题——实现 SLA 承诺变更管理（SLA 升降级流程）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-965：手写 SLA 变更

**需求与边界**：
- 需求：SLA 变更（SCN-SLA-710/965）——① SLA 变更流程（提案/评审/生效——SCN-SLA-710 口径变更）；② 变更的影响分析（通知/门禁/看板——SCN-OPS-954 联动）；③ 变更的审计（SCN-OPS-273）；④ 变更的双跑（SCN-SLA-710 双跑验证）。
- 边界：① 变更的审批（SCN-OPS-241）；② 变更的版本化（SCN-SLA-710）；③ 变更的通知（SCN-OPS-245）。

**答**：
```javascript
async function slaChangeFlow(consumer, newSla) {
  await review({ newSla });                            // 评审（SCN-OPS-241）
  await dualRun(consumer, { oldSla, newSla, duration: '14d' });   // 双跑（SCN-SLA-710）
  const impact = slaImpactAnalysis(consumer, newSla);  // 影响分析（SCN-OPS-954）
  await applySla(consumer, newSla);                    // 生效（版本化——SCN-SLA-710）
  await notify({ to: consumer.ownerRole, payload: { newSla, impact } });   // 通知（SCN-OPS-245）
  audit({ consumer, from: oldSla, to: newSla });       // 审计（SCN-OPS-273）
}
```

**评分点**:
- 变更流程（评审/双跑/生效——SCN-SLA-710）。
- 影响分析联动（SCN-OPS-954）。
- 通知 + 审计（SCN-OPS-245/273）。
