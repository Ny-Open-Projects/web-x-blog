---
title: [AIC-558] AI 辅助重构的安全策略
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-558：AI 重构的安全策略

**答**:
- AI 重构的安全策略：1) **测试先行**（重构前确保测试覆盖——重构 = "行为不变的代码变更"（测试是行为不变的验证器 RBL-518 Agent 传感器）；无测试的重构 = 盲改（行为可能变——不可验证）；2) **小步重构**（每次一个 transformation（提取函数/重命名/移动文件——单步可验证——不做大爆炸式重构）；3) **行为保持验证**（每步重构后运行测试 → 通过则继续，失败则回滚 RBL-558 的 Agent 循环；4) **AI 重构的范围约束**（AI 只重构、不改行为——prompt 约束"不要添加新功能" RBL-512 最小 diff 原则）。
- AI 重构的风险：1) **行为改变**（AI 在"重构"时偷偷改变了行为——变量名变了但逻辑也变了；2) **边界丢失**（AI 重构时删除了边界检查——`if (!x)` 被简化掉 RBL-532 审查重点；3) **间接破坏**（重构 A 模块导致 B 模块的隐式依赖断裂）；防御：每步测试 + diff 审查（RBL-512 最小 diff + RBL-532 检查点）。
- 追问钩子：为什么「测试先行」是 AI 重构的前提而非建议？——AI 重构 = "行为不变的代码变更"——"行为不变"需要验证机制（测试是唯一的自动验证器）；无测试 = 无法验证"行为不变"（重构可能引入 bug 但没人知道）；测试覆盖率 100% → AI 重构的安全网完整 → Agent 可以自主重构（RBL-518 传感器覆盖）；0% → AI 重构 = 盲改——先写测试再重构（RBL-519 Agent 分解器）。

```typescript
// AI 重构的安全流程
async function safeRefactor(ai: AIAgent, target: string, tests: string) {
  // 1) 前置验证：测试必须通过
  const preResult = await runTests(tests);
  if (!preResult.ok) throw new Error('重构前测试必须通过');
  // 2) AI 重构（单步）
  const diff = await ai.refactor(target, { constraint: 'behavior-preserving, minimal diff' });
  // 3) 后置验证：测试仍然通过
  const postResult = await runTests(tests);
  if (!postResult.ok) {
    // 回滚
    await revertDiff(diff);
    throw new Error('重构后测试失败——已回滚');
  }
  // 4) diff 审查（人审最小 diff）
  return { diff, preResult, postResult };
}
```
