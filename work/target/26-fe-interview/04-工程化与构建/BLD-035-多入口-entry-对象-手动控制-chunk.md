---
title: [BLD-035] 多入口（entry 对象）手动控制 chunk 的取舍是什么？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-035：多入口（entry 对象）手动控制 chunk 的取舍是什么？
**答**：
- 多 entry 会生成多个独立 chunk，天然按入口隔离依赖，但公共依赖需要 splitChunks 抽取，否则各打一份重复代码。
- 适合：MPA、独立部署的 admin/app 子站；不适合：公共代码占比高的 SPA（维护成本高）。
- entry 可以配 dependOn（入口依赖链，保证加载顺序）与 runtime 指定共享 runtime；也可给不同 entry 不同的 splitChunks 期望。
- 手动 chunks 的底线：优先让"模块归属"自动推导（splitChunks），手动只是补充命名与特例。

```javascript
// webpack.config.js：多入口 + dependOn 完整示例
const path = require('path');

module.exports = {
  mode: 'production',
  entry: {
    // 共享 chunk 先加载 admin 依赖 shared 运行时
    shared: ['lodash', 'dayjs'],
    admin: { import: './src/admin/index.js', dependOn: 'shared' },
    portal: { import: './src/portal/index.js', dependOn: 'shared' },
  },
  output: {
    path: path.resolve('dist'),
    filename: '[name].[contenthash:8].js',
  },
  optimization: {
    runtimeChunk: 'single', // 多入口共享一个 runtime
    splitChunks: {
      cacheGroups: {
        shared: { test: /[\\/]src[\\/]common[\\/]/, name: 'src-common', chunks: 'all' },
      },
    },
  },
};
// html 模板需按顺序注入 shared -> 入口 chunk
```
