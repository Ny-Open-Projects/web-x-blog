---
title: [BAS-021] null 和 undefined 有什么区别？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-021：null 和 undefined 有什么区别？
**答**：
- undefined：变量声明未赋值、函数缺参、对象缺属性——"系统层面没值"。
- null：开发者主动赋的空值，语义是"这里本应有值，现在置空"。
- `null == undefined` 为 true，`null === undefined` 为 false；`typeof null` 是 'object'。

```javascript
let a;
console.log(a);                  // undefined，声明未赋值
const obj = { name: null };      // 主动表示"置空"
console.log(null == undefined);  // true
console.log(null === undefined); // false
```
