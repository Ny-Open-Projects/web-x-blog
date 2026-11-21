---
title: [BLD-099] 前端构建的未来趋势是什么？bundleless、Rust 化工具链全景怎么看？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-099：前端构建的未来趋势是什么？bundleless、Rust 化工具链全景怎么看？
**答**：
- bundleless dev 成主流：dev 不打包（Vite 开创），Turbopack/Rspack 把"打包也增量到函数级"——本质都是把编译开销摊到按需与增量。
- Rust 化全景：SWC（babel 位）、Rspack（webpack 位）、lightningcss（postcss 位）、Rolldown（Rust 版 Rollup，Vite 的未来底座）、Turbopack（next 位）——JS 工具层逐步下沉为"内核 Rust + 胶水 JS 插件"。
- 概念收敛：bundler/framework/monorepo 工具（Vite+Rolldown、Next+Turbopack、Rspack+Rsbuild+NX）彼此渗透，"选构建器"逐渐变成"选框架全家桶"。
- 对工程师的要求变化：从"会写 webpack 配置"转向"会读产物、会定预算、会写插件（JS 层）与理解底层管线"。

```mermaid
flowchart TD
  A["JS 工具链现状"] --> B["Babel babel-loader"] --> B1["SWC Rust 化"]
  A --> C["webpack"] --> C1["Rspack Turbopack Rust 化"]
  A --> D["Rollup"] --> D1["Rolldown Rust 化"]
  A --> E["postcss cssnano"] --> E1["lightningcss Rust 化"]
  A --> F["terser"] --> F1["esbuild minify SWC minify"]
  B1 --> G["统一形态 内核 Rust 加 JS 胶水插件"]
  C1 --> G
  D1 --> G
  E1 --> G
  F1 --> G
  G --> H["开发者价值 转向 产物治理 插件开发 性能预算"]
```
