---
title: [NODE-998] 笔试题——实现 SLA 体系知识沉淀（案例→检查→规则）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-998：手写 SLA 沉淀

**需求与边界**：
- 需求：SLA 沉淀（SCN-SLA-998/OPS-248）——① SLA 案例（违约/豁免/对齐——SCN-OPS-248）；② 案例→检查项（SCN-联想-886）；③ 案例→规则（SCN-OPS-315）；④ 沉淀的度量（SCN-联想-886）。
- 边界：① 案例的标签（SCN-OPS-248）；② 检查项的门禁（SCN-OPS-229）；③ 规则的降级（SCN-OPS-315）。

**答**：
```javascript
async function slaKnowledgeLoop(breaches) {
  for (const b of breaches) {
    const caseEntry = await slaCase(b);                // 案例（SCN-OPS-248）
    await addToGate({ item: caseEntry.prevention, verify: caseEntry.metric });   // 检查项（SCN-联想-886）
    await addAuditRule({ from: caseEntry.rootCause });   // 规则（SCN-OPS-315）
    audit({ case: caseEntry.id });
  }
  const recurrence = slaBreachTrend();                 // 度量（SCN-联想-886）
  if (recurrence !== 'down') alert('SLA 沉淀失效——违约趋势未降');
}
```

**评分点**:
- 案例→检查项→规则三转化（SCN-OPS-248/联想-886/315）。
- 门禁 + 规则降级（SCN-OPS-229/315）。
- 重发率度量（SCN-联想-886）。
