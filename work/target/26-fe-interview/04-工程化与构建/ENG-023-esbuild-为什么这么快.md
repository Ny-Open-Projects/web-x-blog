---
title: [ENG-023] esbuild 为什么这么快？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-023：esbuild 为什么这么快？
**答**：
- 用 Go 编写，编译为原生机器码；多核并行处理，JS 单线程工具无法比拟。
- 从零实现完整的解析/绑定/代码生成，不经过第三方 AST 库的二次转换。
- 大量数据复用字符串切片，减少内存拷贝与 GC 压力。
- 代价是插件生态与定制能力弱于 webpack/Rollup，因此多用于预构建、压缩、转译等单点提速。

```javascript
const esbuild = require('esbuild');

esbuild.build({
  entryPoints: ['src/index.jsx'],
  bundle: true,
  minify: true,
  format: 'esm',
  target: ['es2018'],
  outdir: 'dist',
});
```
