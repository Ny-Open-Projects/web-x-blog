---
title: [ARC-037] npm 包发布有哪些最佳实践？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-037：npm 包发布有哪些最佳实践？
**答**：
- 双格式产物（ESM + CJS）+ 完整 `exports` 条件映射 + `types`，兼容 bundler 与 Node 场景。
- `files` 白名单控制包体积，`sideEffects` 标注支撑 tree-shaking，`publishConfig` 处理内部 registry。
- 发布前置门禁：干净工作区、`prepublishOnly` 跑测试与构建、`npm pack --dry-run` 人工核对内容。

```json
{
  "name": "@corp/request",
  "version": "1.4.0",
  "type": "module",
  "main": "./dist/index.cjs",
  "module": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js",
      "require": "./dist/index.cjs",
      "default": "./dist/index.cjs"
    },
    "./package.json": "./package.json"
  },
  "files": ["dist", "README.md"],           // 白名单：node_modules 不含测试与源码
  "sideEffects": false,
  "publishConfig": { "registry": "https://registry.corp.internal/" },
  "scripts": {
    "prepublishOnly": "pnpm test && pnpm build && pnpm size-limit",
    "pack:check": "npm pack --dry-run"
  },
  "engines": { "node": ">=18" }
}
```
