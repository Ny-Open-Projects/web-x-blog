---
title: [FRP-223] Solid 的细粒度更新在编译期做了什么？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-223：Solid 细粒度更新在编译期做了什么？
**答**：
- JSX 中的表达式被提取为独立 getter：`<div>{count()}</div>` 编译为 insert(el, () => count())——表达式成为订阅单元。
- 组件函数体只执行一次：JSX 不是每次渲染重建，而是「一次构建 DOM + 声明订阅」。
- Props 访问 getter 化：传递 props.count 实际是 getter 调用（解构会丢响应——Solid 特有坑）。
- 控制流编译为专用组件（Show/For），比 VDOM 条件渲染更精准（For 内部 key 化复用）。
- 与 Vue Vapor 的异同：同为编译期细粒度；Solid 用户显式函数调用，Vue 模板隐式。
