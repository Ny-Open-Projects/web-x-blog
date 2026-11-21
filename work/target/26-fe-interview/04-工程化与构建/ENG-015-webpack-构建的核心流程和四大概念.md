---
title: [ENG-015] webpack 构建的核心流程和四大概念？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-015：webpack 构建的核心流程和四大概念？
**答**：
- entry 指定入口，webpack 从入口递归构建模块依赖图；output 决定产物路径与命名。
- loader 把非 JS 资源（CSS、图片、TS）转换成模块；plugin 通过钩子介入构建生命周期做更广的事情。
- 大致流程：初始化配置 -> 从 entry 开始递归编译模块 -> 封装 chunk -> 输出 bundle。
- mode 决定内置优化：production 自动开启压缩与 tree-shaking。

```javascript
// webpack.config.js
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  mode: 'production',
  entry: './src/main.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    // contenthash 保证内容不变时文件名不变，利于缓存
    filename: '[name].[contenthash:8].js',
  },
  module: {
    rules: [
      { test: /\.css$/, use: ['style-loader', 'css-loader'] },
    ],
  },
  plugins: [new HtmlWebpackPlugin({ template: './index.html' })],
};
```
