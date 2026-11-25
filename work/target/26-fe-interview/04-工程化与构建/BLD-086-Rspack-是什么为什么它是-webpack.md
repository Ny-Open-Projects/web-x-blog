---
title: [BLD-086] Rspack 是什么？为什么它是 webpack 的高性能替代？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-086：Rspack 是什么？为什么它是 webpack 的高性能替代？
**答**：
- Rspack：字节跳动开源的 Rust 构建工具，目标是"兼容 webpack API 的高性能重实现"——配置、loader/plugin 接口（部分）、产物行为对齐 webpack，存量项目低成本迁移。
- 性能来源：Rust 并行、内存布局优化、内置常用功能（minify、css 处理、tree-shaking）减少插件链。
- 生态：rspack.config.js 兼容大部分 webpack 配置；插件体系分 Rust 插件与兼容 webpack 的 JS 插件（有额外开销）；Rsbuild 提供开箱即用的上层封装。
- 选位：大型 webpack 项目想提速（改动最小）、团队想摆脱 vite 迁移成本时的"渐进路线"。

```javascript
// rspack.config.js：与 webpack 配置高度一致的示例
module.exports = {
  mode: 'production',
  entry: './src/index.tsx',
  resolve: { extensions: ['.tsx', '.ts', '.jsx', '.js'] },
  module: {
    rules: [
      { test: /\.tsx?$/, use: { loader: 'builtin:swc-loader', options: { jsc: { parser: { syntax: 'typescript', tsx: true } } } } },
      { test: /\.css$/, type: 'css', use: ['postcss-loader'] }, // 内建 css 支持
      { test: /\.svg$/, type: 'asset/resource' },
    ],
  },
  optimization: { splitChunks: { chunks: 'all' } },
  plugins: [new (require('@rspack/core').HtmlPlugin)()],
  builtins: {
    html: [{ template: './index.html' }], // 内建 html 插件
    minifyOptions: { minifyJS: true },
  },
};
```

**追问**：

1. Rspack 对 webpack 的兼容到什么程度？→ 配置项和主流 loader 基本兼容，但部分 plugin 钩子与内部 API 未实现，深度定制的插件需要改写或换成 Rust 侧实现。
2. 迁移第一步该做什么？→ 先保证产物可比：跑一遍构建 diff 与体积对比，再逐条替换不兼容的 loader/plugin，并保留 webpack 分支作为回退。
3. Rust 插件和 JS 插件性能差多少？→ JS 插件仍在 Node 侧执行，跨语言调用有序列化开销，热点逻辑（自定义 loader 里的正则/AST 处理）会成为新瓶颈。
