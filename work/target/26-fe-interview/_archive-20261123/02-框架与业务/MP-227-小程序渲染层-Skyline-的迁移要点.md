---
title: [MP-227] 渲染层 Skyline 迁移的要点与兼容性？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-227：Skyline 渲染迁移要点？
**答**：
- Skyline：自研渲染引擎（非 WebView），更快的渲染管线、原生级别的滚动/手势、worklet 动画。
- 迁移成本：CSS 子集支持（部分选择器/布局差异）、组件差异（部分组件行为不同）、需 app.json 配置 rendererOptions 与 lazyCodeLoading。
- 收益场景：复杂动画页、超长列表、高频手势交互——WebView 引擎瓶颈页。
- 灰度策略：新页面 Skyline、存量页面 WebView，按页面配置 renderer；双端回归测试矩阵（iOS/Android/版本）。
- 风险： Skyline 与部分三方 SDK（依赖 WebView 特性）不兼容——接 SDK 前查支持矩阵。
