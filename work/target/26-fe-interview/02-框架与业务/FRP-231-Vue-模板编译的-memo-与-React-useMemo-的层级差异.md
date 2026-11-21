---
title: [FRP-231] Vue 的 v-memo 与 React useMemo 的层级差异？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-231：Vue 的 v-memo 与 React useMemo 的层级差异？
**答**：
- v-memo：作用于 vnode 子树——依赖数组不变时整个子树 vnode 直接复用（连 vnode 对象都不重建），diff 完全跳过。
- React useMemo(() => <Rows/>, [deps])：缓存 JSX 引用，React 仍会 reconcile（比较引用相同则跳过子树——需配合 memo 组件才完全跳过）。
- 粒度：v-memo 是编译期插入的 withMemo 调用，可靠性由编译器保证；useMemo 是运行时人工依赖，漏依赖即 bug。
- 场景：大列表 v-for + v-memo（只更新变化行）是 Vue 列表优化的王牌。
- React 对应物是 Compiler 自动 memo（元素级），趋同但机制不同。
