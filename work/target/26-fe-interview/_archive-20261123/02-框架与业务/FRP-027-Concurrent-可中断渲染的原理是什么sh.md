---
title: [FRP-027] Concurrent 可中断渲染的原理是什么？shouldYield 如何判断让出？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-027：Concurrent 可中断渲染的原理是什么？shouldYield 如何判断让出？

**答**：
- Scheduler 把渲染工作拆成一个个 Fiber 单元（unit of work），`workLoop` 用 while 循环逐个执行，**每完成一个单元就检查 `shouldYield()`**：当前帧剩余时间不足（已用超过 5ms）或有更高优先级任务插入，就中断并返回。
- 中断后通过 `hostCallback` 重新调度（MessageChannel 宏任务），**从 `workInProgress` 指针处继续**——链表结构保证了现场可恢复。
- 高优先级插队：新更新的 lane 更高时，丢弃当前进行中的 render（成果保留在 pending 队列），先渲染紧急更新，再低优重放。
- 用户感知：点击输入这类 SyncLane 同步完成，而 startTransition 的大列表渲染被切成多帧执行，输入始终跟手。

```javascript
// 简化实现，帮助理解可中断渲染 workLoop
// 简化实现，帮助理解 React Scheduler
const schedulerChannel = new MessageChannel();
let taskQueue = [];      // 按 lane 排序的任务队列
let currentTask = null;

// shouldYield：帧时间预算判断（源码为 frameYieldMs = 5）
function shouldYield() {
  if (currentTask === null) return false;
  const elapsed = performance.now() - currentTask.startTime;
  return elapsed > 5; // 单个任务片超过 5ms 就让出，给浏览器渲染与输入留时间
}

schedulerChannel.port1.onmessage = () => {
  currentTask = taskQueue.shift();
  if (!currentTask) return;
  const { workLoop, onDone } = currentTask;

  // 核心：循环 + 可中断
  while (workLoop()) {
    if (shouldYield()) {           // 时间片用完
      schedulerChannel.port2.postMessage(null); // 让出主线程，稍后从断点继续
      return;
    }
  }
  onDone?.();
};

// 用法：把一棵 Fiber 树的渲染包装成可中断任务
function performConcurrentWork(root) {
  let workInProgress = root.child;
  taskQueue.push({
    startTime: performance.now(),
    // workLoop 每次调用处理一个 Fiber 单元，返回是否还有剩余工作
    workLoop: () => {
      if (!workInProgress) return false;
      beginWork(workInProgress);            // 处理当前单元
      workInProgress = nextUnitOfWork(workInProgress);
      return true;                          // 还有工作未完成
    },
    onDone: () => commitRoot(root),
  });
  schedulerChannel.port2.postMessage(null);
}

// startTransition 的更新进入低优先级队列：被紧急更新插队后可整体丢弃重放
function startTransition(fn) {
  const prevLane = currentUpdateLane;
  currentUpdateLane = TransitionLane1;
  fn(); // 里面的 setState 以 TransitionLane 调度
  currentUpdateLane = prevLane;
}
```

## 五、React Hooks 原理
