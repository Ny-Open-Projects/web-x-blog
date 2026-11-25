---
title: [R19-265] React 18 自动批处理与 React 19 的批处理有什么差异？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-265：React 18 自动批处理与 React 19 的批处理有什么差异？
**答**：
- 18 起：所有更新（promise/timeout/原生事件）默认批处理，不再只有 React 事件内批处理。
- 19 的一致性：action/transition 内的多次 setState 同样合并；异步 await 后的更新也批处理（18 已支持）。
- 唯一逃逸口：flushSync 强制同步、unstable_batchedUpdates（旧版）已无需。
- 实务影响：一次事件里改 3 个 state 只渲染一次；批处理边界是「微任务队列 flush」，不是事件处理函数。
- 面试陷阱：批处理 ≠ 不渲染，而是「合并到一次渲染」；读取最新值用函数式 setState 或 flushSync。
