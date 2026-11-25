---
title: [R19-356] Scheduler 原理：MessageChannel 宏任务与小顶堆
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, Fiber]
type: 面试题
---

## R19-356：Scheduler 原理：MessageChannel 宏任务与小顶堆

**答**：
- 任务队列是小顶堆（按 expiration = startTime + timeout 排序）——performWorkUntilDeadline 从堆顶取任务
- MessageChannel 而非 setTimeout：postMessage 触发的宏任务在当前 task 结束后立即执行（无 4ms 聚合延迟），是「最快的宏任务」——SetImmediate 不跨浏览器、rAF 与渲染耦合
- shouldYield 控制流：每个工作单元后检查 `currentTime >= deadline`——deadline = frameStart + yieldInterval（5ms，isInputPending 高时降到 3ms）
- 优先级映射：Immediate（同步宏任务内立即跑）/UserBlocking(250ms)/Normal/Idle——Idle 用 requestIdleCallback 兜底（不可用时 setTimeout）
- 前端含义：理解「为什么 React 用宏任务切片」——微任务会让出后立即回来仍然阻塞渲染，宏任务给浏览器渲染机会

```text
scheduleCallback(priority, cb):
  exp = currentTime + timeoutByPriority[priority]
  heap.push({cb, exp}) → requestHostCallback
  → MessageChannel.port2.postMessage → port1.onmessage
  → performWorkUntilDeadline: while(任务 && !shouldYield) cb()
```
