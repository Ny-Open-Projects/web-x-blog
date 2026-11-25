---
title: [AIC-580] 从 diff 推断开发者意图
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-580：从 diff 推断开发者意图

**答**:
- 从 diff 推断意图的模式：1) **bugfix 模式**（改动集中在条件判断/边界检查/错误处理——`if (x)` 变 `if (!x || x === 0)`——修复了漏判的边界；2) **feature 模式**（新增文件/新增函数/import 新包——新功能开发；3) **refactor 模式**（文件移动/函数提取/import 重排——不改行为的重构；4) **performance 模式**（加 memo/useMemo/useCallback/虚拟列表——性能优化意图）。
- 意图推断的用途：1) **自动标注 PR**（PR 标签：bugfix/feature/refactor/performance——审阅者快速了解 PR 性质 RBL-549）；2) **审查重点建议**（bugfix PR → 重点审边界条件；feature PR → 重点审新功能的完整性；3) **CI 策略调整**（bugfix PR → 跑全部测试；docs PR → 跳过测试 RBL-631）。
- 追问钩子：为什么「从 diff 推断意图」是 AI 代码审查的"预处理步骤"？——意图推断 → 决定审查策略（"这是什么类型的变更" → "应该重点看什么"）；不推断意图 → 审查者自己判断（可能判断错——把 bugfix 当 feature 审——重点错位）；「意图推断 = 审查的路标」：意图对了 → 审查的方向对了——推断错了 → 审查方向全错；意图推断的准确性 = 审查效率的前提。

```typescript
// diff 意图推断
function inferIntentFromDiff(diff: {
  newFiles: string[]; modifiedFiles: string[];
  newImports: string[]; changedPatterns: {
    conditionals: number; errorHandling: number;
    memoHooks: number; extractedFunctions: number;
  };
}): { intent: string; confidence: number; reviewFocus: string } {
  let intent = 'feature'; let confidence = 50; let focus = '功能完整性';
  if (diff.changedPatterns.conditionals > 3 && diff.changedPatterns.errorHandling > 2
      && !diff.newFiles.length) {
    intent = 'bugfix'; confidence = 80; focus = '边界条件与错误处理';
  } else if (diff.changedPatterns.memoHooks > 2) {
    intent = 'performance'; confidence = 75; focus = '性能优化正确性';
  } else if (diff.changedPatterns.extractedFunctions > 2 && !diff.newImports.length) {
    intent = 'refactor'; confidence = 70; focus = '行为不变性验证';
  } else if (diff.newFiles.length > 0 || diff.newImports.length > 0) {
    intent = 'feature'; confidence = 75; focus = '新功能的边界与安全';
  }
  return { intent, confidence, reviewFocus: focus };
}
```
