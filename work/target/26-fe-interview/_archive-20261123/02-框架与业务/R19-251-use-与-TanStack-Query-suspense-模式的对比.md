---
title: [R19-251] 原生 use 与 TanStack Query 的 useSuspenseQuery 怎么对比？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-251：原生 use 与 TanStack Query 的 useSuspenseQuery 怎么对比？
**答**：
- 原生 use(promise)：需要自己管 promise 的创建/缓存/失效（React Cache 或自建 Map），胜在零依赖、语义纯净。
- useSuspenseQuery：缓存、去重、失效、重试、分页全部内建，与 Query 缓存体系（invalidate、乐观更新）联动。
- 组合实践：用 Query 管「缓存与失效」，useSuspenseQuery 作为渲染接口——业务里大多数团队选这个组合。
- 纯 Server 架构（RSC 直接取数）：不需要 Query，use/props 数据流即可。
- 判据：客户端缓存需求复杂度决定要不要引入 Query；渲染等待机制两者都走 Suspense。
