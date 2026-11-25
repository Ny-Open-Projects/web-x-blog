---
title: [BAS-090] in 和 hasOwnProperty 有什么区别？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-090：in 和 hasOwnProperty 有什么区别？
**答**：
- `'a' in obj` 检查键是否存在于对象及其整条原型链；hasOwnProperty 只查自身属性。
- 数组上 `0 in arr` 检查的是索引存在性而不是值；稀疏数组的空洞 in 为 false。
- 现代写法用 `Object.hasOwn(obj, 'a')`（ES2022），比直接调 obj.hasOwnProperty 更安全（对象可能没有原型方法）。

```javascript
const obj = Object.create({ inherited: 1 });
obj.own = 2;
console.log('own' in obj, 'inherited' in obj);  // true true
console.log(Object.hasOwn(obj, 'own'));         // true
console.log(Object.hasOwn(obj, 'inherited'));   // false
console.log(0 in [7]);                          // true，检查索引
```
