---
title: [BLD-032] splitChunks 的核心参数精讲？chunks、minSize、cacheGroups、优先级、maxAsyncRequests 怎么配？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-032：splitChunks 的核心参数精讲？chunks、minSize、cacheGroups、优先级、maxAsyncRequests 怎么配？
**答**：
- chunks: 'all' | 'async' | 'initial'：决定参与分割的 chunk 类型，默认 async（最安全），'all' 才能抽出 initial 与 async 共用的模块。
- minSize / minRemainingSize / minChunks：模块至少多大、剩余 chunk 至少多大、被引用几次才值得抽；防止"为抽而抽"。
- maxSize：强制把超过阈值的 chunk 再切（性能一般，仅针对超大包）。
- cacheGroups：按 test/priority/name 分组；priority 决定模块归属（命中多个组时取优先级高的），name 是最终文件名（可用函数）。
- maxAsyncRequests / maxInitialRequests：并行请求上限，超过时放弃优先级最低的分割；HTTP2 可适当调大。

```javascript
// webpack.config.js：生产级 splitChunks 全参数注释版
module.exports = {
  optimization: {
    splitChunks: {
      chunks: 'all',
      minSize: 20 * 1024,        // 模块 >= 20KB 才考虑抽
      maxSize: 500 * 1024,       // 单 chunk 上限 超 500KB 强制再切（可选）
      minChunks: 1,              // 至少被 1 个 chunk 引用
      maxAsyncRequests: 30,      // 异步并行请求上限
      maxInitialRequests: 25,    // 首屏并行请求上限
      automaticNameDelimiter: '~',
      cacheGroups: {
        reactVendor: {           // 命中优先级高 先归它
          test: /[\\/]node_modules[\\/](react|react-dom|scheduler)[\\/]/,
          name: 'vendor-react',
          priority: 40,
          reuseExistingChunk: true,
        },
        echarts: {
          test: /[\\/]node_modules[\\/](echarts|zrender)[\\/]/,
          name: 'vendor-echarts',
          priority: 30,
          chunks: 'async',       // 图表库只随异步页加载
        },
        vendors: {               // 兜底 三方库
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          priority: 10,
        },
        commons: {               // 业务公共模块
          minChunks: 2,
          name: 'commons',
          priority: 20,
          reuseExistingChunk: true,
        },
      },
    },
  },
};
```
