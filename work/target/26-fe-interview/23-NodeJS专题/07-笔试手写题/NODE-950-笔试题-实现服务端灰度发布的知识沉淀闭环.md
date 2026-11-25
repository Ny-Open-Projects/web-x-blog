---
title: [NODE-950] 笔试题——实现发布知识沉淀闭环（发布→案例→检查清单）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-950：手写知识闭环

**需求与边界**：
- 需求：知识沉淀（SCN-联想-886/950）——① 发布案例沉淀（SCN-OPS-248）；② 案例→检查清单项（SCN-联想-886 转化）；③ 检查清单的执行（SCN-OPS-229 门禁）；④ 沉淀效果的度量（事故重发率——SCN-联想-886）。
- 边界：① 案例的标签（SCN-OPS-248）；② 清单项的可验证（SCN-OPS-229）；③ 清单的膨胀防御（SCN-联想-886 季度评审）。

**答**：
```javascript
async function knowledgeLoop(release, incidents) {
  for (const inc of incidents) {
    const caseEntry = await publishCase(release, inc);   // 案例（SCN-OPS-248）
    const checklistItem = { item: caseEntry.prevention, verify: caseEntry.verifiedMetric };   // 转化（SCN-联想-886）
    await addToGate(checklistItem);                    // 门禁（SCN-OPS-229）
    audit({ case: caseEntry.id, addedToGate: true });
  }
  quarterlyReview(checklistItems);                     // 膨胀防御（SCN-联想-886）
  const recurrence = sameRootIncidents();              // 重发率（SCN-联想-886）
  if (recurrence.trend !== 'down') alert('沉淀失效——重发率未降');
}
```

**评分点**:
- 案例→清单转化（SCN-联想-886）。
- 门禁执行（SCN-OPS-229）。
- 膨胀防御（SCN-联想-886 季度评审）。
- 重发率度量（SCN-联想-886）。
