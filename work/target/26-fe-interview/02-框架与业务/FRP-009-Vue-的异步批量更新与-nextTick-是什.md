---
title: [FRP-009] Vue 的异步批量更新与 nextTick 是什么原理？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-009：Vue 的异步批量更新与 nextTick 是什么原理？

**答**：
- 同一事件循环里多次修改状态，组件只会**更新一次**：每次修改触发 trigger 时，不直接执行渲染 effect，而是把组件的更新 job 放进一个去重的队列（`Set` 特性天然去重）。
- 队列通过 `Promise.then` 以**微任务**方式批量 flush——同步代码全部执行完后，一次跑完所有 job 并按组件 id 排序保证父先子后。
- `nextTick(cb)` 的 cb 会在 flush 完成后执行：`nextTick` 就是把回调 push 到同一个微任务队列的尾部，因此此时 DOM 已更新。
- 这也解释了"改了数据马上读 DOM 拿到旧值，包一层 nextTick 才是新值"。

```javascript
// 简化实现，帮助理解异步批量更新与 nextTick
const queue = new Set();     // Set 保证同一组件的更新 job 只入队一次
let isFlushing = false;
const resolvedPromise = Promise.resolve();
const pendingPostFlushCbs = [];

function queueJob(job) {
  queue.add(job);            // 去重：多次改同一组件状态，只有一个 job
  queueFlush();
}

function queueFlush() {
  if (!isFlushing) {
    isFlushing = true;
    // 微任务批量执行：同步代码全部跑完才 flush
    resolvedPromise.then(() => {
      try {
        queue.forEach((job) => job());
        queue.clear();
        // post 队列：nextTick 的回调排在所有更新之后
        pendingPostFlushCbs.forEach((cb) => cb());
        pendingPostFlushCbs.length = 0;
      } finally {
        isFlushing = false;
      }
    });
  }
}

function nextTick(cb) {
  if (isFlushing) pendingPostFlushCbs.push(cb); // 已在 flush 中，追加到本批末尾
  else resolvedPromise.then(cb);
}

// 验证批量更新
let renderCount = 0;
const componentJob = () => { renderCount++; console.log('DOM 更新，count =', count); };
let count = 0;

queueJob(componentJob);
queueJob(componentJob);       // 重复入队被 Set 去重
count = 1; count = 2; count = 3; // 三次修改
console.log('同步读取 count：', count, '，renderCount：', renderCount);
// 输出：同步读取 count 3，renderCount 0 —— 此刻 DOM 还是旧的
nextTick(() => console.log('nextTick 里 renderCount：', renderCount)); // 1 —— 只更新了一次
```
