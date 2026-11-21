---
title: [ENG-012] Vite 生产构建为什么用 Rollup？怎么分包？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-012：Vite 生产构建为什么用 Rollup？怎么分包？
**答**：
- Rollup 产物更干净：原生 ESM 输出、静态分析彻底、tree-shaking 效果好，适合最终发布。
- dev 快（esbuild）与产物优（Rollup）分工，是 Vite "双引擎"设计。
- manualChunks 把稳定依赖抽成独立 chunk，业务迭代时不破坏 vendor 的长缓存。
- 还可配置 target、sourcemap、chunkSizeWarningLimit 等构建细节。

```javascript
// vite.config.ts
import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    target: 'es2015',
    rollupOptions: {
      output: {
        // 手动分包：稳定库单独成 chunk，命中浏览器长缓存
        manualChunks: {
          react: ['react', 'react-dom'],
          lodash: ['lodash-es'],
        },
      },
    },
    chunkSizeWarningLimit: 1024,
    sourcemap: true,
  },
});
```
