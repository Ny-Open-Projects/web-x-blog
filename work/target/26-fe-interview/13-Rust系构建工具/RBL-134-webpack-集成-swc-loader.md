---
title: [RBL-134] webpack 里集成 swc-loader：与 babel-loader 怎么替换
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-134：webpack 里集成 swc-loader：与 babel-loader 怎么替换

**答**：
- 安装 `@swc/core` + `@swc/core-linux-xxx`（对应平台 binding）+ `swc-loader`，把 rule 里 babel-loader 直接换成 swc-loader，配置从 babel 的 presets 改成 `jsc` 结构。
- swc-loader 支持透传 `jsc.transform.react.refresh: true`，webpack 下要开 React Fast Refresh 需要它（或继续配 react-refresh 插件）。
- 提速关键：babel-loader 每个文件走 JS 插件链很重，换 swc-loader 后主耗时回到 webpack 自身（JS 模块图/代码生成），通常还需配 thread-loader 之外的并行由 SWC 内部 Rust 线程池处理——loader 层不用再开多进程。
- 缓存仍要靠 webpack 的 cache（filesystem）或 babel 层的 cacheDirectory 思路——swc-loader 本身不带磁盘缓存。
- 追问钩子：迁移后用 webpack-bundle-analyzer + 构建耗时对比验证收益；若有 Babel 宏（babel-plugin-macros）依赖，这部分仍要保留 babel-loader 双轨。

```javascript
// webpack.config.js 关键 rule
module.exports = {
  module: {
    rules: [
      {
        test: /\.(ts|tsx|js|jsx|mjs)$/,
        exclude: /node_modules/,
        use: [
          {
            loader: 'swc-loader',
            options: {
              jsc: {
                parser: { syntax: 'typescript', tsx: true },
                target: 'es2020',
                transform: { react: { runtime: 'automatic', refresh: process.env.NODE_ENV === 'development' } },
              },
              module: { type: 'es6' },
            },
          },
        ],
      },
    ],
  },
  cache: { type: 'filesystem' }, // swc-loader 无自带磁盘缓存，交给 webpack
};
```
