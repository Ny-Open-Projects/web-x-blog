---
title: [FRP-083] useTransition 的实现原理是什么？它和 lane 优先级调度是什么关系？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-083：useTransition 的实现原理是什么？它和 lane 优先级调度是什么关系？

**答**：
- useTransition 返回 `[isPending, startTransition]`：`startTransition(cb)` 把 cb 里的 setState 标记为 **TransitionLane（低优先级）**，紧急更新（如输入框 onChange 直接 setState）用 SyncLane/高优先级先渲染。
- 调度层：高优先级更新插入时**中断**正在进行的 Transition 渲染，完成紧急渲染后**重放** Transition 更新（基于 lane 模型的抢占式调度，React 18 双优先级通道）；isPending 是一个内部 useState，Transition 渲染开始置 true、结束置 false。
- 典型场景：受控输入 + 大列表过滤。输入的 setState 走紧急 lane（每键即时反馈），过滤结果的 setState 包在 startTransition 里（可被随时打断重排），列表卡顿消失。
- 关键点：transition 内的更新**不会被丢弃**，被打断后会以新状态重放；这也决定了它适合"非紧急、可延迟"的 UI 更新。

```javascript
// 简化实现，帮助理解 lane 分通道与抢占重放
let currentLane = null;
let isPending = false;
let transitionTask = null; // 被打断时可重放的任务

function setState(lane, fn) {
  currentLane = lane;
  if (lane === 'sync') {
    fn(); // 紧急更新：立即渲染，可打断 transition 渲染
    if (transitionTask) {
      // 模拟抢占：紧急渲染完成后重放 transition 更新
      isPending = true;
      transitionTask();
    }
  } else {
    transitionTask = fn; // transition：记录任务，等当前同步渲染后执行
    Promise.resolve().then(() => { transitionTask?.(); isPending = false; transitionTask = null; });
  }
  currentLane = null;
}

function useMyTransition() {
  return [
    () => isPending,
    (cb) => setState('transition', cb), // cb 内 setState 被标记为 TransitionLane
  ];
}

// 紧急 setState：直接通道
const setUrgent = (fn) => setState('sync', fn);

// 验证时序：紧急输入先渲染，列表过滤后渲染
const [getPending, startTransition] = useMyTransition();
let rendered = [];

setUrgent(() => rendered.push('input rendered'));         // 键入：同步先渲染
startTransition(() => rendered.push('list re-filtered')); // 过滤：transition 通道
setTimeout(() => console.log(rendered.join(' -> '), '| isPending after:', getPending()), 0);
// input rendered -> list re-filtered，若两者都走 sync，大列表会阻塞输入反馈
```
