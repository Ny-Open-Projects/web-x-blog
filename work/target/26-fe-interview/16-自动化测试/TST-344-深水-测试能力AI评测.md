---
title: [TST-344] 「AI 生成测试」的能力评测如何做（评估 AI 测试工具）？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-344：「AI 生成测试」的能力评测如何做（评估 AI 测试工具）？
**答**：
- 评测任务集：20 个真实模块（含边界丰富的）让 AI 工具生成，人工评分。
- 评分维度：边界覆盖度/断言强度/可运行率/可维护性（分项打分）。
- 对照基线：与人工资深工程师产出对比（相对水平而非绝对分）。
- 场景分层：纯函数/组件/API mock 三类场景分别统计（能力差异大）。

```javascript
const aiTestEval = {
  tasks: 20, dims: ['boundary', 'assertion-strength', 'runnable', 'maintainability'],
  baseline: 'senior-engineer-same-task',
  byScenario: { pure: 0.85, component: 0.7, apiMock: 0.6 },   // 分场景通过率
};
r
```
