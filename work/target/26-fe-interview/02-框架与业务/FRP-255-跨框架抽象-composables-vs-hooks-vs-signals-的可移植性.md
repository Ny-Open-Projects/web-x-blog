---
title: [FRP-255] 跨框架抽象：composables/hooks/signals 的可移植性对比？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-255：跨框架逻辑抽象的可移植性对比？
**答**：
- 可移植层：纯函数（校验/格式化）、schema（zod）、状态机（xstate）、领域模型——与框架无关，跨栈复用最安全。
- 半可移植：composables（Vue）与 hooks（React）结构相似但生命周期 API 不同——核心逻辑抽出（useRequest 的内核）可共享，UI 绑定层各写。
- 不可移植：signal 细粒度绑定（Solid）、模板编译相关优化。
- 实践：monorepo 中 packages/core（纯逻辑）+ packages/react + packages/vue 各自薄适配层。
- 面试表达：抽象层次越靠近领域模型越可移植，越靠近框架 API 越不可移植。
