---
title: [FRP-221] Svelte 5 的 Runes（$state/$derived/$effect）怎么重新设计编译时响应式？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-221：Svelte 5 的 Runes 怎么重新设计编译时响应式？
**答**：
- Svelte 4 是「隐式响应式」（顶层 let 自动响应），跨组件/动态场景歧义多；Runes 改为显式信号（$state/$derived/$effect）。
- $state：深响应代理（对象自动 proxy），编译产物是 signal getter/setter 调用。
- $derived：惰性求值 + 依赖自动追踪；$effect：显式声明副作用（替代旧 reactive 声明）。
- 组件函数只运行一次（同 Solid），更新走信号订阅而非组件重跑。
- 收益：显式化降低心智歧义 + 保留编译时体积优势 + 与 Solid/Signals 提案对齐（行业收敛）。
