---
title: [JS-229] 全局变量与意外全局的泄漏
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 内存]
type: 面试题
---

## JS-229：全局变量与意外全局的泄漏

**答**：
- 显式全局：window 缓存对象长期只增不减（路由缓存、图表实例缓存）——需上限策略
- 意外全局：`foo = 1`（非严格模式自动挂 window）、`this.x = 1`（this 指向 window 的调用）——隐形钉子
- 防线：全项目 'use strict' / ESM 严格模式（意外赋值直接报错）；ESLint no-undef/no-unused-vars
- 缓存治理：全局缓存都要配「容量上限 + 淘汰策略」或改 WeakMap/WeakRef
- 排查：DevTools Memory 快照按 Constructor 过滤，Window 对象下突增的属性一眼可见

```javascript
// 意外全局的两种形态
function bad() { leaked = 42; }        // 严格模式报错；非严格挂 window
function badThis() { this.x = 1; }     // 裸调用时 this === window
// 全局缓存上限治理
const cache = new Map();
function set(k, v) {
  if (cache.size > 1000) cache.delete(cache.keys().next().value); // 简易 FIFO
  cache.set(k, v);
}
```
