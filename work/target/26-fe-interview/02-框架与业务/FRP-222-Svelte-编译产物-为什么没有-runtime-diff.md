---
title: [FRP-222] Svelte 的编译产物为什么没有 runtime diff？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-222：Svelte 编译产物为什么没有 runtime diff？
**答**：
- 编译期已知每个插值的位置与依赖：产物生成「脏标记 + 直接 DOM 写」的更新函数（`p(ctx, dirty)`），哪条表达式依赖哪个变量是静态事实。
- 更新 = set dirty 位 → 按位执行对应 DOM 写——没有 vnode、没有 diff、没有调度器（更新同步执行或微任务批处理）。
- 代价：动态结构（if/each）也要编译成专用块（block 树，切换成本低但灵活性差）；运行时无法处理「编译期未知」的结构变化。
- 与 Vue 对比：Vue 保留 VDOM 兜底动态性，Svelte 用编译期确定性换取零 diff——Svelte 5 加回信号系统补动态性。
