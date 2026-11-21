---
title: [BLD-083] esbuild-loader 在 webpack 中替代 babel/terser 的收益与配置。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-083：esbuild-loader 在 webpack 中替代 babel/terser 的收益与配置。
**答**：
- 收益：esbuild-loader 替代 babel-loader 转译 + EsbuildPlugin 替代 terser-minimizer，大型项目整体构建提速常见 2~5 倍，且内置并行。
- 代价：产物稍大（esbuild 压缩率略低于 terser）、失去 babel 插件生态（i18n 转换、私有 AST 改造不能用）。
- 折中：业务代码保留 babel（需要插件），node_modules 依赖已编译无需转译；或 dev 用 esbuild prod 用 babel。
- webpack 配置要同步调 optimization.minimizer（替换默认 TerserPlugin）。

```javascript
// webpack.config.js：esbuild-loader 双替换
const { EsbuildPlugin } = require('esbuild-loader');

module.exports = {
  module: {
    rules: [{
      test: /\.(js|jsx|ts|tsx)$/,
      include: /src/,
      loader: 'esbuild-loader',
      options: {
        loader: 'tsx',        // 文件内容类型
        target: 'es2020',
        jsx: 'automatic',
      },
    }],
  },
  optimization: {
    minimizer: [
      '...', // 保留其他默认 minimizer
      new EsbuildPlugin({
        target: 'es2020',
        css: true,            // 顺带压缩 css
        minifyIdentifiers: true,
        minifySyntax: true,
      }),
    ],
  },
};
```
