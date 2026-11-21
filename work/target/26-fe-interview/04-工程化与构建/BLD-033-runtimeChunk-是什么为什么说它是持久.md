---
title: [BLD-033] runtimeChunk 是什么？为什么说它是持久缓存的关键？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-033：runtimeChunk 是什么？为什么说它是持久缓存的关键？
**答**：
- runtime 是 webpack 的模块加载与 chunk 调度代码（__webpack_require__、jsonp 加载、HMR），默认内联在每个 entry chunk 里。
- 问题：runtime 里记录了"chunk id → 文件名（含 contenthash）"映射，任何业务 chunk 变化都会让 entry 的 runtime 变化 → entry contenthash 变化 → 缓存全失效。
- 把 runtime 单独抽成 runtimeChunk 后，业务改动不再触碰 runtime 文件与 vendor 文件，只失效变化的小 chunk，大部分缓存命中。
- 参数：true（每个 entry 一个）、'single'（全页面共用一个）、{ name }；一般配合 SplitChunks 的 deterministic module ids 使用。

```javascript
// webpack.config.js：长效缓存三板斧（runtimeChunk + contenthash + deterministic ids）
module.exports = {
  output: {
    filename: 'js/[name].[contenthash:8].js',
    chunkFilename: 'js/[name].[contenthash:8].chunk.js',
  },
  optimization: {
    runtimeChunk: { name: (entrypoint) => `runtime-${entrypoint.name}` },
    moduleIds: 'deterministic',  // 模块 id 稳定 不受依赖增减扰动
    chunkIds: 'deterministic',
    splitChunks: { chunks: 'all', cacheGroups: { vendors: { test: /[\\/]node_modules/, name: 'vendors' } } },
  },
};

// text 代码块：效果对照
// 未抽 runtime：改一行业务代码 -> main.js hash 变 -> 用户全量重新下载
// 抽出 runtime：改一行业务代码 -> 仅 main.js 变，runtime.js / vendors.js hash 不变 -> 命中强缓存
```
