---
title: [JS-011] var、let、const 的区别？什么是暂时性死区？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-011：var、let、const 的区别？什么是暂时性死区？

**答**：
- var 函数作用域、存在变量提升（提升并初始化为 undefined）、可重复声明、挂到全局对象。
- let/const 块级作用域，提升但不初始化，声明前访问报 ReferenceError，即暂时性死区（TDZ）。
- const 声明时必须初始化且引用不可重新赋值，但对象内容仍可修改。
- 循环中的 let 每次迭代创建新绑定，这是 `for(let i...)` 闭包能拿到正确 i 的原因。

```javascript
console.log(a); // undefined，var 提升并初始化
var a = 1;

console.log(b); // ReferenceError，TDZ
let b = 2;

for (var i = 0; i < 3; i++) setTimeout(() => console.log(i)); // 3 3 3
for (let j = 0; j < 3; j++) setTimeout(() => console.log(j)); // 0 1 2

const list = [];
list.push(1);    // 允许，修改内容
// list = [];    // TypeError，禁止重指向
```
