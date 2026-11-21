---
title: [NODE-005] ESM 在 Node 中如何加载？package.json 有哪些相关字段？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-005：ESM 在 Node 中如何加载？package.json 有哪些相关字段？
**答**：
- 判定 ESM：`.mjs` 扩展名，或 `.js` 且最近祖先 `package.json` 中 `"type": "module"`；`.cjs` 永远是 CJS。ESM 中没有 `require`/`__dirname`，用 `import.meta.url` 转换。
- 关键字段：`type`（module/commonjs）、`exports`（**入口白名单与条件导出**，优先级高于 `main`，且能封装内部路径）、`imports`（包内自引用 `#` 前缀）、`main`/`module`/`browser`（老方案）、`engines`、条件导出中的 `import`/`require`/`node`/`default`/`types`。
- ESM 加载是**异步的、静态分析的**：import 提升与编译期确定依赖图；顶层 await 可用；动态 `import()` 返回 Promise。CJS 可以 `require` ESM（Node 22+ 支持 require 同步 ESM，需无顶层 await），ESM 中推荐 `createRequire` 读取 CJS 资源。

```json
{
  "name": "my-pkg",
  "version": "1.0.0",
  "type": "module",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.mjs",
      "require": "./dist/index.cjs",
      "default": "./dist/index.mjs"
    },
    "./utils": "./dist/utils.mjs",
    "./package.json": "./package.json"
  },
  "imports": {
    "#internal/*": "./src/internal/*.js"
  },
  "engines": { "node": ">=20" }
}
```

```javascript
// ESM 中获取 __dirname 的等价写法（esm-app.mjs）
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { createRequire } from 'node:module';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
console.log(join(__dirname, 'config.json'));

const require = createRequire(import.meta.url); // 在 ESM 中复用 CJS 的 require
const legacy = require('./legacy-config.cjs');
```
