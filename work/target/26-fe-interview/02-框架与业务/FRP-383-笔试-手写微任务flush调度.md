---
title: [FRP-383] 笔试：手写微任务 flush 调度（Vue 式更新队列）
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 笔试题, 并发]
type: 笔试题
---

## FRP-383：笔试：手写微任务 flush

**答**：实现 Vue 式调度：① queueJob(job)：去重入队（同 job 不重复——id 对比）+ 微任务 flush；② flushJobs：按 id 排序执行（父组件先于子组件——job id 升序）；③ flush 中新入队的 job 也执行（本轮清空，防饥饿上限保护）；④ nextTick：flush 后执行（Promise.then 挂 flush promise）；⑤ flush 期间用户再触发 nextTick 的正确时序。写出实现。

```javascript
const queue = new Set();          // 保序去重
let flushing = false;
let currentFlushPromise = null;

function queueJob(job) {
  if (queue.has(job)) return;                       // 去重(引用)
  queue.add(job);                                   // Set 保插入序
  if (!flushing) currentFlushPromise = Promise.resolve().then(flushJobs);
}
async function flushJobs() {
  flushing = true;
  try {
    let guard = 0;
    while (queue.size) {
      if (++guard > 1000) throw new Error('flush 死循环保护');
      const jobs = [...queue].sort((a, b) => a.id - b.id);   // 父先于子
      queue.clear();
      for (const job of jobs) job();                 // 执行中新增的 job 会在下轮 while 处理
    }
  } finally {
    flushing = false;
    currentFlushPromise = null;
  }
}
function nextTick(fn) {
  const p = currentFlushPromise ?? Promise.resolve();
  return fn ? p.then(fn) : p;
}
// 时序: queueJob → 微任务 flush → (flush 内 new job 也清空) → nextTick 在 flush 后
```

**评分点**：
- 去重入队（Set 引用去重）与微任务延迟 flush
- 按 id 排序（父先子后）的更新顺序语义
- flush 中新 job 的本轮处理与死循环保护
- nextTick 挂 flush promise 的时序正确性
