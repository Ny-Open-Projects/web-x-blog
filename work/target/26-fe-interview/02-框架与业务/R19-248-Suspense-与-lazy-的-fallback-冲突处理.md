---
title: [R19-248] Suspense 同时有 lazy 组件和异步数据时 fallback 怎么表现？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-248：Suspense 同时有 lazy 组件和异步数据时 fallback 怎么表现？
**答**：
- lazy 的 chunk 加载也是「throw promise」：与数据 promise 走同一 Suspense 机制，fallback 在两者都未就绪时持续展示。
- 时序：chunk 加载完 → 组件渲染 → 内部 use(promise) pending → 同一边界继续 fallback（如果数据在边界内）→ 全就绪显示。
- 优化：边界拆分让「组件加载完成但数据未到」时可以显示组件骨架而非全屏 fallback。
- 兜底：Suspense 可配置 expectedActivity？不——React 用 fallbackChain 合并多个 pending，注意嵌套边界的 fallback 覆盖关系（内层优先）。
- 实践清单：chunk 预取（hover/idle）、数据预取（路由级）、边界粒度设计三者齐备才不闪。
