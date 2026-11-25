---
title: [BLD-219] Chunk 命名与长缓存策略怎么设计？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-219：Chunk 命名与长缓存怎么设计？
**答**：
- 命名策略：`[name].[contenthash].js`——内容 hash 是缓存命中的根基；chunk 名稳定性（同一路由每次构建同名——rollup 的 chunk 名由模块路径推导，动态 import 名由 chunkName 注释）。
- hash 粒度问题：一个模块变更导致引用它的所有 chunk hash 变化——「共享 chunk 的引用传染」；缓解：稳定模块 ID（deterministic module ids，不用自增数字——自增 ID 因插入顺序变化导致全部 chunk 变化）。
- runtime chunk 单独提取（runtime 的 chunk 加载器变更频率最低——单独缓存）。
- 命名可读性：线上排障时 chunk 名可定位（routes/checkout.js 优于 3.async.js）。
- 追问钩子：为什么「自增模块 ID」是长缓存的隐形杀手——webpack 默认按发现顺序给模块编号，新增一个 import 后所有后续模块 ID 平移，引用它们的 chunk 全部内容变化（hash 全变）；deterministic ID（基于路径 hash）让 ID 与发现顺序无关——这是缓存命中率的关键开关。

```javascript
output: {
  filename: '[name].[contenthash:8].js',
  chunkFilename: 'chunks/[name]-[contenthash:8].js',
},
optimization: {
  moduleIds: 'deterministic',                        // 稳定 ID（长缓存关键）
  runtimeChunk: 'single',                            // runtime 单独缓存
}
```
