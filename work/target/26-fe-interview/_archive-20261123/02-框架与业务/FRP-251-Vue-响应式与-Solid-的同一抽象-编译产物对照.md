---
title: [FRP-251] Vue 与 Solid 响应式的同一抽象：编译产物对照？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-251：Vue 与 Solid 响应式的同一抽象：编译产物对照？
**答**：
- 模板 `<span>{{count}}</span>`（Vue Vapor）与 JSX `<span>{count()}</span>`（Solid）产物形态一致：textContent 绑定一个 getter effect。
- 差异只在「依赖来源」：Vue 编译器从模板推导依赖，Solid 要求用户显式 signal。
- 因此「同一抽象」：signal/setter + effect 细粒度更新，框架差异收敛为「显式 vs 隐式」的 API 风格。
- 推论：TC39 Signals 若标准化，Vue/Solid/Svelte 内核可共享，框架竞争聚焦渲染与 DX 层。
- 面试亮点：用产物对照证明「实现路径不同、抽象终点相同」。
