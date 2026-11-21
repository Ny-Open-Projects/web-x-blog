---
title: [FRP-236] MobX 与 Vue 响应式的异同？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-236：MobX 与 Vue 响应式异同？
**答**：
- 同：自动依赖追踪（observable/computed）、行动后自动通知、原子化可组合。
- 异：MobX 是「库」与 React 配合（observer 高阶组件包裹，粒度组件级，内部细粒度但通知到组件重渲染）；Vue 是「框架内建」，粒度直达组件 render 与 DOM。
- 事务机制：MobX 有 transaction 批处理；Vue 用调度队列（nextTick 批量）。
- 数据可变性：两者都是 mutable 优先（对比 Redux 不可变流）。
- React + MobX 的组合本质：把细粒度响应式嫁接到 VDOM 框架上——observer 决定「要不要 render」，render 内仍是 VDOM diff。
