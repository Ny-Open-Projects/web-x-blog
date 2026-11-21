---
title: [RBL-016] Rspack 如何处理静态资源（图片/字体/WASM）？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-016：Rspack 如何处理静态资源（图片/字体/WASM）？
**答**：
- Asset 模块与 webpack 5 对齐：`type: 'asset'` 自动在 inline（data URL）与 file（ emitted 文件）之间按体积阈值（parser.dataUrlCondition.maxSize，默认 8KB）选择。
- 四种类型语义：asset/resource 强制外部文件；asset/inline 强制 data URL；asset/source 直接导出源码字符串；asset 自动二选一。
- 输出命名：generator.filename 支持 [name][ext][contenthash:8]，字体/图片分别配 cacheGroup 控制落盘目录。
- WASM：支持 async webassembly 模块类型，import() 后返回 wasm 导出，与 webpack 的 WebpackAsyncBoundary 行为对齐。
- 对比 webpack 差异：file-loader/url-loader/asset-modules 的迁移方向是统一收敛到内置 asset 类型，不再需要旧 loader。
- 追问钩子：小图标高数量场景（雪碧图时代遗留）用 maxSize 提高内联阈值可减少请求数，但注意 CSS 体积与缓存失效的权衡。

```javascript
// rspack.config.js
module.exports = {
  module: {
    rules: [
      { test: /\.(png|jpe?g|webp|gif|svg)$/,
        type: 'asset',
        parser: { dataUrlCondition: { maxSize: 8 * 1024 } },
        generator: { filename: 'img/[name].[contenthash:8][ext]' } },
      { test: /\.(woff2?|ttf|eot)$/, type: 'asset/resource',
        generator: { filename: 'font/[name].[contenthash:8][ext]' } },
      { test: /\.wasm$/, type: 'webassembly/async' },
    ],
  },
  experiments: { asyncWebAssembly: true },
};
```
