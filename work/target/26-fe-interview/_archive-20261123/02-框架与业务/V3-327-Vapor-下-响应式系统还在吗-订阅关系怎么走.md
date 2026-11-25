---
title: [V3-327] Vapor 模式下响应式系统还在吗？订阅关系怎么走？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-327：Vapor 模式下响应式系统还在吗？订阅关系怎么走？
**答**：
- 完整保留：reactive/ref/computed/watch 全部照旧，Vapor 只是换掉了「订阅者末端」——从 render+patch 换成编译期生成的 DOM 更新函数。
- 链路：数据 ref → 依赖链表 → 细粒度更新 effect（如 setText 的表达式）→ 直接 DOM 写。更新粒度是「动态点」级别。
- 组件级更新仍存在：props 变化、事件冒泡、父传子的协议层更新与 VDOM 模式一致。
- 这正是 Vapor 与 Solid/Svelte 的共同点：响应式直达 DOM；Vue 的差异是模板编译器在编译期自动生成这些细粒度订阅，开发者无感。
- 心智变化：不再能依赖「整树重渲染」的兜底行为，所有更新都是定向的，调试时按动态点排查。
