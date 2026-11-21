---
title: [BLD-023] css-loader 和 mini-css-extract-plugin 的协作链路是怎样的？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-023：css-loader 和 mini-css-extract-plugin 的协作链路是怎样的？
**答**：
- css-loader 负责"css 里的依赖与语义"：解析 @import、url() 为 require/import（变成模块图依赖），处理 CSS Modules 的 :local/:global 类名映射，导出一个默认数组结构（[module id, css 文本, sourceMap, media]）。
- mini-css-extract-plugin.loader 在 normal 阶段（不是 pitch）拦截 css-loader 的输出：不返回 JS，而是调用 plugin 主模块注册的收集器，把 css 文本作为 chunk 的副产物收集。
- plugin 主体在 compilation 钩子（processAssets 之前的 renderChunk / contentHash 阶段）把收集到的 css 按 chunk 合并、分割（importLoaders 对应的链也重排），生成 .css 文件并修改 js 里对样式的引用为纯 import（运行时只加载文件，无样式注入逻辑）。
- 注意 importLoaders 数值：值为 2 表示 css-loader 之前的 2 个 loader（postcss-loader、sass-loader）产物也被 @import 引用链用到，必须一致否则变量/mixin 丢失。

```javascript
// webpack.config.js：生产级 css 抽离完整配置
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  module: {
    rules: [{
      test: /\.(css|scss)$/,
      use: [
        MiniCssExtractPlugin.loader,   // 3 收集 css-loader 输出 交给 plugin 抽文件
        { loader: 'css-loader',        // 2 解析 @import url 处理 CSS Modules
          options: {
            importLoaders: 2,          // @import 进来的 css 也先过前两个 loader
            modules: { exportLocalsConvention: 'camelCase' },
            sourceMap: true,
          } },
        'postcss-loader',              // 1 autoprefixer 等
        'sass-loader',                 // 0 sass 编译
      ],
    }],
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: 'css/[name].[contenthash:8].css',
      chunkFilename: 'css/[id].[contenthash:8].css',
      experimentalUseImportModule: true, // webpack 5 更快的原生模块执行
    }),
  ],
};
```
