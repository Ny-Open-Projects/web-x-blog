---
title: [ENG-138] npm 包发布的完整工程要包含哪些字段与流程？双格式 dts exports files？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-138：npm 包发布的完整工程要包含哪些字段与流程？双格式 dts exports files？
**答**：
- 双格式产物：esm 给现代打包器（tree-shaking 友好），cjs 兜底 node require 场景，exports 显式声明两个入口与 types。
- dts 必须随包发布：types 字段指向 d.ts，用 tsc --emitDeclarationOnly 或 api-extractor 生成，不让用户手写声明。
- files 白名单控制发布内容：只带 dist/README/LICENSE，tests 与 src 截在包外，直接影响用户 install 时长。
- 发布链路：prepublishOnly 跑 lint+test+build，先 --dry-run 看清单，版本号由 CI 自动化打（见 changelog 一章）。

```json
{
  "name": "@corp/http-client",
  "version": "2.1.0",
  "type": "module",
  "main": "./dist/index.cjs",
  "module": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js",
      "require": "./dist/index.cjs"
    },
    "./package.json": "./package.json"
  },
  "files": ["dist", "README.md", "LICENSE"],
  "sideEffects": false,
  "publishConfig": { "registry": "https://verdaccio.corp.internal" },
  "scripts": {
    "build": "vite build && tsc --emitDeclarationOnly",
    "prepublishOnly": "pnpm lint && pnpm test && pnpm build && npm publish --dry-run"
  }
}
```
