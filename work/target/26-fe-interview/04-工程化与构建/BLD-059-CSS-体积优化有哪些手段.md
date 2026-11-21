---
title: [BLD-059] CSS 体积优化有哪些手段？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-059：CSS 体积优化有哪些手段？
**答**：
- 清死代码：PurgeCSS 按"产物 HTML/JS 中出现过的类名"裁剪样式；Tailwind 项目天然受益（JIT 只生成用到的类），但要小心动态拼接类名被误删（白名单 safelist）。
- 压缩：cssnano / lightningcss（比 cssnano 快且支持现代语法降级）；构建期去 @import 合并。
- 架构：CSS Modules + 组件级拆分让样式随 chunk 分割；公共样式抽取防重复（BLD-036）；关键 CSS 内联、其余异步。
- 治理变量：Sass 的 @import 全局引入要换 css @use 按需；旧版 element-ui 全量 import 改按需 babel 插件。

```javascript
// webpack.config.js：PurgeCSS + cssnano 生产链
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  module: {
    rules: [{
      test: /\.css$/,
      use: [MiniCssExtractPlugin.loader, 'css-loader', 'postcss-loader'],
    }],
  },
  plugins: [
    new MiniCssExtractPlugin({ filename: 'css/[name].[contenthash:8].css' }),
    new (require('purgecss-webpack-plugin'))({
      paths: require('glob').sync('src/**/*.{js,jsx,ts,tsx,vue}'),
      extractors: [{
        extractor: (content) => content.match(/[A-Za-z0-9_-]+/g) || [],
        extensions: ['js', 'jsx', 'ts', 'tsx', 'vue'],
      }],
      safelist: { standard: [/^(is|has|data-)/, 'transition', 'fade-enter'] }, // 动态类白名单
    }),
  ],
};

// postcss.config.js：压缩层
module.exports = {
  plugins: [
    require('autoprefixer'),
    require('cssnano')({ preset: ['default', { discardComments: { removeAll: true } }] }),
  ],
};
```
