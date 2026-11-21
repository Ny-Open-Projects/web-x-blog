---
title: [V3-360] defineAsyncComponent 与 Suspense 怎么选？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-360：defineAsyncComponent 与 Suspense 怎么选？
**答**：
- defineAsyncComponent：解决「chunk 懒加载」的局部占位，loading/error/delay/timeout 配置齐全，适用于小组件级（弹窗内容、图表组件）。
- Suspense：管理「setup 内异步依赖」（await 数据），粒度是组件树的异步边界，适合数据驱动的新旧 UI 切换。
- 二者可嵌套：异步组件内部有异步数据时，外层 defineAsyncComponent 管 chunk、内部 Suspense 管数据，各自 fallback。
- 选择口诀：代码分割问题 → defineAsyncComponent；数据加载编排问题 → Suspense + 数据层。
- 注意 defineAsyncComponent 的 error 回调只管「加载失败」，数据错误仍要走组件内部/Suspense 错误通道。
