---
title: [RBL-022] Rspack 与 Rsbuild 的关系是什么？何时选 Rsbuild？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-022：Rspack 与 Rsbuild 的关系是什么？何时选 Rsbuild？
**答**：
- 分层关系：Rspack 是构建内核（对标 webpack 核心），Rsbuild 是基于内核的上层框架（对标 CRA/Next 的构建层），内置 HTML 生成、dev server、最佳实践默认值、插件体系。
- Rsbuild 价值：零配置起步（约定 src/index 入口）、内置 html/assets/env 体系、统一的 plugins（rsbuild-plugin-*），省去手写 rspack.config.js 的大量样板。
- 选型逻辑：从 webpack 迁移且配置重度定制→直接用 Rspack 保持配置语义；新项目或想要约定式开发体验→Rsbuild，需要底层控制时再向下逃生（支持 webpack 兼容配置透传）。
- 心智负担：Rsbuild 把常见场景（MPA、CSS Modules、polyfill、sourcemap 策略）做了默认决策，团队不用每次争论配置。
- 成本：多一层抽象，遇到边界问题要区分是 Rsbuild 默认值问题还是 Rspack 内核问题。
- 追问钩子：Rsbuild 的 product 定位与 Vite 团队的 Rolldown-vite 相对应——都是"上层框架收编底层引擎"。

```javascript
// rsbuild.config.ts：对比 Rspack 需要的样板大幅减少
import { defineConfig } from '@rsbuild/core';
export default defineConfig({
  source: { entry: { index: './src/index.tsx' } },
  html: { template: './index.html' },
  output: { filenameHash: true, assetPrefix: 'https://cdn.example.com' },
  performance: { chunkSplit: { strategy: 'split-by-experience' } }, // 内置分割策略
  plugins: [],
});
```
