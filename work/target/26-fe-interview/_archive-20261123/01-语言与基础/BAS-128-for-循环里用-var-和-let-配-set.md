---
title: [BAS-128] for 循环里用 var 和 let 配 setTimeout 输出有什么区别？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-128：for 循环里用 var 和 let 配 setTimeout 输出有什么区别？
**答**：
- var 版本：i 是函数级全局绑定，回调执行时循环已结束，输出 3 3 3。
- let 版本：每轮迭代都会创建一个全新的 j 绑定，闭包捕获当轮副本，输出 0 1 2。
- 本质：let 的块级作用域 + 迭代级新建绑定，等价于每轮用 IIFE 复制一份值。

```javascript
for (var i = 0; i < 3; i++) setTimeout(() => console.log(i));
// 输出 3 3 3：三个闭包共享同一个全局 i，执行时 i 已经是 3

for (let j = 0; j < 3; j++) setTimeout(() => console.log(j));
// 输出 0 1 2：let 每轮迭代新建绑定，闭包捕获的是当轮的 j 副本
```
