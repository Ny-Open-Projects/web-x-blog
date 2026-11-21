---
title: [BLD-036] CSS 的分割与提取发生在什么时机？怎样避免样式被重复或丢失？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-036：CSS 的分割与提取发生在什么时机？怎样避免样式被重复或丢失？
**答**：
- 时机：mini-css-extract-plugin 在 compilation 的 processAssets（OPTIMIZE 阶段前）把 css-loader 收集的样式按 chunk 维度合并写出，同步更新 js 模块引用——即"代码生成后的产物优化阶段"。
- 分割规则：与 js splitChunks 一致，async chunk 对应的 css 单独成文件；splitChunks.cacheGroups 也能把公共 css 抽成 common.css。
- 重复：同一模块被多个 chunk 引用时依赖 reuseExistingChunk；丢失：css 被 tree-shake（sideEffects 未豁免 css）或 importLoaders 配错。
- 首屏关键 CSS 可以配合 CriticalCSS/inline 处理，其余异步 css 由 chunk 加载器自动 append link。

```javascript
// webpack.config.js：css 分割与公共样式抽取
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  module: {
    rules: [{
      test: /\.css$/,
      use: [MiniCssExtractPlugin.loader, 'css-loader'],
    }],
  },
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        styles: { // 抽公共样式：被 2 个以上 chunk 引用的 css
          name: 'styles-common',
          type: 'css/mini-extract',
          chunks: 'all',
          minChunks: 2,
          enforce: true, // 忽略 minSize 等限制 强制生效
        },
      },
    },
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: 'css/[name].[contenthash:8].css',
      chunkFilename: 'css/[id].[contenthash:8].css',
    }),
  ],
};
```
