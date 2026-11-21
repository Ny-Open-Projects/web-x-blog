---
title: [RBL-136] SWC 的压缩能力：swc-minify 与 terser 怎么选
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-136：SWC 的压缩能力：swc-minify 与 terser 怎么选

**答**：
- swc 的 minifier 是 Rust 实现（借鉴 terser 语义），速度比 terser 快几十倍，大项目能把 minify 阶段从分钟级压到秒级。
- 压缩率：两者差距一般在 1%~3% 以内（terser 偶尔更极致），对 gzip 后体积影响更小——性能收益远大于这点体积差。
- 配置面：mangle/compress/死代码消除/const folding 均支持；`compress: true` + `mangle: true` 是常规组合，`drop_console`、`keep_fnames` 等开关也有对应项。
- Rspack 内置 minify 默认走 SWC（optimization.minimize + minimizer 配置 swcJsMinimizerRspackPlugin），webpack 下可用 SwcMinifyWebpackPlugin 或继续 terser。
- 追问钩子：sourcemap 正确性是历史踩坑点——升级 SWC 版本后要抽查压缩产物 sourcemap 映射，特别是 async/await 与 try/catch 位置。

```javascript
// webpack 使用 swc 压缩（vs terser 配置对照）
const SwcMinifyWebpackPlugin = require('swc-minify-webpack-plugin').default;

module.exports = {
  optimization: {
    minimize: true,
    minimizer: [
      new SwcMinifyWebpackPlugin({
        minimize: true,
        compress: { drop_console: process.env.NODE_ENV === 'production' },
        mangle: true,
        format: { comments: false }, // terser 的 extractComments 对应项
      }),
    ],
  },
};
// 独立调用（CLI 场景）：
// const { minify } = require('@swc/core');
// const r = await minify(code, { compress: true, mangle: true, sourceMap: true });
```
