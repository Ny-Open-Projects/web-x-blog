---
title: [WEB-254] 浏览器事件循环与 Node 事件循环的区别
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 浏览器]
type: 面试题
---

## WEB-254：浏览器事件循环与 Node 事件循环的区别

**答**：
- 共同内核：宏任务（script/回调）→ 清空微任务队列（Promise.then、queueMicrotask）→ 可能渲染。
- 浏览器：任务队列按 source 分（定时器/IO/事件），无阶段概念；每个宏任务后检查是否需要渲染（rAF 在渲染前、样式/布局在那之后）。
- Node（libuv）：六阶段循环 timers → pending → poll → check（setImmediate）→ close；微任务在每阶段切换间清空；process.nextTick 队列优先级最高。
- 关键差异：`setTimeout(fn,0)` 与 `setImmediate` 在 Node 主模块里顺序不确定，但在 I/O 回调里 setImmediate 一定先跑；浏览器没有 setImmediate。
- Node 11+ 后对齐浏览器：单个宏任务后立即清微任务（此前是每阶段一次），输出题里高频。

```javascript
// Node 11+ 输出（与浏览器不同的关键示例）
setTimeout(() => console.log('timeout'), 0);
setImmediate(() => console.log('immediate'));
Promise.resolve().then(() => console.log('microtask'));
// 输出: microtask → timeout/immediate（顺序不定）
// 但在 I/O 回调中 setImmediate 先于 setTimeout 触发
```
