---
title: [RBL-003] Rspack 与 webpack 的兼容边界在哪里？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-003：Rspack 与 webpack 的兼容边界在哪里？
**答**：
- 高兼容区：配置项主体（entry/output/resolve/module.rules/optimization）、主流 loader（babel-loader、css-loader、less/sass-loader）、大多数 hook 语义一致的插件 API 子集。
- 部分兼容区：webpack 插件 API 只实现了高频子集（约 80% 语义覆盖但非全量），tapable 钩子的部分阶段（如某些 stage 参数）行为可能有差异；依赖 compiler 内部私有字段的插件基本不可用。
- 不兼容区：依赖 webpack 内部对象结构（Module/Chunk 私有字段）、重度依赖动态 require 运行时改写、部分冷门 loader 生命周期（pitch 的高级用法需验证）。
- 官方策略：优先用 @rspack/core 内置能力（内置 swc-loader、内置 css/chunk 图优化）替代社区插件，把"必须用 webpack 插件"的场景收敛到最少再评估迁移。
- 实战判定法：跑官方 compatibility 工具 + `rspack build` 直接试编译，收集 warning 中列出的不支持的插件/钩子，逐个找替代方案。
- 追问钩子： webpack-dev-server 与 rspack 的关系——用 @rspack/dev-server（基于 webpack-dev-server fork）。

```javascript
// rspack.config.js：与 webpack 配置高度同构，可直接平移大部分字段
module.exports = {
  entry: './src/index.ts',
  output: { filename: '[name].[contenthash:8].js', clean: true },
  resolve: { extensions: ['.ts', '.tsx', '...'], alias: { '@': './src' } },
  module: {
    rules: [
      { test: /\.tsx?$/, use: 'builtin:swc-loader', exclude: /node_modules/ },
      // builtin:swc-loader = 内置 Rust 实现，替代 babel-loader，零 FFI 开销
      { test: /\.css$/, type: 'css' }, // 内置 CSS 支持，替代 css-loader+mini-css
    ],
  },
  plugins: [], // webpack 插件需逐一确认是否在支持列表内
};
```
