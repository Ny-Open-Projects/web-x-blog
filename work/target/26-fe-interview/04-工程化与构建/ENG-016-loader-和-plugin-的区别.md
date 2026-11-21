---
title: [ENG-016] loader 和 plugin 的区别？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-016：loader 和 plugin 的区别？
**答**：
- loader 是文件转换器：输入源码字符串/Buffer，输出 JS 模块，链式执行且从右到左（从下到上）。
- plugin 基于 tapable 钩子机制介入编译器全生命周期：打包优化、资源注入、生成文件都能做。
- loader 运行在模块转换阶段；plugin 可以监听从 beforeRun 到 done 的任何时机。
- 记忆：loader 解决"webpack 不认识这个文件"，plugin 解决"webpack 流程中做额外的事"。

```javascript
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  module: {
    rules: [
      {
        test: /\.css$/,
        // 执行顺序：css-loader 先解析依赖，再交给 style 层处理
        use: [MiniCssExtractPlugin.loader, 'css-loader'],
      },
    ],
  },
  plugins: [
    // plugin 做 loader 做不到的事：把 CSS 抽成独立文件
    new MiniCssExtractPlugin({ filename: '[name].[contenthash].css' }),
  ],
};
```
