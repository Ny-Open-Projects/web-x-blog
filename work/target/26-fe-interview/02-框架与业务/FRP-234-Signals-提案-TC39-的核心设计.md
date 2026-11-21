---
title: [FRP-234] TC39 Signals 提案的核心设计是什么？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-234：TC39 Signals 提案的核心设计？
**答**：
- 目标：把「细粒度响应式」标准化为 JS 语言原语（Signal.State 可写信号、Signal.Computed 计算信号、Signal.effect/subscribe）。
- 核心语义：自动依赖追踪、惰性求值（computed 不被读就不算）、去重传播（同一次批量内只算一次）、循环检测报错。
- 意义：框架响应式内核可能收敛到统一原语——Vue/Solid/Svelte 的 signal 实现可共享标准（当前各家 API 语义已趋同）。
- 现状：Stage 1（早期），polyfill 可玩（@preact/signals 兼容语义）。
- 面试表达：它是「响应式界的 Promise 标准化时刻」——若落地，框架差异收敛到渲染层。
