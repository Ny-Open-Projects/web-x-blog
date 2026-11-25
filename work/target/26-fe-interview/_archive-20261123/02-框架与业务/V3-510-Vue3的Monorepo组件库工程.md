---
title: [V3-510] Vue3 的 Monorepo 组件库工程
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## V3-510：Vue3 的 Monorepo 组件库工程

**答**：
- 结构：packages/{components, hooks, utils, icons, theme}——组件与 hooks 分包（用 hooks 不用组件的场景轻依赖）；pnpm workspace + changesets 版本管理
- 构建策略：组件库产物双格式（ESM + 类型 d.ts，unbuild/tsup）+ 按需子路径导出（exports map）——tree-shaking 友好与 types 完整
- 开发体验：workspace 内 demo 应用直接引用源码（HMR 不用构建）；文档站（Storybook/VitePress）与组件同仓
- 版本与发布：changesets（PR 声明变更 → 合并出 release PR）——组件库 breaking change 的流程化管控
- 测试分层：hooks 单测（vitest）+ 组件交互测试（test-utils）+ 视觉回归（Storybook + 截图）——仓库 CI 按包增量跑

```json
// package.json exports
{ "name": "@acme/components",
  "exports": {
    ".": { "types": "./dist/index.d.ts", "import": "./dist/index.mjs" },
    "./button": { "types": "./dist/button/index.d.ts", "import": "./dist/button/index.mjs" }
  },
  "sideEffects": ["**/*.css"] }
```
