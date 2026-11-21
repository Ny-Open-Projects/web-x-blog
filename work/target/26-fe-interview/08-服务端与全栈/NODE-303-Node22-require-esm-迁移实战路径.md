---
title: [NODE-303] Node 22 require(esm) 迁移实战路径？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-303：Node 22 require(esm) 迁移实战路径？
**答**:
- 阶段一：不迁移，直接 require ESM 依赖（Node 22 允许）——CI 加 lint 检查"被 require 的 ESM 不能含 TLA"。
- 阶段二：package.json 加 "type": "module"（或 .mjs 后缀），存量 .js 改 import/export——codemod（require → import）+ __dirname 替换（import.meta.dirname）。
- 阶段三：清理双产物（原 CJS+ESM 双发 → 纯 ESM 单产物），exports map 收敛。
- 风险点：深度 require 链中的 ESM-TLA 依赖、动态 require（可变路径）在 ESM 不支持——改 import()。

```javascript
// 迁移 codemod 要点
// 1) require → import：const x = require('lib') → import x from 'lib'（named: import { a } from 'lib'）
// 2) __dirname → import.meta.dirname（Node 20.11+）
// const path = __dirname + '/conf.json'
// → const path = import.meta.dirname + '/conf.json'
// 3) 动态 require → await import()
// const mod = require(name)
// → const mod = await import(name)      // 注意调用方要变 async
// 4) exports 产物收敛
// "exports": { ".": "./dist/index.mjs" }   // 原 cjs+esm 双入口 → 单入口
```
