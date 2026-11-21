---
title: [BAS-182] npm 包支持 ESM 要在 package.json 里配什么？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-182：npm 包支持 ESM 要在 package.json 里配什么？
**答**：
- `type: "module"`：让 .js 文件按 ESM 解析（否则默认 CommonJS）。
- exports：现代入口声明，限定外部能导入的子路径，优先级高于 main，支持 import/require 双条件。
- 双格式包惯例：module 字段给打包器提示 ESM 版本，exports 里用条件导出精确分流。

```json
{
  "name": "pkg",
  "type": "module",
  "main": "./dist/index.cjs",
  "module": "./dist/index.js",
  "exports": {
    ".": {
      "import": "./dist/index.js",
      "require": "./dist/index.cjs"
    },
    "./utils": "./dist/utils.js"
  }
}
```
