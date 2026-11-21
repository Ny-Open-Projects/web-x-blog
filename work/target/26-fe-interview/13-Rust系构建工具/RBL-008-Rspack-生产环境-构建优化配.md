---
title: [RBL-008] Rspack 生产环境构建有哪些关键配置？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-008：Rspack 生产环境构建有哪些关键配置？
**答**：
- 压缩：默认 mode: production 用内置 swc 压缩 JS/CSS，不需要 TerserPlugin/CssMinimizerPlugin；要自定义走 optimization.minimizer。
- 代码分割：optimization.splitChunks 配置与 webpack 同构，配合 splitChunks.chunks: 'all' 抽公共依赖；动态 import 天然切 chunk。
- 内容哈希与长效缓存：output.filename 用 [contenthash]，Rspack 保证同 webpack 语义，配合稳定 moduleIds/chunkIds（默认 deterministic）保证发版缓存命中。
- Scope hoisting：生产默认开启模块串联优化，与 webpack 的 ModuleConcatenationPlugin 语义对齐。
- 产物分析：用 bundle-stats / rspack 内置 stats.toJson() 做体积分析，替代 webpack-bundle-analyzer（有社区适配版）。
- 追问钩子：source map 选择——生产用 hidden-source-map 传监控平台，避免泄露源码。

```javascript
// rspack.config.js（生产关键项）
const rspack = require('@rspack/core');
module.exports = (env) => ({
  mode: 'production',
  entry: { app: './src/index.ts' },
  output: {
    path: '/dist',
    filename: 'js/[name].[contenthash:8].js',
    cssFilename: 'css/[name].[contenthash:8].css',
    clean: true,
  },
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: { test: /[\\/]node_modules[\\/]/, name: 'vendor', priority: 10 },
      },
    },
    runtimeChunk: 'single',
    // minimizer 默认内置 swc，无需配置
  },
  devtool: 'hidden-source-map',
});
```
