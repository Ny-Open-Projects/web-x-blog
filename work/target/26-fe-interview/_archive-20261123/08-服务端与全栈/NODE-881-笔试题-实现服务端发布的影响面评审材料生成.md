---
title: [NODE-881] 笔试题——实现发布影响面评审材料生成（发布版）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-881：手写评审材料

**需求与边界**：
- 需求：发布评审材料（SCN-OPS-261）——① 影响面报告（变更→受影响服务/接口——SCN-OPS-291）；② 历史案例检索（SCN-OPS-329）；③ 回滚预案摘要（SCN-OPS-234）；④ 待决策清单（SCN-OPS-261）。
- 边界：① 材料预生成（SCN-OPS-261 事实前置）；② 页数上限（SCN-OPS-261 摘要化）；③ 决策项提取（未自动化判断点）。

**答**：
```javascript
async function releaseReviewMaterial(plan) {
  const impact = affectedServicesAndApis(plan);        // 影响面（SCN-OPS-291）
  const cases = searchCases(plan.failureModeTags, { top: 3 });   // 案例检索（SCN-OPS-329）
  const rollback = { entry: plan.rollbackEntry, eta: plan.rollbackEta,
    cost: assessRollbackCost(plan) };                  // 回滚摘要（SCN-OPS-234）
  const decisions = plan.openQuestions.filter(q => !q.auto);   // 待决策（SCN-OPS-261）
  const material = compress({ impact, cases, rollback, decisions }, { maxPages: 3 });   // 摘要化
  return material;
}
```

**评分点**:
- 四段材料（影响面/案例/回滚/待决策——SCN-OPS-261）。
- 事实前置（预生成——SCN-OPS-261）。
- 摘要化上限（SCN-OPS-261）。
- 决策项提取（未自动化判断点）。
