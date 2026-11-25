---
title: [JS-250] 逻辑赋值运算符 ||= &&= ??= 的行为
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 语法]
type: 面试题
---

## JS-250：逻辑赋值运算符 ||=、&&=、??=

**答**：
- 语义：`a ||= b` ≈ `a || (a = b)`——a 为假值才赋值；`??=` 仅在 null/undefined 时赋值（最常用）
- 与数学赋值（+=）的区别：逻辑赋值「条件触发」，不满足时不执行赋值（无副作用写法差异）
- ??= 的黄金场景：默认值初始化——`config.timeout ??= 5000`（0 是合法值不会被覆盖，||= 会覆盖掉 0！）
- 陷阱对比表：||= 把 0/''/false 当「未设置」；??= 只有 null/undefined 算未设置——选错就出 bug

```javascript
let t = 0;
t ||= 5000;   // 变成 5000 —— 0 被误伤！
t = 0;
t ??= 5000;   // 仍是 0 —— nullish 只认 null/undefined ✅

let opts = { retries: null };
opts.retries ??= 3;    // 3
opts.retries ??= 9;    // 仍 3
```
