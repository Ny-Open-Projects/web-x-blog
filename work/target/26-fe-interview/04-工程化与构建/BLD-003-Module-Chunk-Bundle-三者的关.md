---
title: [BLD-003] Module、Chunk、Bundle 三者的关系是什么？举例说清。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-003：Module、Chunk、Bundle 三者的关系是什么？举例说清。
**答**：
- Module 是编译的基本单位：每个被 webpack 处理的文件（js/css/图片，经 loader 转换后）都是一个 module，通过依赖关系组成模块图。
- Chunk 是打包过程的中间产物：由一组 module 依据 entry、splitChunks、动态 import 规则组装成，是"分块策略"的结果。
- Bundle（asset）是最终输出文件：每个 chunk 经过代码生成写出 1 个或多个 bundle（chunk 本体 + 可选的 css/图片副产物）。
- 举例：entryA 有 3 个模块（a + shared + 动态 import 的 lazy），entryB 有 2 个模块（b + shared）→ modules 共 4 个，chunks 有 4 个（entryA、entryB、async、common），bundle 输出 4 个 js。
- 面试追问点：一个 chunk 可以对应多个 asset（js + css），async chunk 不会阻塞首屏。

```javascript
// webpack.config.js：对应上述例子的完整可运行配置
const path = require('path');

module.exports = {
  mode: 'production',
  entry: {
    entryA: path.resolve(__dirname, 'src/pages/a.js'),
    entryB: path.resolve(__dirname, 'src/pages/b.js'),
  },
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name].[contenthash:8].js',
    chunkFilename: 'chunk.[name].[contenthash:8].js',
  },
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        common: { name: 'common', test: /[\\/]src[\\/]shared[\\/]/, minChunks: 2, priority: 10 },
      },
    },
  },
};

// 文件结构与结果对照：
// src/pages/a.js      -> import shared util, 动态 import('./lazy.js')   （module a + shared + lazy）
// src/pages/b.js      -> import shared util                             （module b + shared）
// 结果：modules = 4，chunks = entryA/entryB/lazy/common，bundles = 4 个 js 文件
```
