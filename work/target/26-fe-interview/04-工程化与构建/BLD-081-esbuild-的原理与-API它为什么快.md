---
title: [BLD-081] esbuild 的原理与 API？它为什么快？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-081：esbuild 的原理与 API？它为什么快？
**答**：
- 为什么快：Go 编译型语言 + 真多核并行（每文件一个 goroutine）；从零实现的编译器不做 AST 对象（用连续内存/二进制表示），解析、绑定、转换一次遍历完成；缓存友好的内存布局；依赖图并行分析。
- 巨大收益的来源还有"先到者优势"：等价功能的 JS 工具链（babel/terser/webpack）串行执行多遍 AST。
- 三大 API：transform（单文件转换，最常用）、build（项目构建，输出产物）、serve/buildSync/transformSync（同步或开发服务变体）。
- 定位：转换与打包的速度之王；但生态扩展靠 Go 插件（弱），常被嵌入 Vite、tsup、ts-node 等做"重活"。

```javascript
// esbuild API 三件套
const esbuild = require('esbuild');

// 1 transform：单文件转换（loader: ts/jsx/css 等）
const result = await esbuild.transform(tsCode, {
  loader: 'ts',
  target: 'es2020',
  sourcemap: true,
  minify: true,
});

// 2 build：项目级构建（打包 + 压缩 + sourcemap 一条龙）
await esbuild.build({
  entryPoints: ['src/index.ts'],
  bundle: true,
  outdir: 'dist',
  format: 'esm',
  splitting: true,          // ESM 动态 import 自动分 chunk
  minify: true,
  sourcemap: true,
  metafile: true,           // 输出体积元数据
  external: ['react'],
  jsx: 'automatic',
});

// 3 serve：内置 dev 服务（比外部 watch 少一层 fs 开销）
await esbuild.serve({ servedir: 'dist', port: 8000 }, {
  entryPoints: ['src/index.ts'], bundle: true, outdir: 'dist',
});

// metafile 分析（text 代码块）：
// node -e "const r=require('./meta.json');
//   for (const [file, info] of Object.entries(r.outputs)) console.log(file, info.bytes)"
```
