---
title: [AIC-244] 线上 bug 修复后如何让 AI 自动沉淀回归测试，保证同类问题不再发生？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-244：线上 bug 修复后如何让 AI 自动沉淀回归测试，保证同类问题不再发生？
**答**：
- 输入三件套：bug 报告、修复 diff、复现步骤——AI 从中提取最小复现场景。
- 生成「先红后绿」用例：在未修复代码上必须失败（验证用例真实捕获 bug）。
- 用例命名关联 issue 编号，形成 bug→测试的可追溯链。
- 沉淀进评测集：同类组件的 AI 测试生成提示词带上这些回归用例作为范例。

```javascript
async function addRegressionCase(bug: { report: string; fixDiff: string; steps: string[] }) {
  const tc = await llm(`从 bug 报告与修复 diff 提炼最小回归用例：
${bug.report}\n${bug.fixDiff}\n步骤：${bug.steps.join(';')}
要求：在旧代码上必失败，命名含 ${bug.id}`);
  const red = await runTestOn(tc, { checkout: 'pre-fix' }); // 旧代码必须红
  if (!red.failed) throw new Error('用例未捕获 bug，废弃');
  await runTestOn(tc, { checkout: 'post-fix' }); // 新代码必须绿
  return tc;
}
r
```
