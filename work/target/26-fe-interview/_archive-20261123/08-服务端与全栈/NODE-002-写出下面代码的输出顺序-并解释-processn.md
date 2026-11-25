---
title: [NODE-002] 写出下面代码的输出顺序，并解释 process.nextTick 与 Promise 的优先级？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-002：写出下面代码的输出顺序，并解释 process.nextTick 与 Promise 的优先级？
**答**：
- `process.nextTick` 有**独立队列**，优先级高于 Promise 微任务：每个宏任务结束后，先清空 nextTick 队列，再清空 Promise 队列（若 nextTick 回调中又产生 nextTick，会持续清空，存在饿死 I/O 的风险，Node 对 nextTick 队列有最大深度保护但需警惕）。
- `setImmediate` 属于 check 阶段的宏任务，晚于所有微任务。
- 输出顺序（高频输出题）：`start` → `nextTick1` → `nextTick2` → `promise1` → `promise2` → `immediate` → `timeout`。

```javascript
console.log('start');

process.nextTick(() => {
  console.log('nextTick1');
  process.nextTick(() => console.log('nextTick2')); // 追加到 nextTick 队列尾，仍先于 Promise
});

Promise.resolve()
  .then(() => {
    console.log('promise1');
    Promise.resolve().then(() => console.log('promise2'));
  });

setImmediate(() => console.log('immediate')); // check 阶段
setTimeout(() => console.log('timeout'), 0);  // timers 阶段，check 先于 timers

// 输出：start nextTick1 nextTick2 promise1 promise2 immediate timeout
```
