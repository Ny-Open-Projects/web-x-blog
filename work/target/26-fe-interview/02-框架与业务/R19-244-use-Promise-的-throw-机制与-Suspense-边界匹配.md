---
title: [R19-244] use(Promise) 未完成时 throw 的 promise 是怎么被 Suspense 捕获的？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-244：use(Promise) 未完成时 throw 的 promise 怎么被 Suspense 捕获？
**答**：
- use 读到 pending promise 时以「抛出 promise」的方式中断渲染（可中断渲染模型），最近的 Suspense 边界捕获并展示 fallback。
- promise resolve 后 React 重新调度该子树渲染，use 返回数据继续渲染——数据缓存不变（同一 promise 再 use 不会重新 throw）。
- reject 时作为渲染错误抛出，由 ErrorBoundary 捕获；没有边界则页面崩溃。
- 边界匹配：throw 的 promise 会挂在触发它的子树，边界粒度决定重试范围——细粒度边界让其他区域不受影响。
- 与传统 usePromise hook 的区别：use 是渲染同步语义（数据即渲染），不需要 useEffect + loading 三态。
