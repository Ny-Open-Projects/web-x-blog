---
title: [BLD-054] hash、chunkhash、contenthash 的区别？（高频）
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-054：hash、chunkhash、contenthash 的区别？（高频）
**答**：
- hash：整个构建的哈希，任何一个文件变全变——已不适合缓存场景。
- chunkhash：按 chunk 计算，同 chunk 内模块变化影响该 chunk；但 chunk 依赖变化（如入口引了新异步 chunk）也会变。
- contenthash：按"文件内容本身"计算，css 与 js 解耦——js 改动不影响抽出的 css 文件名，是长效缓存正确姿势。
- 组合实践：js 用 contenthash，css（mini-css-extract）用 contenthash，runtime 单独抽；同时配 moduleIds: 'deterministic' 防止 id 扰动。
- 坑：WebpackManifestPlugin 引用文件名要同步读取 stats 映射，别手拼 hash。

```javascript
// webpack.config.js：三类 hash 对比与推荐配置
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  output: {
    // 推荐 contenthash：内容定文件名
    filename: 'js/[name].[contenthash:8].js',
    chunkFilename: 'js/[name].[contenthash:8].chunk.js',
  },
  optimization: {
    runtimeChunk: 'single',
    moduleIds: 'deterministic', // 配合 contenthash 缓存才稳
  },
  module: {
    rules: [{
      test: /\.css$/,
      use: [MiniCssExtractPlugin.loader, 'css-loader'],
    }],
  },
  plugins: [
    new MiniCssExtractPlugin({
      // css 用 contenthash：js 逻辑变化不影响 css 缓存
      filename: 'css/[name].[contenthash:8].css',
    }),
  ],
};

// text 代码块：三者的变化粒度示意
// hash:        改任何文件 -> 所有文件名全变（整站缓存失效）
// chunkhash:   改入口依赖的模块 -> 该入口及其子 chunk 变
// contenthash: 改 css -> 只有 css 文件名变；改 js -> 只有 js 文件名变
```
