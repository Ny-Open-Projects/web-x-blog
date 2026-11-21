---
title: [BLD-009] tapable 提供哪些钩子类型？各自适用什么场景？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-009：tapable 提供哪些钩子类型？各自适用什么场景？
**答**：
- Sync 系：SyncHook（顺序执行）、SyncBailHook（返回非 undefined 中断后续）、SyncWaterfallHook（上一个返回值传给下一个）、SyncLoopHook（返回 true 循环重试当前订阅）。
- AsyncSeries 系：串行 await，适合有先后依赖的异步步骤（如 beforeRun 校验环境）。
- AsyncParallel 系：并行执行不等待彼此，适合互不依赖的异步任务（如多线程压缩前的分发）。
- AsyncSeriesBailHook / AsyncSeriesLoopHook 与 Sync 同理加异步维度；带 -HookMap 后缀的是按 key 索引的钩子集合。
- 命名规律：Sync/Async（同步异步）+ Series/Parallel（串行并行）+ Bail/Waterfall/Loop（中断/传值/循环）。

```javascript
// tapable 各钩子类型行为对照
const {
  SyncHook, SyncBailHook, SyncWaterfallHook,
  AsyncSeriesHook, AsyncParallelHook,
} = require('tapable');

// SyncHook 顺序执行 无返回值
const sync = new SyncHook(['name']);
sync.tap('a', (n) => console.log('a', n));
sync.tap('b', (n) => console.log('b', n));
sync.call('webpack');

// SyncBailHook 返回非 undefined 则跳过后续订阅
const bail = new SyncBailHook(['name']);
bail.tap('a', () => 'stop');      // 返回了值
bail.tap('b', () => console.log('不会执行'));
bail.call('webpack');

// SyncWaterfallHook 返回值传给下一个订阅者
const wf = new SyncWaterfallHook(['val']);
wf.tap('double', (v) => v * 2);
wf.tap('plus1', (v) => v + 1);
console.log(wf.call(10)); // 21

// AsyncSeriesHook 串行异步 tapPromise/promise
const series = new AsyncSeriesHook(['name']);
series.tapPromise('a', async () => { await sleep(100); });
series.tapPromise('b', async () => { await sleep(100); });
series.promise('webpack'); // 总耗时约 200ms 串行

// AsyncParallelHook 并行异步
const parallel = new AsyncParallelHook(['name']);
parallel.tapPromise('a', async () => { await sleep(100); });
parallel.tapPromise('b', async () => { await sleep(100); });
parallel.promise('webpack'); // 总耗时约 100ms 并行

function sleep(ms) { return new Promise((r) => setTimeout(r, ms)); }
```
