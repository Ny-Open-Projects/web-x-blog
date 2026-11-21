---
title: [V3-141] 手写 nextTick（微任务批处理）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-141：手写 nextTick（微任务批处理）？
**答**：
- 更新是异步批处理：改数据只把渲染 job 放进 queue（Set 天然去重），并用 Promise.then 注册一次 flush，同一轮内改 N 次只渲染 1 次。
- nextTick 返回 flush 完成后的 Promise，保证回调执行时 DOM 已更新；多个 nextTick 按注册顺序排队。
- flushing 标志区分当前批次：flush 期间新入队的 job 属于下一轮，保证本批次快照稳定。
- 兼容层可以口述：优先 Promise.then，降级 MutationObserver 再降级 setTimeout；源码还会按组件 uid 排序保证父先子后。

```javascript
// mini-next-tick.js
const queue = new Set();      // Set 天然去重：一个组件一帧内改多次只渲染一次
let flushing = false;
const resolvedPromise = Promise.resolve();

function queueJob(job) {
  // flushing 中新增的 job 交给下一轮，保证本次 flush 的快照稳定
  if (!flushing) queue.add(job);
  scheduleFlush();
}

function scheduleFlush() {
  if (!flushing) {
    flushing = true;
    resolvedPromise.then(flushJobs); // 微任务时机：同步代码全部跑完再统一渲染
  }
}

function flushJobs() {
  queue.forEach((job) => job()); // 生产版按 uid 排序：保证父组件先更新
  queue.clear();
  flushing = false;
}

// nextTick：把回调排在 flush 之后，拿到"已更新"的 DOM
function nextTick(fn) {
  const p = flushing ? resolvedPromise : resolvedPromise.then(flushJobs);
  return fn ? p.then(fn) : p;
}

// 验证批处理
const state = { count: 0 };
const render = () => console.log("渲染一次，count =", state.count);

queueJob(render);
queueJob(render);
queueJob(render); // 同一轮同步代码改 3 次
// 本轮微任务只输出一次：渲染一次，count = 0

nextTick(() => {
  console.log("DOM 已更新，可以安全读取尺寸/滚动位置");
});
```
