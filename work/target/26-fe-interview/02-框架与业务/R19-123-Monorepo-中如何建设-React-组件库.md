---
title: [R19-123] Monorepo 中如何建设 React 组件库？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-123：Monorepo 中如何建设 React 组件库？
**答**：
- 包结构：peerDependencies 声明 react/react-dom 交给宿主提供，避免打包出双 React 实例。
- 构建用 tsup/vite lib mode 输出 ESM + d.ts；exports 字段约束入口与类型。
- 发版用 changesets：PR 里声明变更，CI 自动汇总生成版本与 changelog。
- Storybook 承担文档与视觉回归；组件库原则：受控优先、样式可覆盖、不内置业务请求。

```javascript
// packages/ui/package.json —— 组件库包的关键字段
{
  "name": "@acme/ui",
  "version": "0.0.0",
  "type": "module",
  "exports": {
    ".": { "types": "./dist/index.d.ts", "import": "./dist/index.js" },
    "./styles.css": "./dist/styles.css"
  },
  // React 交给宿主，避免双实例导致 Invalid hook call
  "peerDependencies": { "react": "^19.0.0", "react-dom": "^19.0.0" },
  "scripts": {
    "build": "tsup src/index.tsx --dts --external react",
    "test": "vitest run"
  }
}
// 工程链路：pnpm workspace 管理 + changesets 发版 + Storybook 当文档与视觉回归
// 组件库原则：受控优先、样式可覆盖、不内置业务请求
```
