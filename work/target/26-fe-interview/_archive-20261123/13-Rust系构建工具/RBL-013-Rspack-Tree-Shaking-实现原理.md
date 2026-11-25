---
title: [RBL-013] Rspack 的 Tree Shaking 是怎么实现的？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-013：Rspack 的 Tree Shaking 是怎么实现的？
**答**：
- 基础能力与 webpack 对齐：基于 ESM 静态依赖图做"未引用导出"标记（harmony modules），sideEffects: false 的包整模块摇除，sideEffects 数组精细控制（如 ["*.css"]）。
- 实现位置：在 Rust 侧构建模块图时同步做使用标记（usedExports / providedExports）， concatenation（scope hoisting）期间对可串联模块做进一步死代码消除。
- 压缩层配合：内置 swc 压缩做最后一层 DCE（不可达代码删除），两层叠加才达到最终体积收益；所以"摇不干净"要区分是标记没做还是压缩器保守。
- 常见摇不掉原因：动态访问（obj[key]）、带副作用的上层 re-export、CJS/ESM 混用、babel 转译成 CJS 后依赖图失真（迁移到 builtin:swc-loader 保持 ESM 输出）。
- 验证手段：stats 里查 unused 标记、产物里 grep 导出名、构建时 `optimization.usedExports` 输出提示。
- 追问钩子：Rspack 对 re-export 链、命名空间导入的处理与 webpack 有细节差异，迁移后要抽查体积。

```javascript
// utils.js —— sideEffects 声明决定摇除粒度
export const add = (a, b) => a + b;   // 纯函数，未引用会被摇掉
export const init = () => window.__x = 1; // 有副作用，保留判定交由标记分析

// package.json
// { "name": "@corp/utils", "sideEffects": ["*.css"] }
//   → 除 css 外所有模块声明无副作用，可整模块摇除

// index.js
import { add } from '@corp/utils'; // init 未引用 → DCE 后产物中无 init
console.log(add(1, 2));
```
