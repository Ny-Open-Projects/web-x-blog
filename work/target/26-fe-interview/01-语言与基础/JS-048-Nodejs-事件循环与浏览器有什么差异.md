---
title: [JS-048] Node.js 事件循环与浏览器有什么差异？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-048：Node.js 事件循环与浏览器有什么差异？

**答**：
- Node 分六个阶段：timers → pending callbacks → poll → check（setImmediate）→ close callbacks。
- `process.nextTick` 优先级最高，在每阶段切换前清空，且先于 Promise 微任务。
- setTimeout 与 setImmediate 的先后受进入时机影响：主模块中顺序不确定，I/O 回调里 setImmediate 先执行。
- 浏览器没有多阶段概念，Node 有微任务/nextTick 队列在阶段间 drained 的规则。

```javascript
// Node.js 环境
setImmediate(() => console.log('immediate'));
setTimeout(() => console.log('timeout'), 0);
// 主模块中：顺序不确定（取决于 1ms 对齐）

require('fs').readFile(__filename, () => {
  setTimeout(() => console.log('timeout in io'), 0);
  setImmediate(() => console.log('immediate in io'));
  // I/O 回调内：immediate 先输出，进入 check 阶段
});

Promise.resolve().then(() => console.log('promise'));
process.nextTick(() => console.log('nextTick'));
// 输出顺序：nextTick → promise
```

## 七、ES6+ 新特性
