---
title: [ENG-019] webpack 构建速度慢，如何优化？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-019：webpack 构建速度慢，如何优化？
**答**：
- 持久化缓存 cache.type: 'filesystem'，二次构建直接复用缓存，提升最明显。
- 缩小 loader 处理范围：include/exclude 限定 src，babel-loader 开 cacheDirectory。
- resolve.extensions 少配通配后缀，减少解析尝试；alias 指明常见路径。
- 项目过大考虑拆构建或换 Rsbuild/Rspack（Rust 实现的高兼容替代）。

```javascript
const path = require('path');

module.exports = {
  cache: {
    type: 'filesystem', // 持久化缓存
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        include: path.resolve('src'), // 缩小处理范围
        loader: 'babel-loader',
        options: { cacheDirectory: true },
      },
    ],
  },
  resolve: {
    // 后缀列表越短，解析尝试越少
    extensions: ['.js', '.ts', '.jsx'],
    alias: { '@': path.resolve('src') },
  },
};
```
