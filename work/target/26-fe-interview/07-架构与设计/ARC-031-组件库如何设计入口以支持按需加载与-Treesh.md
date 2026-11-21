---
title: [ARC-031] 组件库如何设计入口以支持按需加载与 Tree-shaking？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-031：组件库如何设计入口以支持按需加载与 Tree-shaking？
**答**：
- 前提是 ESM 产物 + 无副作用：`sideEffects: false`（样式文件除外），打包器才能安全摇树。
- 双入口策略：主入口聚合导出给 TypeScript 补全，同时提供 `exports` 子路径（`@corp/ui/button`）给强按需场景。
- Babel 插件方案（`unplugin-vue-components`/`babel-plugin-import`）是兜底，能靠 exports 解决就少一个构建插件。

```json
{
  "name": "@corp/ui",
  "type": "module",
  "sideEffects": ["**/*.css"],
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "import": "./dist/index.js",
      "require": "./dist/index.cjs"
    },
    "./button": {
      "types": "./dist/button/index.d.ts",
      "import": "./dist/button/index.js",
      "require": "./dist/button/index.cjs"
    },
    "./dist/style.css": "./dist/style.css",
    "./package.json": "./package.json"
  }
}
```

```typescript
// dist/index.js 聚合入口（配合 sideEffects:false 可被 tree-shaking）
export { Button } from './button';
export { Table } from './table';
// 使用方：import { Button } from '@corp/ui' → 只打包 Button 相关模块
// 使用方：import Button from '@corp/ui/button' → 显式子路径，按需最彻底
```
