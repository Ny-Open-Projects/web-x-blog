---
title: [NODE-202] Node 22 的 require(esm) 互操作如何工作？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-202：Node 22 的 require(esm) 互操作如何工作？
**答**：
- 机制：require('.mjs') 时 Node 把 ESM 模块编译为同步可加载形式——named exports 变成 require 返回对象的属性；`module.exports = await import('...')` 的内建化。
- 限制一：模块图里任何模块含**顶层 await（TLA）**则 require 抛 ERR_REQUIRE_ASYNC_MODULE——同步语义装不下异步初始化。
- 限制二：仅限"文件级 ESM"，require 仍然是同步的，动态 import 行为不变。
- 实践价值：老 CommonJS 项目可以零迁移引入 ESM 依赖（很多新 npm 包已弃 CJS）；迁移策略从"全仓转换"变为"按文件渐进"。
- 面试加分：指出 CJS require ESM 与 ESM import CJS 的差异（后者早支持，named exports 靠 cjs-module-lexer 静态分析）。

```javascript
// pkg-info.mjs (ESM)
export const version = '2.0';
export function info() { return `pkg@${version}`; }

// legacy.cjs（CommonJS，不迁移直接用 ESM）
const { version, info } = require('./pkg-info.mjs');   // Node 22 OK
console.log(info());                                   // pkg@2.0

// 反例：含顶层 await 的 ESM 不能被 require
// config.mjs: export const cfg = await loadRemote();   // TLA
// require('./config.mjs') → ERR_REQUIRE_ASYNC_MODULE
// 解法：动态 import（异步上下文）或预构建（bundle 成 CJS）
```
