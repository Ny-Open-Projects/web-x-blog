---
title: [FRP-091] React 18 的自动批处理是如何实现的？为什么 flushSync 能打断它？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-091：React 18 的自动批处理是如何实现的？为什么 flushSync 能打断它？

**答**：
- 批处理本质：多次 setState 只**入队不立即渲染**，`scheduleUpdateOnFiber` 把 fiber 标脏后检查"当前是否在渲染中"，不在则把根调度为一次渲染任务（`ensureRootIsScheduled`，默认 lane 走 Scheduler 的宏任务/微任务回调）。
- v17 及以前只有 React 事件处理器内的更新批处理（因为批处理标志由事件系统开关）；v18 用 `createRoot` 后**所有上下文**（setTimeout、Promise、原生事件）都批处理——调度器统一在**微任务（scheduleMicrotask → flushSyncCallbacks）** 中统一 flush 队列。
- `flushSync(fn)`：内部直接**同步执行渲染**（workLoopSync）并清空同步队列，fn 里的 setState 同步可见——用于需要在 React 更新后立刻读 DOM 的场景（如打开菜单后测量）；它是"打断微任务批处理"的唯一官方通道。
- 多次 setState 中若第一个是 flushSync，后续同步更新也跟着同步 flush；高优先级（离散事件）更新也会插队到当前 transition 渲染之前。

```javascript
// 简化实现，帮助理解微任务批处理与 flushSync
const syncQueue = new Set(); // 同步渲染回调队列
let isFlushingSync = false;
let isBatching = true; // React 18：任何上下文都默认批处理

function scheduleUpdate(fiberRoot, setStateFn) {
  syncQueue.add(setStateFn); // 入队去重，不渲染
  if (isFlushingSync) return;   // 正在同步 flush 中，等本轮结束
  if (isBatching) {
    // 微任务统一 flush：同一 tick 的所有 setState 合并成一次渲染
    scheduleMicrotask(flushSyncCallbacks);
  }
}
const scheduleMicrotask = (fn) => Promise.resolve().then(fn);

function flushSyncCallbacks() {
  if (isFlushingSync || !syncQueue.size) return;
  isFlushingSync = true;
  const fns = [...syncQueue];
  syncQueue.clear();
  fns.forEach((fn) => fn());  // 一次渲染循环执行所有更新
  isFlushingSync = false;
}

function flushSync(fn) {
  isBatching = false;            // 暂停批处理
  fn();                          // fn 内 setState 立即入队
  flushSyncCallbacks();          // 同步清空队列 -> DOM 立刻更新
  isBatching = true;             // 恢复批处理
}

// 验证：setTimeout 内的多次 setState 也被合并为一次渲染
let renderCount = 0;
const render = () => { renderCount++; console.log('render', renderCount); };
scheduleUpdate('root', render);
scheduleUpdate('root', render);
scheduleUpdate('root', render);
setTimeout(() => {
  console.log('after microtask, renderCount =', renderCount); // 1：三次合并一次
  flushSync(() => { scheduleUpdate('root', render); });
  console.log('after flushSync, renderCount =', renderCount); // 2：同步立即渲染
}, 0);
```
