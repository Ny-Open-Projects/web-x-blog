---
title: [NODE-896] 笔试题——实现大促值守应急决策树执行（预案一键执行）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-896：手写应急决策树

**需求与边界**：
- 需求：应急决策树（SCN-联想-865/OPS-234）——① 故障分类 → 预案映射（SCN-联想-865 矩阵）；② 预案一键执行（值班权限——SCN-OPS-253）；③ 执行验证（预案生效验证——SCN-联想-865）；④ 决策记录（SCN-OPS-273）。
- 边界：① 决策树的分叉条件（故障级别/影响面——SCN-OPS-234）；② 预案执行的审计（谁在何时执行了什么——SCN-OPS-220）；③ 决策树的演练保鲜（SCN-联想-833）。

**答**：
```javascript
const DECISION_TREE = {
  'machine-down': { inject: 'all-to-human', action: throttleUpload },
  'db-slow': { action: ['isolate-slow-pool', 'expand-slow-pool'], verify: 'pool-health' },   // SCN-NODE-862
  'api-error-50': { action: ['degrade-L2', 'pause-ramp'], verify: 'error-rate' },   // SCN-NODE-778
};
async function emergency(decision, oncall) {
  requireRole(oncall, 'oncall-mgr');                   // 权限（SCN-OPS-253）
  const plan = DECISION_TREE[decision.type];
  for (const action of plan.action) await actions[action](decision.context);
  const verified = await verify(plan.verify);          // 生效验证（SCN-联想-865）
  audit({ decision, by: oncall, verified });           // 审计（SCN-OPS-273）
  return { verified };
}
```

**评分点**:
- 故障→预案映射（SCN-联想-865 矩阵）。
- 一键执行 + 权限（SCN-OPS-253）。
- 执行验证（SCN-联想-865）。
- 决策记录（SCN-OPS-273）。
