---
title: [FRP-266] 各家 DX 细节：解构丢失响应式问题对照？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-266：解构丢失响应式的对照？
**答**：
- Vue reactive：解构丢响应（值快照）——需要 toRefs；props 解构 3.5 起编译期转换可保留。
- Solid props：解构丢 getter——需用 props.x 访问或 mergeProps。
- Svelte 5：$props() runes 解构保留响应（编译器处理）。
- React：无此问题（props 本身就是每渲染新值），但 hooks 闭包陷阱是等价痛点（exhaustive-deps 管控）。
- 共同教训：「值拷贝 vs 引用访问」的边界是响应式 DX 事故高发区——框架都在用编译器兜这个底。
