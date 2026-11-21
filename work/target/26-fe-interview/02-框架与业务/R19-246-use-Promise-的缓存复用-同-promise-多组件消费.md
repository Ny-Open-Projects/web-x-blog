---
title: [R19-246] 同一个 Promise 被多个组件 use 会怎样？如何避免重复请求？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-246：同一个 Promise 被多个组件 use 会怎样？
**答**：
- use 只消费 promise 对象本身：多个组件 use 同一 promise，resolve 时大家同时拿到数据——天然共享。
- 重复请求的根源是「每次渲染创建新 promise」，不是 use 本身：解决靠缓存 promise（key → promise Map、React Cache、TanStack Query）。
- 实践：promise 在父组件/模块级创建一次传下去；或用 React 的 cache() 包请求函数实现请求级记忆化。
- 失败共享：promise reject 后所有消费组件同时进入错误态，错误边界粒度要提前设计（多组件共用失败域）。
- 注意：promise 缓存要有 TTL/失效策略，否则「服务端确认后」数据陈旧——配合 revalidate 手段。
