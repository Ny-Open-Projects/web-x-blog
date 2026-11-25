---
title: [TST-235] 视觉 diff 结果如何呈现才能让评审者 10 秒做决策？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-235：视觉 diff 结果如何呈现才能让评审者 10 秒做决策？
**答**：
- 三联图并排：基线 / 实际 / diff 高亮（差异区红框），一眼看变化点。
- diff 分类标签先行（AI 分类：回归/可接受/噪声），分类可信时评审者只扫「回归」类。
- 变更摘要：差异像素比、受影响组件、关联样式变更 PR。
- 一键操作：接受为新基线（生成 PR）/ 标记误报（回流训练）。

```javascript
// 报告条目结构
const entry = {
  triple: ['baseline.png', 'actual.png', 'diff.png'],
  aiCategory: 'acceptable',
  diffRatio: 0.003,
  relatedPR: '#4321',
  actions: ['accept-baseline', 'mark-noise'],
};
r
```
