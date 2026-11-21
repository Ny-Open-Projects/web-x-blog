---
title: [AIC-243] AI 生成的测试跑不过时，让 AI「自动修复到通过」有哪些风险？正确做法是什么？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-243：AI 生成的测试跑不过时，让 AI「自动修复到通过」有哪些风险？正确做法是什么？
**答**：
- 最大风险：AI 改测试迁就实现（把断言改成实际输出），实现错了测试照样绿。
- 正确做法：先让 AI 归因（实现 bug 还是测试错误），归因结论人确认后再修。
- 修复实现类：带上下文修代码；测试错误类：调整用例而非放宽断言。
- 门禁兜底：修复后的 diff 若只改断言期望值，标记人工必须复核。

```javascript
async function fixFailingTest(testFile: string) {
  const run = await runTest(testFile);
  const verdict = await llm(`测试失败：${run.error}
判断根因是「实现 bug」还是「测试错误」，给出依据，不要直接改代码。`);
  if (verdict.root === 'impl-bug') return fixImpl(verdict);
  return relaxTestReviewGate(verdict); // 放宽断言 → 必须人审
}
r
```
