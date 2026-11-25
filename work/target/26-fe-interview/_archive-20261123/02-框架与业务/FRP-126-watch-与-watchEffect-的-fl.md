---
title: [FRP-126] watch 与 watchEffect 的 flush 时机（pre/post/sync）在源码层面是怎么实现的？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-126：watch 与 watchEffect 的 flush 时机（pre/post/sync）在源码层面是怎么实现的？

**答**：
- 三种 flush 对应 job 的三种排队策略：`pre`（默认）job 标记 PRE，进队列且**排在所属组件 update job 之前**；`post` 标记 POST，排在组件更新之后（靠 flag 让调度器在 flushJobs 里分区段取）；`sync` 完全不进队列，变更当场执行。
- 因此行为差异：pre 回调里读 DOM 是**旧**的（组件还没重渲）；post 里是新 DOM；sync 连批量更新都不等（适合必须同步的极少数场景）。
- 源码实现要点：watcher 的 job 挂 `flags`（ALLOW_RECURSE / PRE / POST），queueJob 入队时按 flags 与 job.id 排序，flushJobs 一次微任务里按 id 升序执行，POST 段在组件更新段之后。
- watchEffect 与 watch 共用这套调度，区别只在前者"立即执行一次并自动收集依赖"，后者是"getter + 显式 source"。

```javascript
// 简化实现，帮助理解 pre/post/sync 的调度
const queue = new Set(); // 真实实现按 id 排序的数组，这里用 Set 去重
let isFlushing = false;
const p = Promise.resolve();

function queueJob(job) {
  if (job.flags === 'sync') return job();            // sync：跳过队列
  queue.add(job);
  if (!isFlushing) { isFlushing = true; p.then(flushJobs); } // 微任务批处理
}
function flushJobs() {
  isFlushing = false;
  // 源码级关键：先执行 pre（组件更新前），再组件 update，最后 post
  const jobs = [...queue]; queue.clear();
  jobs.filter(j => j.flags === 'pre').forEach(j => j());
  jobs.filter(j => j.flags === 'update').forEach(j => { j(); }); // 组件重渲染
  jobs.filter(j => j.flags === 'post').forEach(j => j());
}

let dom = '旧 DOM';
function componentUpdate() {
  queueJob({ flags: 'update', id: 1, fn() { dom = '新 DOM'; console.log('  [组件更新]'); } });
}

// watch(source, cb, { flush: 'pre' }) —— 默认
function watch(cb, flush = 'pre') {
  const job = { flags: flush, id: 2, fn: cb };
  return () => queueJob(job); // 简化：触发即入队
}
const log = (tag) => () => console.log(`  [watch ${tag}] DOM = ${dom}`);

const preWatch = watch(log('pre'), 'pre');
const postWatch = watch(log('post'), 'post');
const syncWatch = watch(log('sync'), 'sync');

console.log('数据变更：');
componentUpdate(); // 组件更新入队
preWatch();        // pre 入队（会先于 update 执行）
postWatch();       // post 入队（晚于 update）
syncWatch();       // sync 立即执行：DOM = 旧 DOM
// 输出顺序：sync（立即、旧 DOM）→ 微任务里 pre（旧 DOM）→ 组件更新 → post（新 DOM）
```
