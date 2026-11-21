---
title: [RBL-088] Turbopack 与 Rspack 该怎么选？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-088：Turbopack 与 Rspack 该怎么选？
**答**：
- 按框架绑定选：Next.js 项目 → Turbopack（官方路线，深度集成 RSC/App Router）；其他 React/Vue/自研架构项目 → Rspack（webpack 兼容，通用）。
- 按存量生态选：重度 webpack 插件/loader 资产 → Rspack（兼容层）；愿意为 dev 极致速度放弃通用插件 → Turbopack。
- 架构差异一句话：Rspack = "快版 webpack"（模块级增量 + webpack 语义），Turbopack = "函数级增量 + 框架专用"（不做 webpack 兼容）。
- 团队成本：Rspack 迁移主要是配置/插件改造；Turbopack 迁移前提是"项目本来就在 Next 上"。
- 演进趋势：两者都由 Rust 内核 + 官方框架深度绑定路线发展；Turbopack 也在把 next build（生产）纳入。
- 追问钩子：面试可以给个决策树——Next?→Turbopack；webpack 存量?→Rspack；全新项目无包袱?→看团队 Rust 工具链熟悉度与框架选择。

```text
决策树
Next.js 项目？
├─ 是 → Turbopack（next dev --turbo，逐步覆盖 build）
└─ 否 → 有 webpack 存量资产？
     ├─ 是 → Rspack（兼容迁移）
     └─ 否 → 新项目：按框架选（Vite→rolldown-vite / Rsbuild / Turbopack）
```
