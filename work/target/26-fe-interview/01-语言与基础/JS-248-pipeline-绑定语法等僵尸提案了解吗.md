---
title: [JS-248] pipeline、绑定语法等「僵尸提案」了解吗
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 新特性]
type: 面试题
---

## JS-248：了解 pipeline、绑定语法等长期停滞的提案吗

**答**：
- Pipeline（|> 函数管道）：社区争论「占位符风格 vs 无占位符」多年停滞——争议即僵尸原因的典型
- 部分应用语法（~fn(1, ?)）/ 绑定操作符（::this.map）：被「更简单的替代」（箭头函数）覆盖了大部分场景
- do 表达式、throw 表达式：仍在 stage 但节奏慢； pattern matching（match 语法）推进中但未定
- 判断价值的框架：一个语法若「现有语法能自然表达」，优先级就低——提案死活的经验法则
- 面试话术：不用背列表，能举 2 个例子 + 说清「为何停滞」（争议/被替代）即体现对提案流程的了解

```javascript
// pipeline 设想（未实现）：
// "  hello  " |> trim |> toUpper |> (% + "!");
// 现实替代：函数组合工具
const compose = (...fns) => (x) => fns.reduce((v, f) => f(v), x);
compose(toUpper, trim, addBang)("  hello  ");
```
