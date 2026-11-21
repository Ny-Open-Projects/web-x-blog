---
title: [R19-252] Suspense 下的状态提升陷阱：为什么「数据进 Context」要谨慎？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-252：Suspense 下的状态提升陷阱：为什么「数据进 Context」要谨慎？
**答**：
- 把异步数据放 Context.value：provider 也要等数据（provider 内 use + Suspense），否则 value 初始为 null，消费组件全要 null 判断——Suspense 语义被破坏。
- 正确做法：数据以 promise/props 传递（声明式等待），或 provider 本身放 Suspense 边界内、value 就是数据（子组件假设非空）。
- 陷阱二：provider 在边界外、消费者在边界内——数据更新时 provider 重渲染把整个子树拖下水。
- 缓存型数据（用户信息、权限）适合 Context；动态业务数据适合 props/use。
- 口诀：Context 装「会话级稳定状态」，Suspense 管「请求级动态数据」，别交叉。
