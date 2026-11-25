---
title: [FRP-258] 用自定义 reconciler 渲染终端 UI 的原理（react-ink 模式）？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-258：react-ink 模式的自定义渲染原理？
**答**：
- react-reconciler 包允许提供自定义 host config：createInstance/appendChild/commitUpdate 接到任意后端——终端（ANSI 文本）、Canvas、Three.js、Figma。
- React 核心管线（hooks/并发/调度）全保留，只换「DOM 操作层」——这是 VDOM 中间表示的最大红利。
- 实现要点：host context、文本节点处理、commit 阶段的批处理、尺寸测量（终端行高）。
- 类似生态：react-three-fiber（Canvas）、react-pdf、ink（终端）。
- 面试表达：「reconciler 与 host 分离」让 React 成为「UI 逻辑内核」而非「DOM 框架」。
