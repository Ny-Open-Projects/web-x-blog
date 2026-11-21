---
title: [BLD-085] Turbopack 是什么？定位与现状如何？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-085：Turbopack 是什么？定位与现状如何？
**答**：
- Turbopack：Vercel 出品的 Rust 增量打包器，定位 webpack 的继任者（作者 Tobias Koppers 主导），深度绑定 Next.js 生态。
- 核心技术点：函数级增量计算引擎（Turbopack 内部的"任务图"缓存细粒度函数结果）、Rust 并行、按需打包（只编译被请求的部分，融合 dev 不打包与打包的思路）。
- 现状：dev 稳定用于 Next.js（`next dev --turbo`），build 支持逐步推进；不作为通用 CLI 输出独立生态。
- 与 Vite 路线差异：Vite dev 不打包 + Rollup 生产；Turbopack dev/prod 都是"细粒度增量打包"，目标把 webpack 的功能完整迁移。

```javascript
// next.config.js：Turbopack 配置（Next.js 15+）
/** @type {import('next').NextConfig} */
module.exports = {
  turbopack: {
    resolveAlias: {
      '@': './src',
      // 大库别名到浏览器友好版本
      lodash: 'lodash-es',
    },
    rules: {
      '*.svg': { loaders: ['@svgr/webpack'], as: '*.js' },
    },
  },
};

// bash 代码块：
// next dev --turbo     # dev 使用 Turbopack
// next build --turbo   # 生产构建（版本支持随 Next 演进）
```
