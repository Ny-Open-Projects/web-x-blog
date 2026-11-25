---
title: [R19-264] commit 阶段的三个子阶段为什么不可中断？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-264：commit 阶段的三个子阶段为什么不可中断？
**答**：
- 三个子阶段：beforeMutation（读 DOM 快照，useLayoutEffect 前置）、mutation（写 DOM）、layout（useLayoutEffect/refs）。
- 不可中断原因：DOM 写入一旦开始中途停顿会出现「半更新 DOM」——用户可见的撕裂，且 cleanup/Effect 顺序依赖完整清单。
- 代价：commit 是同步长任务，大量 DOM 写入会掉帧——优化方向是减少 mutation 数量（虚拟化、memo），而非拆 commit。
- 异步效应：useEffect 在 paint 后异步执行（不阻塞帧），由调度器独立调度，可被清理。
- 面试表达：render 可中断、commit 不可中断，中间靠双缓冲与 effectList 衔接。
