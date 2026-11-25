---
title: [NODE-979] 笔试题——实现回滚决策闭环（决策→执行→验证→善后→学习）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-979：手写回滚闭环

**需求与边界**：
- 需求：回滚闭环（SCN-OPS-234/227/833）——① 决策（SCN-OPS-234 决策树）；② 执行（SCN-NODE-833 自动回滚）；③ 验证（SCN-OPS-930 多维）；④ 善后（SCN-OPS-227 五步）；⑤ 学习（SCN-联想-886 沉淀）。
- 边界：① 闭环的时效（SCN-OPS-215）；② 闭环的审计（SCN-OPS-273）；③ 闭环的演练（SCN-OPS-215）。

**答**：
```javascript
async function rollbackClosedLoop(incident, release) {
  const decision = rollbackDecisionTree(incident, release);   // ① 决策（SCN-OPS-234）
  const exec = decision.action === 'ROLLBACK' ? await autoRollback(release) : await hotfix(release);   // ② 执行（SCN-NODE-833）
  const verify = await multidimRollbackVerify(release);   // ③ 验证（SCN-OPS-930）
  const aftermath = await postRollbackChain(release);  // ④ 善后（SCN-OPS-227）
  const learned = await knowledgeLoop(release, [incident]);   // ⑤ 学习（SCN-联想-886）
  return { decision, exec, verify, aftermath, learned };   // 全链闭环
}
```

**评分点**:
- 五步闭环（决策/执行/验证/善后/学习）全链引用。
- 各步编号引用（SCN-OPS-234/833/930/227/联想-886）。
