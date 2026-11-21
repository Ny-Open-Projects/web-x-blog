---
title: [RBL-009] 为什么 Rspack 选择兼容 webpack 而不是另起炉灶？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-009：为什么 Rspack 选择兼容 webpack 而不是另起炉灶？
**答**：
- 生态资产：webpack 生态十年沉淀了海量 loader/plugin 和业务配置，全部重写成本极高；兼容意味着存量项目可以渐进迁移，而不是推倒重来。
- 迁移成本是采用率的决定因素：字节内部数千个 webpack 项目，"改个 import 就能提速"比"重写配置+重写插件"的 ROI 高得多，这是 Rspack 产品定位的核心。
- 差异化空间：兼容子集策略保留了大改内核的自由——不需要为全量 tapable 兼容买单，可以在 Rust 里重新设计模块图、缓存、并行调度。
- 与 esbuild/Vite 路线对比：esbuild 是"快但不做完整生态"（作者明确不做 plugin 长尾），Rspack 是"快 + 尽量兼容存量"，面向的是已有大型 webpack 应用的团队。
- 代价：兼容层约束了架构演进速度，webpack 语义里历史包袱（如 javascript/auto 的动态 require）也要背着。
- 追问钩子：Rspack 团队与 Rolldown 团队后来合并推进统一路线，两者分别对应 webpack 系与 rollup 系的存量迁移。

```javascript
// 迁移成本对比（示意）
// 路线 A：webpack → Rspack
//   改 package.json + 引 rspack.config.js（大部分字段平移）+ 验证插件替代 ≈ 数人日~数人周
// 路线 B：webpack → 全新工具（如 esbuild 自建管线）
//   重写所有 loader/plugin 语义 + 验证存量边界行为 ≈ 数人月，且持续维护双轨
console.log('兼容 = 生态复用；重写 = 生态清零。存量项目多的团队选前者。');
```
