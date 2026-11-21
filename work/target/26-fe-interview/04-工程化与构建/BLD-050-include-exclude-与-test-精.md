---
title: [BLD-050] include/exclude 与 test 精确化为什么重要？怎么写才规范？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-050：include/exclude 与 test 精确化为什么重要？怎么写才规范？
**答**：
- 原理：loader 命中判断发生在"每个模块构建"时；不写 include 会让 babel-loader/eslint-loader 扫遍 node_modules，这是新手构建慢的第一大原因。
- 规范写法：用 include 白名单（正向表达业务目录）优先于 exclude 黑名单；test 与 type、resourceQuery 组合精确匹配。
- include 用绝对路径数组，避免用宽松正则误吞 node_modules 内的 @scope。
- 提示：Include 越严，HMR 与增量也越快（快照范围同步缩小）。

```javascript
// webpack.config.js：规范示例
const path = require('path');
const SRC = path.resolve('src');
const PKGS = ['@app/ui', '@app/hooks'].map((p) =>
  path.dirname(require.resolve(`${p}/package.json`))); // monorepo 内部包也纳入编译

module.exports = {
  module: {
    rules: [
      {
        test: /\.(js|jsx|ts|tsx)$/,
        include: [SRC, ...PKGS],   // 白名单 业务目录 + 内部包
        use: 'babel-loader',
      },
      {
        test: /\.css$/,
        oneOf: [
          { test: /\.module\.css$/, include: SRC, use: ['style-loader', { loader: 'css-loader', options: { modules: true } }] },
          { use: ['style-loader', 'css-loader'] },
        ],
      },
    ],
  },
};
```
