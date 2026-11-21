---
title: [ENG-020] webpack 产物体积大，如何优化？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-020：webpack 产物体积大，如何优化？
**答**：
- 开启 tree-shaking：production mode + package.json 声明 sideEffects。
- splitChunks 抽离 node_modules 公共依赖，业务改动不影响 vendor 缓存。
- 用 webpack-bundle-analyzer 分析大模块，替换或按需引入重型依赖。
- 文件名带 contenthash + 长缓存策略，让用户增量加载而不是整包更新。

```javascript
const TerserPlugin = require('terser-webpack-plugin');
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

module.exports = {
  mode: 'production', // 内置 usedExports 与 tree shaking
  optimization: {
    minimize: true,
    minimizer: [new TerserPlugin()],
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendors: { test: /[\\/]node_modules[\\/]/, name: 'vendors', priority: -10 },
      },
    },
  },
  plugins: [new BundleAnalyzerPlugin({ analyzerMode: 'static' })],
};
```
