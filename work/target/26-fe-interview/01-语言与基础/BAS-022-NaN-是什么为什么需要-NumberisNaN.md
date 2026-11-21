---
title: [BAS-022] NaN 是什么？为什么需要 Number.isNaN？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-022：NaN 是什么？为什么需要 Number.isNaN？
**答**：
- NaN 是非法数值运算的结果，如 `Number('abc')`、`0/0`；它与任何值都不相等，包括自身。
- 全局 `isNaN` 会先把参数转数字，`isNaN('abc')` 也返回 true，存在误判。
- `Number.isNaN` 不做转换，只有参数真的是 NaN 才返回 true；也可用 `Object.is(x, NaN)`。

```javascript
Number('abc');               // NaN
NaN === NaN;                 // false，NaN 不等于任何值
isNaN('abc');                // true，'abc' 先被转成了 NaN
Number.isNaN('abc');         // false，字符串本身不是 NaN
Number.isNaN(Number('abc')); // true
```
