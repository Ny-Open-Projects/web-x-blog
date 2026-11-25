---
title: [OPS-224] AB 实验结束的发布协同（实验→全量的落地动作）怎么设计？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## OPS-224：实验结束怎么协同？
**答**：
- 转全量两条路：代码化（删 flag 分支保留实验组代码，发版）vs flag 常开（不删分支，flag 固定 true）——优先代码化（flag 分支长期留存是代码腐化）。
- 实验结论存档：实验报告（指标/置信度/决策）归档关联 flag——「为什么这个功能长这样」的历史可查。
- 负结果处置：实验失败 → 移除实验代码 + flag 清理（失败实验的代码残留是常见垃圾）；实验结论进知识库。
- 时序：实验结束 → 决策评审 → 代码化 PR → 常规发布流程（实验不是发布捷径）。
- 追问钩子：为什么实验转全量「优先代码化」而不是 flag 常开——flag 常开意味着实验分支永远在代码里（复杂度永续），且 flag 服务成为该功能的硬依赖（挂了功能失效）；代码化把实验产出变成「正常代码」，是一次性成本换长期清爽。

```javascript
async function concludeExperiment(exp) {
  const decision = await review(exp.report);           // 决策评审
  if (decision.adopt) {
    await createCodeMigrationPR(exp.flag);             // 删 flag 分支保留实验组代码
    await scheduleNormalRelease();                     // 走常规发布（非捷径）
  } else {
    await removeExperimentCode(exp);                   // 失败实验代码清理
  }
  archive({ exp, decision });                          // 结论归档进知识库
}
```
