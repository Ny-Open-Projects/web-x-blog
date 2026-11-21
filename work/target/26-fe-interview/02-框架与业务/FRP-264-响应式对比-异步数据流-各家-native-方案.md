---
title: [FRP-264] 异步数据流的各家原生方案对比？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-264：异步数据流的各家方案？
**答**：
- React：Suspense 数据层（use/action）+ TanStack Query——渲染等待语义内建。
- Vue：Suspense + composable（useAsyncData/自研）+ VueUse。
- Solid：createResource（内建异步信号，refetch/latest 缓存语义完整）——三者中最早原生集成。
- Svelte：await 块（模板级异步）+ load 函数（SvelteKit）。
- 对比维度：缓存去重、失效、乐观更新、SSR 脱水——TanStack Query 这类跨框架层把四家拉齐。
