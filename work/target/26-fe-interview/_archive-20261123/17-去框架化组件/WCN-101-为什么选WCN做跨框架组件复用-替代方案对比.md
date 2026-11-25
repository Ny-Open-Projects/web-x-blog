---
title: [WCN-101] 为什么用 WCN（Web Components）做跨框架组件复用？各替代方案对比如何？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 跨框架复用]
type: 面试题
---

## WCN-101：为什么用 WCN（Web Components）做跨框架组件复用？各替代方案对比如何？

**答**：
- 方案 A：多框架源码维护（同一组件写 React/Vue 两份）——成本最高、易失同步。
- 方案 B：源码级转换（vue-sfc → react、Mitosis/ teleport）——编译假设不完全、调试困难，只适合简单组件。
- 方案 C：微前端整页集成——粒度太粗、运行时开销大。
- 方案 D：WCN——写一次，浏览器原生消费；React/Vue/Svelte/原生都能直接用 `<x-card>`；样式 Shadow DOM 隔离；SSR 可用 DSD。
- WCN 的成本：状态管理要自建或用 Signals；与宿主框架的数据流要靠 attribute/property/事件桥接；调试影子树需要适配工具。
- 判断标准：组件受众跨 ≥2 个技术栈或要在"无框架区域"（营销页、低代码画布）使用 → WCN 收益显著；单一 React 项目内 → 直接写 React 更顺手。

```html
<!-- 同一组件，三种宿主零改动 -->
<user-card user-id="42"></user-card>            <!-- 原生 HTML -->
<user-card :user-id="uid"></user-card>          <!-- Vue -->
<user-card userId={uid} />                      <!-- React 19（属性自动映射 property） -->
```
