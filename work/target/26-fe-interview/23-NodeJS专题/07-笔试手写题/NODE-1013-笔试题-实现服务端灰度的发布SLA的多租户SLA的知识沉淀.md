---
title: [NODE-1013] 笔试题——实现租户 SLA 知识沉淀（租户违约→检查→规则）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1013：手写租户沉淀

**需求与边界**：
- 需求：租户沉淀（SCN-SLA-998/1013）——① 租户违约案例（SCN-OPS-248）；② 案例→租户分层检查项（SCN-SLA-992）；③ 案例→审计规则（SCN-OPS-315）；④ 沉淀度量（SCN-联想-886）。
- 边界：① 分层的案例标签（SCN-SLA-992）；② 检查项的门禁（SCN-OPS-229）；③ 度量（SCN-联想-886）。

**答**：
```javascript
async function tenantKnowledgeLoop(breaches) {
  for (const b of breaches) {
    const entry = await tenantSlaCase(b);              // 案例（SCN-OPS-248）
    await addToTierGate({ tier: b.tier, item: entry.prevention });   // 分层检查项（SCN-SLA-992）
    await addAuditRule({ from: entry.rootCause, scope: `tier:${b.tier}` });   // 规则（SCN-OPS-315）
    audit({ case: entry.id });                         // 审计
  }
  if (tenantBreachTrend() !== 'down') alert('租户沉淀失效');   // 度量（SCN-联想-886）
}
```

**评分点**:
- 分层案例→检查项→规则（SCN-SLA-992/OPS-315）。
- 门禁 + 度量（SCN-OPS-229/联想-886）。
