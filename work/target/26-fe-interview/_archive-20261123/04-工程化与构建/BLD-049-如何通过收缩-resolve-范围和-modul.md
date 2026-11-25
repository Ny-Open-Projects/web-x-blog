---
title: [BLD-049] 如何通过收缩 resolve 范围和 module.noParse 提速？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-049：如何通过收缩 resolve 范围和 module.noParse 提速？
**答**：
- resolve：extensions 列表精简并按命中率排序；modules 只保留本项目 node_modules；alias 直接命中；symlinks: false 可减少软链接二次解析（无 pnpm 场景）；exportsFields 限定包入口字段。
- noParse：声明"这些文件不需要解析依赖"（如 dist 版的 echarts/monaco），webpack 只读不 parse，省 AST 与依赖收集。
- noParse 代价：文件内的 require 不再处理，必须是自包含产物（UMD bundle）。
- 副手：ignorePlugin 屏蔽多语言等无用模块（moment/locale）。

```javascript
// webpack.config.js：resolve 收缩 + noParse
const webpack = require('webpack');
const path = require('path');

module.exports = {
  resolve: {
    extensions: ['.js', '.jsx', '.ts', '.tsx', '.json'], // 精简按命中排序
    modules: [path.resolve('node_modules')],             // 不再向上递归查找
    alias: { react: path.resolve('node_modules/react') },
  },
  module: {
    noParse: [
      /echarts\.min\.js$/,       // 自包含 dist 产物 不解析依赖
      /monaco-editor\/min\/vs/,
    ],
    rules: [
      { test: /\.css$/, use: ['style-loader', 'css-loader'] },
      { test: /\.(js|jsx)$/, include: /src/, use: 'babel-loader' },
    ],
  },
  plugins: [
    // 屏蔽 moment 全部语言包 只保留中文
    new webpack.IgnorePlugin({ resourceRegExp: /^\.\/locale$/, contextRegExp: /moment$/ }),
  ],
};
```
