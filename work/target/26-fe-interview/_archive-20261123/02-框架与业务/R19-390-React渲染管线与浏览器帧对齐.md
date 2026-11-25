---
title: [R19-390] React 渲染管线与浏览器帧对齐
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## R19-390：React 渲染管线与浏览器帧对齐

**答**：
- 帧对齐模型：Scheduler 时间片（5ms）让渲染落在「一帧内非渲染时段」——时间片耗尽让出 → 浏览器有机会 paint → 下帧继续
- 为什么 5ms：给「输入事件处理 + 样式/布局」留预算；isInputPending API（实验）在支持的浏览器把时间片动态压到 3ms——输入优先
- useLayoutEffect 与帧：同步 commit 内执行——「读布局改样式」的连锁（layout thrashing）在 React 里同样存在（多个 layout effect 链式读写）
- React 19 的 frame 探索：View Transition 集成、useDeferredValue 的重渲染尽量贴帧——框架向「帧预算意识」演进
- 业务指导：动画循环别放 setState（用 ref+WAAPI）；重计算放 transition/Worker——「React 内的帧纪律」与原生一致

```text
一帧 16.7ms:
  输入事件 → React 时间片(≤5ms) → 样式/布局 → paint
  React 保证: 输入处理即时(discrete lane), 渲染可让出(时间片)
反模式: rAF 里 setState 高频 → 渲染队列堆积掉帧
```
