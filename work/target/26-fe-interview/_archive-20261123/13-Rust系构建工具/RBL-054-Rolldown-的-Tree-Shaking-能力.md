---
title: [RBL-054] Rolldown 的 Tree Shaking 与 Rollup 相比如何？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-054：Rolldown 的 Tree Shaking 与 Rollup 相比如何？
**答**：
- 算法同源：Rolldown 移植了 Rollup 的"标记-清除"式摇树（入口语句驱动：模块的顶层语句依是否被引用导出决定去留），再叠加 Rust 并行执行。
- 优势场景：rolldown 在大依赖图上更快，且对 sideEffects 字段、/*#__PURE__*/ 注解、CJS 互操作的处理与 Rollup 对齐；官方基准中部分场景体积甚至略优于 rollup（压缩层用了 oxc_minifier）。
- 与 webpack 的差异：rollup/rolldown 的摇树以"语句"为粒度，比 webpack 的模块粒度标记更精细（webpack 主要靠 usedExports + terser DCE）。
- 常见坑一致：有副作用的无条件顶层调用、类字段的装饰器副作用、CJS require 互操作都会阻止摇除。
- 验证方法：构建加 --dev 不压缩看未摇除导出；或 grep 产物确认目标函数是否在。
- 追问钩子：Rollup 的 output.generatedCode 控制产物风格（es2015 symbols 等），rolldown 也有对应选项，影响摇树保守程度。

```javascript
// side-effects 判定演示
// lib.js
export const pure = (x) => x * 2;      // 未引用 → 语句被摇掉
export const tag = (() => {            // 顶层 IIFE 有副作用 → 保留
  window.__side = true;
  return (s) => `[${s}]`;
})();

// pure 注解让调用点在未使用时被摇除
const r = /*#__PURE__*/ pure(2);

// package.json：{ "sideEffects": false } → 未引用模块整体摇除
```
