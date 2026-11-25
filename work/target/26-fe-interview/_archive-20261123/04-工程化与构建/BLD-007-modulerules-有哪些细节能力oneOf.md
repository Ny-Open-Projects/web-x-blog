---
title: [BLD-007] module.rules 有哪些细节能力？oneOf、enforce pre/post、sideEffects 怎么用？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-007：module.rules 有哪些细节能力？oneOf、enforce pre/post、sideEffects 怎么用？
**答**：
- 规则匹配自上而下；oneOf 内的规则命中一条即停止，避免同一文件被多个 loader 叠加处理，常把通用 loader 放进 oneOf。
- enforce: 'pre' 让 loader 先于所有普通 loader 执行（eslint-loader/源码检查），enforce: 'post' 最后执行（如打包后混淆）。
- sideEffects: false 是规则级开关，配合 compilation.hooks.optimizeChunkAssets 前的 sideEffects 优化阶段，把无副作用的模块标记可移除（等价于 package.json 的模块级粒度，规则级可强制覆盖）。
- 其他细节：issuer 限定"被谁引用"、dependency 排除纯 require 上下文、resolve.with + fullySpecified、use 数组顺序为从后往前。

```javascript
// webpack.config.js
module.exports = {
  module: {
    rules: [
      {
        test: /\.(js|ts|jsx|tsx)$/,
        enforce: 'pre',
        include: /src/,
        use: ['eslint-loader'], // 最先跑 源码还没被 babel 转换
      },
      {
        test: /\.css$/,
        oneOf: [ // 命中一条即停
          { test: /\.module\.css$/, use: ['style-loader', 'css-loader?modules'] },
          { use: ['style-loader', 'css-loader'] }, // 兜底
        ],
      },
      {
        test: /vendor-no-side-effect/,
        sideEffects: false, // 规则级声明该文件无副作用 可被 tree-shaking
        type: 'javascript/auto',
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: { loader: 'babel-loader', options: { cacheDirectory: true } },
      },
    ],
  },
};
```
