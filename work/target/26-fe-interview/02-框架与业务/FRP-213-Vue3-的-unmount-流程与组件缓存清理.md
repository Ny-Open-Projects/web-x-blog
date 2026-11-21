---
title: [FRP-213] Vue3 的 unmount 流程与清理细节？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-213：Vue3 的 unmount 流程与清理细节？
**答**：
- 顺序：beforeUnmount 钩子 → 递归 unmount 子节点/子组件 → 指令 unmounted → 移除 DOM → unmounted 钩子。
- 组件卸载：停止组件 EffectScope（所有 watch/computed/自定义 effect 一起断链）、清 subscriptions（store 依赖）。
- KeepAlive 缓存卸载：不销毁实例，从缓存 Map 移除时才真正 unmount。
- Transition 卸载： leave 动画完成后才 remove DOM（delayed removal，框架内建）。
- 资源类：模板 ref 置 null、原生事件由编译产物清理（v-on 自动解绑）。
