---
title: [RBL-014] Rspack 的代码分割能力与 webpack 有何异同？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-014：Rspack 的代码分割能力与 webpack 有何异同？
**答**：
- 三种分割来源一致：多 entry 手动分割、optimization.splitChunks 公共块提取、动态 import() 天然异步 chunk，语义与 webpack 对齐。
- splitChunks 配置项（chunks/minSize/maxSize/cacheGroups/priority/reuseExistingChunk）基本同构，迁移时通常可原样复制。
- 差异点：个别高级字段支持不完整（如部分 automaticGroupName 语义），需要以实际产物为准做 diff；Rspack 内置 chunk 图算法在 Rust 中实现，分割计算本身更快。
- 长效缓存友好性：默认 deterministic 的 moduleIds/chunkIds，配合 contenthash，公共依赖不变时 vendor hash 稳定——这点与 webpack 5 一致。
- 实战分组模板：node_modules 抽 vendor、业务公共（被 2 个以上入口共享）抽 common、runtime 单独抽出。
- 追问钩子：过度分割会放大请求数，配合 HTTP/2 并发与 preload 策略权衡。

```javascript
// rspack.config.js
module.exports = {
  optimization: {
    runtimeChunk: 'single',
    splitChunks: {
      chunks: 'all',
      minSize: 20000,
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendor', priority: 10, enforce: true,
        },
        common: {
          minChunks: 2, name: 'common', priority: 5, reuseExistingChunk: true,
        },
      },
    },
  },
};
// 动态 import 按路由分割
// const Page = React.lazy(() => import('./pages/Detail')); // 独立 chunk
```
