---
title: [FRP-030] React 18 的自动批处理是什么原理？为什么 setState 是异步的？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-030：React 18 的自动批处理是什么原理？为什么 setState 是异步的？

**答**：
- `setState` 本身不执行更新，只是把 update 排进对应 hook 的队列并**调度一次 render**；真正的更新在微任务/调度器回调里批量执行——这就是"异步"的体感来源。
- 批处理：同一事件循环内的多次 setState 合并为**一次 render**，只取最终值；React 17 只在合成事件与生命周期内批处理，18 起通过 `ensureRootIsScheduled` 让 Promise/setTimeout/原生事件里也批处理。
- 实现核心：调度入口加 `isBatching` 标记，多次 setState 只安排一次 `flushWork`（微任务），flush 时统一处理所有排队的 update。
- `flushSync` 可强制同步 flush，用于"改完立即读 DOM"的场景。

```javascript
// 简化实现，帮助理解批量更新
let isBatching = false;
const pendingRoots = new Set();

function scheduleRender(fiber) {
  pendingRoots.add(fiber);          // 多次 setState 只累积
  if (isBatching) return;           // 已有 flush 在排队，不重复调度
  isBatching = true;
  Promise.resolve().then(flushWork); // 微任务批量执行 —— 这就是"异步"的本质
}

function flushWork() {
  isBatching = false;
  const roots = [...pendingRoots];
  pendingRoots.clear();
  roots.forEach((root) => renderFromRoot(root)); // 一次 render 消费所有 update
}

// 用法验证：
// function handleClick() {
//   setCount(1);        // 只排队
//   setCount(n => n + 1); // 只排队
//   setName('x');       // 只排队
//   console.log(count); // 0 —— 还没 render，拿到旧值
//   // 本次事件结束后微任务 flush，一次 render：count 最终为 2
// }

// React 18 前后的差异：setTimeout 内 React 17 会 render 两次，18 仍批处理
// setTimeout(() => {
//   setCount(n => n + 1);
//   setName('y');
//   // React 18：一次 render；React 17：两次 render
// }, 0);

// 需要同步拿最新 DOM 时用 flushSync
// import { flushSync } from 'react-dom';
// flushSync(() => setCount(10));
// console.log(ref.current.textContent); // 立即是 10
```
