---
title: [JS-256] 复杂输出题：闭包与循环 var/let 输出题原理
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 笔试题, 闭包]
type: 面试题
---

## JS-256：闭包与循环 var/let 输出题原理

**答**：
- var 版：循环变量是函数作用域唯一变量，所有闭包共享同一「槽位」——循环跑完后 i = 3，回调读到 3
- let 版：每次迭代创建新的词法环境（块级绑定逐次复制），每个闭包捕获各自的 i——输出 0/1/2
- 原理深化：let 的「每次迭代新绑定」是规范行为（CreatePerIterationEnvironment），不是语法糖巧合
- 变体陷阱：setTimeout 传参版 `setTimeout(fn, 0, i)`——参数复制与闭包无关，var 也输出 0/1/2；IIFE 版同理

```javascript
for (var i = 0; i < 3; i++) setTimeout(() => console.log(i));   // 3 3 3
for (let i = 0; i < 3; i++) setTimeout(() => console.log(i));   // 0 1 2
for (var j = 0; j < 3; j++) setTimeout((x) => console.log(x), 0, j); // 0 1 2（传参复制）
```
