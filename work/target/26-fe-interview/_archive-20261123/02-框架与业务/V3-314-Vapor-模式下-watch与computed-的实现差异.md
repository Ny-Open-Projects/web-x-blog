---
title: [V3-314] Vapor 模式下 watch 与 computed 的实现和 VDOM 模式有何差异？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-314：Vapor 模式下 watch 与 computed 的实现和 VDOM 模式有何差异？
**答**：
- 响应式内核完全复用：reactive/ref/computed 仍是同一套（3.5 链表依赖），Vapor 改的是「订阅者如何更新 DOM」这一层。
- VDOM 模式订阅者是「重新执行 render 函数 → 生成新 vnode → patch」；Vapor 订阅者是编译期生成的细粒度 DOM 更新函数（setText 里的表达式）。
- watch 语义不变，但 Vapor 组件销毁走的是 Vapor 实例的 scope，watch 自动归入组件作用域，无需 onUnmounted。
- computed 的脏检查在 Vapor 下收益更大：细粒度更新链路短，computed 缓存命中直接省一次 DOM 写。
- 结论：逻辑代码（store、composable）无需为 Vapor 改写，只有模板编译层不同。
