---
title: [BLD-141] rollup 打包流程：acorn 解析 → 作用域分析 → treeshake → generate 各阶段做什么？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-141：rollup 打包流程：acorn 解析 → 作用域分析 → treeshake → generate 各阶段做什么？
**答**：
- `rollup.rollup(inputOptions)`：**build 阶段**——resolveId/load/transform 钩子逐模块产码 → acorn 解析 AST → **作用域分析**（@rollup/pluginutils? 实际内置 scope 分析：绑定变量声明与引用，建 Module 间依赖图 with resolution）→ **treeshake**（从 entry 的被引用符号出发做活性分析，标记副作用与死代码）→ 产出 bundle 对象（内存中的 chunk 划分与模块树）。
- `bundle.generate/write(outputOptions)`：**generate 阶段**——renderChunk/renderStart/outputOptions/banner-footer 钩子、代码渲染（保留执行顺序的语句级拼接）、sourcemap 链生成、`write` 落盘。
- 与 webpack 本质差异：rollup 的产物是**语句级拼接**（ESM 原生结构保持 hoisting），没有 runtime/模块表；tree-shaking 是**构建进图时的一等公民**（基于 use 标记），而非后置优化。
- 调试手段：`rollup -c --environment DEBUG:trees`? 更通用的是 `bundle.write({ sourcemap })` + `visualizer`；官方 playground（rollupjs.org/repl）看树摇结果。

```javascript
// rollup 双阶段 API 拆解：rollup.rollup（build）与 bundle.write（generate）
import { rollup } from 'rollup';

const bundle = await rollup({
  input: 'src/index.js',
  plugins: [ /* resolve/load/transform 在 build 阶段逐模块调用 */ ],
  treeshake: {
    moduleSideEffects: true,
    tryCatchDeoptimization: false,   // try/catch 内不做副作用豁免（默认 true 会保守保留）
  },
});
// 此刻已完成：模块图构建 + 作用域分析 + 树摇标记
console.log(bundle.modules.map((m) => ({
  id: m.id,
  usedExports: m.getRenderedExports?.(),   // 实际保留的导出
  removedExports: m.getUnusedExports?.(),
})));

await bundle.write({
  format: 'esm',
  file: 'dist/index.js',
  sourcemap: true,
  // generate 阶段输出控制：hoistTransitiveImports 避免异步 chunk 间多余静态依赖
});
await bundle.close();
```
