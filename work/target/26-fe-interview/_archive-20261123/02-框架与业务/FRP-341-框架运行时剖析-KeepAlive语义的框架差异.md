---
title: [FRP-341] 框架运行时剖析：KeepAlive/状态保留语义的框架差异
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 面试题, 架构]
type: 面试题
---

## FRP-341：框架运行时剖析：KeepAlive/状态保留语义的框架差异

**答**：
- 三框架的状态保留原语：Vue KeepAlive（内置组件，缓存 vnode+DOM）、React（无官方原语——Activity API 实验中；社区方案 display:none 或卸载存 store）、Solid（Show + 状态外提）
- 语义差异点：React 的「保留」必须把状态外提（提升到不卸载的父级/store）——组件实例本身不保留；Vue 保留组件实例（activated 钩子）
- 对业务的影响：React 方案「状态在 store」天然跨页面一致；Vue KeepAlive「实例内状态」滚动位置等 DOM 态也保留——各自适合的场景
- 生态缺口：React 社区的 react-activation 等方案 hack fiber（风险高）——Activity API 落地前的过渡
- 迁移注意：从 Vue 迁 React 时「KeepAlive 依赖」要重构为状态外提——架构级改动点

```text
状态保留光谱:
  Vue KeepAlive:  实例+DOM 保留 (activated/deactivated)
  React Activity: 状态保留 + effect 暂停 (实验中)
  React 现状:     状态外提到 store + 卸载组件
迁移: Vue KeepAlive → React 时, 实例态上提 store
```
