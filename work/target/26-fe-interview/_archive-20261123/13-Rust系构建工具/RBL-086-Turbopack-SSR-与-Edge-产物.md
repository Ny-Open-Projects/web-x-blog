---
title: [RBL-087] Turbopack 如何支撑 Next.js 的 SSR 与 Edge 运行时产物？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-087：Turbopack 如何支撑 Next.js 的 SSR 与 Edge 运行时产物？
**答**：
- 多 target 输出：Next 应用同时需要 client bundle（浏览器）、server bundle（Node SSR/RSC）、edge bundle（轻量隔离运行时），Turbopack 以"环境（environment）"为一等概念，同一模块在不同 target 下可以有不同编译结果（条件导出、polyfill 差异）。
- RSC 拆分：server/client 组件边界由编译器静态识别（'use client' 指令），client 引用 server 组件时生成占位引用——这类框架语义内建在 Turbopack 任务里。
- Edge 产物约束：单文件 bundle、无 node 原生模块、体积受限——Turbopack 为 edge target 走独立打包策略。
- 增量收益：SSR 场景下 server bundle 的重建同样享受函数级增量，改一行页面代码 server 侧重编也快。
- 通用打包器对比：webpack/rollup 都没有把"多运行时 target + RSC 边界"内建，都是靠框架层插件硬凑——这是 Turbopack 差异化的根本。
- 追问钩子：'use client' 边界的产物含义：server 侧输出 client 组件的引用 chunk，client 侧输出组件实现。

```text
同一 Button.tsx 在三个 target 下的产物
client : 浏览器 bundle（含交互实现 + hydration）
server : RSC payload 渲染用（无 DOM 代码，或作为引用占位）
edge   : 单文件 bundle（无 node API，体积受限）
'use client' 边界：编译期切分，server bundle 里是引用 token
```
