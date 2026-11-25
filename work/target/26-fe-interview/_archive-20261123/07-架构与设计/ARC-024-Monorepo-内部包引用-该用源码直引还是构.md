---
title: [ARC-024] Monorepo 内部包引用，该用源码直引还是构建产物？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-024：Monorepo 内部包引用，该用源码直引还是构建产物？
**答**：
- 源码直引（Transpile Packages）：调试方便、改动即时生效，但每个 app 都要重复编译上游，构建慢、编译器配置耦合。
- 构建产物引用：包自己 `prepublish`/watch 产出 dist，消费方零编译成本，但开发链路要配 watch。
- 实践折中：开发期用 tsconfig paths + pnpm 内部链接直指源码，CI/发布走产物；Turborepo 的 `^build` 保证产物总是新鲜。

```json
{
  "name": "@corp/ui",
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
  "files": ["dist"],
  "scripts": {
    "dev": "tsup src --watch",          // 开发期 watch
    "build": "tsup src --format esm,cjs --dts"
  },
  "publishConfig": { "access": "public" }
}
```
