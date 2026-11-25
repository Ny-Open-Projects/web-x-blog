---
title: [AIC-755] AI 生成代码的可维护性如何量化评估
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-755：AI 生成代码的可维护性如何量化评估

**答**：
- 结论先行：可维护性可量化为「可维护性指数（MI）」——综合代码行数、圈复杂度、注释比例、重复度；AI 代码常见问题不是「不能跑」，而是「难维护」（嵌套过深、命名抽象、重复堆砌）。
- 维度：1) 圈复杂度（分支越多越难测）；2) 函数长度（超长函数难理解）；3) 重复代码率（复制粘贴）；4) 命名质量（语义 vs 抽象）；5) 注释/文档比。
- 用法：设阈值门禁，超标的 AI 产出要求重构后再合入；把 MI 趋势作为团队 AI 质量的长期观测指标。
- 追问钩子：为什么高复杂度的 AI 代码更危险？——复杂度高的代码 bug 密度更高、测试更难覆盖，且 AI 后续修改更容易引入回归。

```javascript
// 简化可维护性指数：行数、复杂度、重复度加权
function maintainability({ loc, complexity, dupRatio, commentRatio }) {
  const clamped = v => Math.max(0, Math.min(1, v));
  const score = 100
    - Math.min(loc / 5, 40)
    - Math.min(complexity * 2, 30)
    - clamped(dupRatio) * 20
    + clamped(commentRatio) * 10;
  return Math.max(0, Math.min(100, score));
}
console.log(maintainability({ loc: 100, complexity: 3, dupRatio: 0.1, commentRatio: 0.2 }).toFixed(0)); // 约 52
console.log(maintainability({ loc: 20, complexity: 1, dupRatio: 0, commentRatio: 0.3 }).toFixed(0));    // 93
```
