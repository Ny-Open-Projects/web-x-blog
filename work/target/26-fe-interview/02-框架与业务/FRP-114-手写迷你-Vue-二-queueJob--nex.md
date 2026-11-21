---
title: [FRP-114] 手写迷你 Vue（二）：queueJob + nextTick 调度器与 watch？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-114：手写迷你 Vue（二）：queueJob + nextTick 调度器与 watch？

**答**：
- 调度器三件套：`queueJob`（Set 去重入队）、`flushJobs`（微任务统一执行，promise.then 保证同步代码全部跑完才渲染）、`nextTick`（flush 后的 Promise.then，拿到"更新后"的时机）。
- `watch(source, cb)` = effect 读 source + scheduler：数据变化时 effect 不立即重跑，scheduler 把它入队；flush 时先执行 effect 拿新旧值，再调 cb——这就是 watch 异步批处理与 `oldValue/newValue` 的来源。
- 队列内按 id 排序保证父组件先更新（父重渲染可能让子组件的更新失效/跳过）；flush 期间新入队的 job 在**同一轮**继续处理。

```javascript
// 简化实现，帮助理解：微任务调度器与 watch
const queue = new Set();
let flushing = false;
const resolvedPromise = Promise.resolve();
let currentFlushPromise = null;

function nextTick(fn) {
  const p = currentFlushPromise || resolvedPromise;
  return fn ? p.then(fn) : p; // 排在 flush 之后：拿到更新后的 DOM/状态
}
function queueJob(job) {
  if (!queue.has(job)) {            // Set 去重：同一次 flush 内同组件只更新一次
    queue.add(job);
    if (!flushing) currentFlushPromise = resolvedPromise.then(flushJobs);
  }
}
function flushJobs() {
  flushing = true;
  try {
    queue.forEach((job) => job());  // 逐个执行（真实实现按 id 排序父先子后）
  } finally {
    queue.clear(); flushing = false;
  }
}

// watch：effect + scheduler + 新旧值
function watch(source, cb) {
  let oldValue;
  const getter = typeof source === 'function' ? source : () => source;
  const job = () => {
    const newValue = getter();       // flush 时重算
    cb(newValue, oldValue);          // watch 回调：新值旧值在此产生
    oldValue = newValue;
  };
  oldValue = getter();               // 立即求值完成首次依赖收集
  effect(() => getter(), { scheduler: () => queueJob(job) }); // 变化只入队
}

// 验证：同一 tick 多次修改 -> watch 只触发一次（批处理）
let tickCount = 0;
const state = reactive({ n: 0 });
watch(() => state.n, (nv, ov) => console.log(`watch: ${ov} -> ${nv} (batched)`));
state.n = 1; state.n = 2; state.n = 3;   // 同步阶段三次修改
console.log('同步阶段：watch 尚未触发');
setTimeout(() => {
  console.log('微任务后：watch 触发一次, n =', state.n);
  nextTick(() => console.log('nextTick 回调：DOM 已更新, tick', ++tickCount));
}, 0);
// 输出顺序：watch 未触发 -> watch: 0 -> 3 -> nextTick 回调
```
