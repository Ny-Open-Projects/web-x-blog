---
title: [BAS-024] var、let、const 有什么区别？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-024：var、let、const 有什么区别？
**答**：
- var：函数作用域、变量提升（声明前访问是 undefined）、可重复声明。
- let/const：块级作用域、暂时性死区（声明前访问直接报 ReferenceError）、不可重复声明。
- const 锁的是"绑定不可变"，对象内容仍可修改；规范：默认 const，需要重新赋值才 let，禁用 var。

```javascript
console.log(x); // undefined，var 提升且未报错
var x = 1;
console.log(y); // ReferenceError，暂时性死区
let y = 2;
const user = { name: 'A' };
user.name = 'B';  // 合法，const 锁的是绑定不是内容
// user = {};     // TypeError，绑定不可重新赋值
```
