---
title: [BAS-086] 浏览器和 Node 里全局的 this 分别是什么？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-086：浏览器和 Node 里全局的 this 分别是什么？
**答**：
- 浏览器普通 script 顶层 this 是 window；`type="module"` 模块顶层 this 是 undefined。
- Node CommonJS 文件顶层 this 是 module.exports；全局对象通过 globalThis 获取（即 global）。
- 跨环境取全局对象的标准方式是 globalThis，不要猜 window 或 global。

```javascript
// 浏览器 <script> 中
console.log(this === window);      // true
console.log(globalThis === this);  // true

// 浏览器 <script type="module"> 中
console.log(this === undefined);   // true

// Node CJS 模块中
// console.log(this === module.exports);  // true
```
