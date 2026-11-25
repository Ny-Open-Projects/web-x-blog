---
title: [RBL-056] Rolldown 做库打包（ESM/CJS/UMD/dts）的推荐配置？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-056：Rolldown 做库打包（ESM/CJS/UMD/dts）的推荐配置？
**答**：
- 多格式输出：output 数组同时给 esm 与 cjs 两份产物，package.json 用 exports 的 import/require 条件分发；umd 已被主流平台淘汰（用 cjs 兜底 CDN）。
- dts 生成：rolldown 不内置类型声明生成，用 rolldown-plugin-dts（基于 oxc/ts compiler）或 tsc --emitDeclarationOnly 并行任务，rolldown 的 rollupTypes 模式可把声明文件合并为单文件。
- 外部依赖：external 声明 peerDeps（react、vue 等），库产物不带运行时；package.json 依赖分 dependencies（runtime）与 peerDependencies（宿主提供）。
- 产物纯净：preserveModules: true 做"源码结构保留"产物（利于 monorepo 内部消费与调试），或单文件 bundle（利于 CDN）；sourceMap 可选 external。
- 与 tsup/unbuild 对比：rolldown 提供同等的库打包能力但底层更快，配置语义与 rollup 兼容生态直接复用。
- 追问钩子：库打包的常见事故——把 react 打进产物（external 缺失）导致双实例冲突。

```javascript
// rolldown.config.js（库）
import dts from 'rolldown-plugin-dts';
export default {
  input: 'src/index.ts',
  external: [/^react/, 'clsx'],
  plugins: [dts({ emitDTSOnly: true })],
  output: [
    { format: 'esm', dir: 'dist', entryFileNames: '[name].mjs' },
    { format: 'cjs', dir: 'dist', entryFileNames: '[name].cjs' },
  ],
};
// package.json
// "exports": { ".": { "import": "./dist/index.mjs", "require": "./dist/index.cjs" } }
```
