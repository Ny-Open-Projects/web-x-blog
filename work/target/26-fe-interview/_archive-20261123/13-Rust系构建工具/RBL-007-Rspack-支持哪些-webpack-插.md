---
title: [RBL-007] Rspack 对 webpack 插件生态的支持策略是什么？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-007：Rspack 对 webpack 插件生态的支持策略是什么？
**答**：
- 策略一句话：高频插件官方实现或提供 rspack 专用版，长尾插件由社区适配，依赖 webpack 内部实现的直接劝退并给出替代方案。
- 官方平替清单：HtmlPlugin→html-rspack-plugin、CopyPlugin→rspack 内置（支持同样配置）、DefinePlugin/EnvironmentPlugin→内置、MiniCssExtract→内置 CSS、TerserPlugin→内置 swc 压缩、ProgressPlugin→内置。
- 兼容层原理：Rspack 实现了 webpack 的 Compiler/Compilation/RspackResolver 以及常用 hooks 的子集，JS 插件通过 napi 拿到"代理对象"操作构建，语义对齐但不保证内部结构一致。
- 迁移判定：插件用了 `compiler.hooks.*` 高频钩子大概率可用；用了 `compilation.modules` 私有遍历、chunk 内部字段、webpack-sources 深度 API 的要逐个验证。
- 追问钩子：插件数量与构建速度的权衡——每个 JS 插件钩子回调都要跨 FFI，迁移目标之一是把插件数收敛到个位数。

```javascript
// rspack.config.js：高频插件的官方替代写法
const rspack = require('@rspack/core');
const HtmlWebpackPlugin = require('html-rspack-plugin');

module.exports = {
  plugins: [
    new HtmlWebpackPlugin({ template: './index.html' }),
    new rspack.CopyRspackPlugin({ patterns: [{ from: 'public', to: '.' }] }),
    new rspack.DefinePlugin({ __APP_VERSION__: JSON.stringify('1.0.0') }),
    // Copy/Define/Progress 等都在 @rspack/core 内置，无需单独安装 webpack 版
  ],
};
```
