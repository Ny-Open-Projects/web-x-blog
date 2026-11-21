---
title: [BLD-027] 为什么 CommonJS 难以 tree-shaking？有哪些缓解手段？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-027：为什么 CommonJS 难以 tree-shaking？有哪些缓解手段？
**答**：
- 原因一：exports 是运行时可变对象，可被 `module.exports.x = ...`、条件赋值、`Object.defineProperty` 等动态改写，无法静态枚举导出集合。
- 原因二：require 是普通函数调用，可以出现在 if、循环里，甚至拼接路径（require('./lib/' + name)），使用关系不确定。
- 原因三：CJS 有隐式副作用（this、__dirname、顶层执行顺序），删除顶层语句不安全。
- 缓解手段：cjs-module-lexer 能静态识别"直白"的 `module.exports = { a, b }` 与 `exports.a = ...`，给 webpack 提供部分命名导出；npm 包提供 module/exports 字段给 ESM 入口；或构建前用 esbuild 把 CJS 转 ESM 再进主流程。

```javascript
// cjs 分析示例
// 情形一 可静态分析 -> 命名导出可被标记未使用
exports.formatDate = () => {};
exports.deepClone = () => {};
module.exports = { formatDate, deepClone };

// 情形二 无法分析 -> 整个模块被保留
const name = Math.random() > 0.5 ? 'a' : 'b';
module.exports = require('./' + name);        // 动态 require
module.exports['dyn' + suffix] = () => {};    // 动态键
if (process.env.NODE_ENV === 'dev') {         // 条件导出
  module.exports.debug = () => {};
}
```
