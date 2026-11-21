---
title: [DP-221] 源码识别：React Fiber 双缓冲与调度优先级队列？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-221：源码识别：React Fiber 双缓冲与调度优先级队列？
**答**：
- 备忘录/双缓冲：current 树与 workInProgress 树两份快照交替，alternate 指针互指——可中断渲染靠"从快照恢复"（DP-153 备忘录思想的调度级实现）。
- 优先级队列：update 队列按 lane（优先级位图）排序，调度器（Scheduler）用最小堆按 expirationTime 取任务——高优先级插队、低优先级饥饿防范。
- 状态机：fiber 的 tag/lanes/effectsFlags 编码节点所处阶段（render → commit），可中断点在 render 阶段。
- 识别要点：能说清"lane 是优先级 + 批次的双重编码"，以及 commit 阶段不可中断的原因（DOM 一致性）。

```javascript
// Scheduler 最小堆调度（源码级简化）
const taskQueue = new MinHeap((a, b) => a.expirationTime - b.expirationTime);
function scheduleCallback(priority, callback) {
  const expirationTime = now() + priorityTimeoutMap[priority];   // lane → 超时
  taskQueue.push({ callback, expirationTime });
}
function workLoop(deadline) {
  while (taskQueue.size && !shouldYield(deadline)) {             // 时间切片
    const task = taskQueue.pop();
    task.callback();                                             // 执行一个 render 单元
  }
  if (taskQueue.size) requestAnimationFrame(workLoop);           // 让路
  else commitRoot();                                             // commit 不可中断
}
function shouldYield(deadline) { return deadline.timeRemaining() < 1 || hasHigherPriorityArrived(); }
// 双缓冲：workInProgress.alternate === current；commit 后 workInProgress 成为新 current
```
