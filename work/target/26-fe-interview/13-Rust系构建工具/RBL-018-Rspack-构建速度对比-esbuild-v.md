---
title: [RBL-018] Rspack 与 esbuild 构建速度对比，各自定位？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-018：Rspack 与 esbuild 构建速度对比，各自定位？
**答**：
- 纯编译吞吐 esbuild 通常更快（Go 单二进制、极简管线、作者激进优化），Rspack 因为背着 webpack 兼容语义（模块类型、splitChunks、tapable 子集）有额外开销，但量级同样是"秒级"。
- 定位差异：esbuild 是"构建原语"（transform/build API），不做完整插件生态、不做 HMR 运行时协议，常被 Vite 当依赖使用；Rspack 是"完整构建器"，目标是替代 webpack 承载大型应用。
- 能力差异：Rspack 提供 webpack 级的 splitChunks/Module Federation/持久缓存/loader 链；esbuild 用极简 plugin API + manualChunks 声明式分割。
- 选型逻辑：新项目从零搭且接受极简生态→esbuild/Vite 系；存量 webpack 项目要提速→Rspack。
- 数据参考：同为数千模块应用，esbuild 冷构建可能 1~3s、Rspack 5~10s、webpack 60s+；差异来自功能面而不是纯速度。
- 追问钩子：esbuild 瓶颈常在"生态缺失要自己补"，Rspack 瓶颈常在"JS 插件 FFI"，两者都提示：构建工具的最终速度由最慢的一环决定。

```javascript
// esbuild：原语式 API（无 webpack 语义）
await require('esbuild').build({
  entryPoints: ['src/index.ts'], bundle: true, minify: true,
  splitting: true, format: 'esm', outdir: 'dist',
  manualChunks: { vendor: ['react', 'react-dom'] },
});

// Rspack：完整构建器（webpack 语义子集）
// const config = require('./rspack.config.js'); // splitChunks、MF、缓存齐备
```
