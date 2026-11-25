---
title: [JS-259] 复杂输出题：变量提升与 TDZ 输出题
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 作用域]
type: 面试题
---

## JS-259：变量提升与 TDZ 输出题

**答**：
- 三种声明的提升行为：var 提升并初始化为 undefined；let/const 提升但不初始化（TDZ，访问即 ReferenceError）；function 声明整体提升（可先调用）
- 函数表达式：var fn 是 undefined（提升后）；let fn 是 TDZ——`fn()` 在声明前分别是 undefined 报错与 ReferenceError
- TDZ 范围：从块开始到声明语句——即使在同一块内「先打印后声明」也报错
- 高频变体：同名函数与 var（函数声明赢）；块内函数声明在不同模式下的行为差异（严格模式下块作用域）

```javascript
console.log(a); // undefined（var 已提升）
var a = 1;
console.log(b); // ❌ ReferenceError（TDZ）
let b = 2;
foo();          // 'hoisted'（函数声明整体提升）
function foo() { console.log('hoisted'); }
bar();          // ❌ TypeError: bar is not a function（var 提升 undefined）
var bar = () => {};
```
