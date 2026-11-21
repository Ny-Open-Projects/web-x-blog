---
title: [V3-320] Vapor 与 VDOM 组件的混合渲染（interop）是怎么实现的？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-320：Vapor 与 VDOM 组件的混合渲染（interop）是怎么实现的？
**答**：
- 双向包装：VDOM 组件渲染 Vapor 子组件时，在 vnode 层生成一个占位组件，内部调 Vapor 组件的 setup 拿 DOM 并挂载；生命周期钩子桥接到 Vapor block。
- Vapor 组件渲染 VDOM 子组件时，为该子组件创建一个独立的 VDOM 渲染上下文（内部起一个 renderer 实例级作用域），把返回的根 vnode mount 到容器元素。
- props/事件传递走统一组件实例协议，两边共享同一套 props 响应式与 emits 触发机制。
- 限制：跨边界频繁高频更新会有转换开销；Suspense/Transition 跨边界的行为要按官方支持矩阵验证。
- 实践意义：让「按路由/按页面灰度迁移到 Vapor」成为可能，不必一次性切换。
