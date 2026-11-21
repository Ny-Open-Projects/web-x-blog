---
title: [FRP-225] Vue 的编译优化与 Svelte/Solid 的边界差异在哪？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-225：Vue 编译优化与 Svelte/Solid 的边界差异？
**答**：
- Vue：VDOM 保留为「动态性兜底」，patchFlag/block tree 只是裁剪 diff 范围——更新粒度仍是组件级 render 函数。
- Svelte/Solid：完全绕过 VDOM，订阅直达 DOM——粒度是表达式级。
- 原因：Vue 要兼容 render 函数/JSX/运行时模板等灵活场景；纯编译策略无法覆盖。
- 收敛趋势：Vue Vapor 模式补上「编译期直达 DOM」的能力（opt-in），证明两种模式可在同一框架共存。
- 判决式：动态性需求高 → Vue/React；静态模板为主 → 编译时框架收益更大。
