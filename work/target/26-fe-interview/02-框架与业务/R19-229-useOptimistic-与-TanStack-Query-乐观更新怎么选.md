---
title: [R19-229] useOptimistic 与 TanStack Query 的乐观更新怎么选？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-229：useOptimistic 与 TanStack Query 的乐观更新怎么选？
**答**：
- useOptimistic：React 19 原生，与 action 生命周期绑定（onSettled 自动清队列），适合「提交型操作」（表单、点赞），零依赖。
- TanStack Query onMutate：缓存级乐观更新（直接改 query cache），回滚靠返回的 prev 数据 snapshot，适合「读-改-写」的数据缓存体系（列表内编辑）。
- 选型：全 action + Server State 架构（Next App Router）→ useOptimistic；客户端数据缓存架构（SPA + Query）→ onMutate。
- 两者可共存：Query 管列表缓存，提交动作用 action + useOptimistic，成功后 invalidate 对应 query。
- 判据一句话：乐观更新的「回滚真相」在哪一层维护，就用哪一层的方案。
