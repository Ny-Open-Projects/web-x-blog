---
title: [FRP-233] 响应式粒度光谱：从 Redux 到 Solid 的五档划分？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-233：响应式粒度的五档光谱？
**答**：
- L1 应用级：Redux/Flux——整 store 通知，组件按 mapStateToProps 订阅，粒度靠人工 memo。
- L2 store 级：Pinia/Vuex——store 维度响应，配合 computed 收窄。
- L3 字段级：MobX/Vue reactive——对象字段依赖收集，改 a 只触发读 a 的 effect。
- L4 表达式级：Vue Vapor/Svelte 5——编译期把表达式作为订阅单元，DOM 更新按表达式定位。
- L5 信号级：Solid/Preact signals——每个 signal 独立传播，计算图按需执行（lazy、可缓存）。
- 粒度越细，更新范围越小，但心智/依赖管理越自动化或越显式——光谱两端各有代价。
