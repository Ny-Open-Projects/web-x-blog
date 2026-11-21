---
title: [V3-351] 子组件「直接修改 props」的合法边界与反模式是什么？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-351：子组件「直接修改 props」的合法边界与反模式是什么？
**答**：
- 单向数据流原则：props 顶层赋值（`props.title = 'x'`）在 dev 下报错，反模式。
- 合法边界一：修改 props 内部嵌套对象属性（`props.row.status = 1`）技术上可行且不报错（Proxy 深层），但破坏数据流可预测性，仅限「该对象所有权明确归子组件」的受控场景。
- 合法边界二：defineModel 是官方的「双向例外」，编译为 prop + emit，语义清晰可追踪。
- 反模式：解构 props 后存本地 ref 又不完全同步，造成「父变子不变」的两份真相；正确做法是 computed 派生或 defineModel。
- 大型项目建议：ESLint vue/no-mutating-props 开到最严（含深层修改检测），双向场景一律 defineModel。
