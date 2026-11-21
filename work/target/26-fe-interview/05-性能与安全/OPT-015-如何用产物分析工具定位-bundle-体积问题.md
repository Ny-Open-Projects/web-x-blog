---
title: [OPT-015] 如何用产物分析工具定位 bundle 体积问题？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-015：如何用产物分析工具定位 bundle 体积问题？

**答**：
- Vite/Rollup 用 `rollup-plugin-visualizer`，webpack 用 `webpack-bundle-analyzer`，产出 treemap 直观展示"谁占了体积"。
- 分析四类典型问题：被整包引入的大库（moment/locale）、重复依赖（两个版本的 lodash）、polyfill 过度（legacy 插件目标过旧）、静态资源误打包（大 JSON/图片 base64）。
- 看体积要同时看原始体积与 gzip/brotli 后体积，传输成本以后者为准。
- 把分析命令固化到 `npm run analyze`，配合 CI 体积报告（size-limit / bundlesize）形成习惯。

```typescript
// 一一对应：Vite 接入 rollup-plugin-visualizer
import { defineConfig } from 'vite';
import { visualizer } from 'rollup-plugin-visualizer';

export default defineConfig({
  plugins: [
    visualizer({
      filename: 'dist/stats.html', // 构建后打开 dist/stats.html 查看 treemap
      template: 'treemap',         // 也可选 sunburst / network
      gzipSize: true,              // 同时展示 gzip 后体积，更接近真实传输成本
      brotliSize: true,
    }),
  ],
});
```
