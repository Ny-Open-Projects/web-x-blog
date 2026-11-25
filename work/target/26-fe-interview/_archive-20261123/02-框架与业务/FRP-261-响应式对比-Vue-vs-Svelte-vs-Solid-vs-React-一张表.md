---
title: [FRP-261] 响应式对比总表：Vue vs Svelte vs Solid vs React？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-261：响应式对比总表：Vue vs Svelte vs Solid vs React？
**答**：
- Vue：Proxy 隐式收集 + 编译裁剪 diff，组件级 render + 表达式级 patchFlag，VDOM 兜底。
- Svelte 5：Runes 显式信号 + 编译期块更新，无 VDOM，一次执行组件。
- Solid：显式 signal + JSX getter 化，无 VDOM，一次执行，粒度最细。
- React：不可变状态 + 全树 reconcile，依赖人工 memo/Compiler，模型最简单。
- 维度表：依赖收集方式 / 更新粒度 / VDOM 有无 / 组件执行次数 / 心智负担——面试时画表逐格对比，结论「粒度与简单性的光谱」。
