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

**边界与易错**：

1. `manualChunks` 函数返回 `undefined` 不报错：模块静默退回默认分包，vendor 根本没拆出来，要核对产物而不是相信配置。
2. 跨 chunk 循环依赖：Rollup 会告警并把模块拉回同一 chunk，原本拆开的长缓存收益直接消失。

**追问**：

1. vendor 拆太细为什么更慢？→ 请求数上升，共享模块被复制进多个 chunk 重复下载，单 chunk 命中率也不一定更高。
2. `manualChunks` 和 `splitVendorChunkPlugin` 怎么选？→ 后者自动拆 node_modules 省事但粗，前者可控但要维护映射。
3. 怎么确认分包生效？→ 看 dist 与 chunk 报告，确认业务 chunk 里没有 react 源码。
