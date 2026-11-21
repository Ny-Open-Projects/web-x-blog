---
title: [PER-018] requestIdleCallback 的作用是什么？如何封装降级？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-018：requestIdleCallback 的作用是什么？如何封装降级？

**答**：
- 在浏览器**空闲期**执行低优先级任务，不与渲染抢主线程，适合预计算、日志清洗、非首屏数据预取。
- 回调收到 `deadline.timeRemaining()`，应把大任务切成小片，每片做完检查剩余时间。
- 两个注意点：回调可能一次都不执行（一直不空闲），所以可传 `{ timeout }` 强制超时前执行；Safari 长期不支持，需 `setTimeout` 降级。
- 与 `requestAnimationFrame` 相对：rAF 在渲染前跑高优先级任务，rIC 在渲染后跑低优先级任务。

```javascript
// Safari 不支持时用 setTimeout 降级
const ridle =
  window.requestIdleCallback ||
  ((cb) => setTimeout(() => cb({ timeRemaining: () => 50, didTimeout: false }), 1));
const cidle = window.cancelIdleCallback || ((id) => clearTimeout(id));

// 把大量预计算任务切成小片，空闲时执行，且最多等 2 秒保证最终会跑
const tasks = [
  () => precomputeSearchIndex(),
  () => precomputeDictionary(),
  () => warmupRouteCache()
];

const id = ridle(function run(deadline) {
  while (deadline.timeRemaining() > 0 && tasks.length) {
    tasks.shift()();
  }
  if (tasks.length) ridle(run, { timeout: 2000 });
}, { timeout: 2000 });

// 需要时可以取消：cidle(id)
```
