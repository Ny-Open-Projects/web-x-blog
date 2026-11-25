---
title: [NODE-949] 笔试题——实现决策链与预案联动（决策触发预案执行）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-949：手写预案联动

**需求与边界**：
- 需求：决策与预案联动（SCN-OPS-896/949）——① 决策触发预案（决策树→预案卡片——SCN-OPS-896）；② 预案执行（SCN-OPS-932 卡片）；③ 执行验证（SCN-联想-865）；④ 联动审计（SCN-OPS-273）。
- 边界：① 预案的权限（SCN-OPS-253）；② 联动的去抖（SCN-OPS-276）；③ 联动的演练（SCN-OPS-269）。

**答**：
```javascript
decisionTree.on('decision', async ({ type, context, by }) => {   // 决策树（SCN-联想-896）
  if (recentlyExecuted(type)) return;                  // 去抖（SCN-OPS-276）
  requireRole(by, 'oncall-mgr');                       // 权限（SCN-OPS-253）
  const card =预案卡片(type);                           // 预案卡片（SCN-OPS-932）
  for (const action of card.action) await execute(action, context);
  const verified = await verify(card.verify);          // 验证（SCN-联想-865）
  audit({ decision: type, verified });                 // 审计（SCN-OPS-273）
});
```

**评分点**:
- 决策树→预案卡片联动（SCN-联想-896/932）。
- 权限 + 去抖（SCN-OPS-253/276）。
- 执行验证（SCN-联想-865）。
- 审计（SCN-OPS-273）。
