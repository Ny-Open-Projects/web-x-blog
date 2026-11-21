---
title: [BLD-048] thread-loader / 并行处理何时有效、何时是负优化？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-048：thread-loader / 并行处理何时有效、何时是负优化？
**答**：
- 原理：thread-loader 把后续 loader 放进 worker 池执行，利用多核；只对"它之后"的 loader 生效。
- 有效场景：单文件转换计算量大（babel 重 preset、ts 编译）、模块数量多、机器核多。
- 负优化场景：loader 本身很轻（纯字符串处理）、文件数少（启动 worker 进程的固定开销 > 收益）、缓存开启后二次构建命中率已很高。
- webpack 5 生态推荐：压缩并行交给 terser-webpack-plugin 的 parallel、js 转换交给 esbuild-loader/SWC（内置并行）替代 thread-loader + babel。

```javascript
// webpack.config.js：thread-loader 位置与替代方案
const os = require('os');

module.exports = {
  module: {
    rules: [{
      test: /\.js$/,
      include: /src/,
      use: [
        {
          loader: 'thread-loader',
          options: {
            workers: Math.max(1, os.cpus().length - 1),
            poolTimeout: 2000,     // dev 常驻 prod 可设短释放
          },
        },
        'babel-loader',            // 真正干重的 loader 放在 thread-loader 之后
      ],
    }],
  },
};

// 更优替代：esbuild-loader 内置 Go 并行（推荐）
// module.exports = { module: { rules: [{
//   test: /\.js$/, include: /src/,
//   use: [{ loader: 'esbuild-loader', options: { target: 'es2018' } }],
// }] } };
```
