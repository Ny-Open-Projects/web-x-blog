---
title: [ENG-022] Rollup 和 webpack 怎么选？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-022：Rollup 和 webpack 怎么选？
**答**：
- Rollup 基于 ESM 静态分析，产物干净、几乎无运行时冗余，tree-shaking 效果更好。
- webpack 生态与 code splitting 更成熟，适合应用开发；Rollup 适合打包库。
- Vite 让两者分工：dev 用 esbuild + 原生 ESM，build 用 Rollup。
- 库打包输出多格式：ESM 给打包器、UMD 给 script 标签场景。

```javascript
// rollup.config.js
import terser from '@rollup/plugin-terser';

export default {
  input: 'src/index.js',
  output: [
    { file: 'dist/index.esm.js', format: 'es' },
    { file: 'dist/index.umd.js', format: 'umd', name: 'MyLib' },
  ],
  // react 由使用方提供，不打进产物
  external: ['react'],
  plugins: [terser()],
};
```
