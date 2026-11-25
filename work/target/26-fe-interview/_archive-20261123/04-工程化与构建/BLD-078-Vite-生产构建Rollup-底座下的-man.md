---
title: [BLD-078] Vite 生产构建：Rollup 底座下的 manualChunks 分包实践。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-078：Vite 生产构建：Rollup 底座下的 manualChunks 分包实践。
**答**：
- 生产构建 = Rollup：build.rollupOptions.output.manualChunks 自定义分组；推荐"函数式"按 id 归组，比对象式可控。
- 生态动向（2025-2026 新考点）：Vite 团队用 Rust 重写的 Rolldown（基于 oxc）正逐步接管生产构建，`rolldown-vite` 已可作为替换包试用，后续大版本默认切换—— Rolldown 兼容 Rollup 插件 API 与 manualChunks 语义，迁移成本低；面试提到"Vite dev 用 esbuild、build 用 Rollup"时，能补一句 Rolldown 正在统一两者（构建期与压缩都用 Rust 链路）是显著加分项。
- 策略：框架层（react/vue + router/状态）一组享最长缓存；UI 库一组；异步大库（echarts/编辑器）不进 manualChunks，让它们随动态 import 自然成 chunk。
- 坑：manualChunks 把"仅被一个异步页用到的库"也抽成公共 chunk，导致首屏多加载——要按引用路径判断；rollup 下 minSize 等语义与 webpack 不同。
- 构建报告：build: { rollupOptions } + rollup-plugin-visualizer 输出 treemap。

```javascript
// vite.config.js：manualChunks 实践
import { defineConfig } from 'vite';
import { visualizer } from 'rollup-plugin-visualizer';

export default defineConfig({
  build: {
    target: 'es2020',
    chunkSizeWarningLimit: 800,
    rollupOptions: {
      output: {
        manualChunks(id) {
          if (!id.includes('node_modules')) {
            return undefined; // 业务代码不手动分 让路由动态 import 决定
          }
          if (/react|react-dom|scheduler|react-router/.test(id)) return 'vendor-react';
          if (/echarts|zrender/.test(id)) return undefined; // 异步页独享 让 import 自然分割
          if (/[\\/]node_modules[\\/]/.test(id)) return 'vendors';
        },
        entryFileNames: 'js/[name].[hash].js',
        chunkFileNames: 'js/[name].[hash].js',
        assetFileNames: 'assets/[name].[hash].[ext]',
      },
    },
  },
  plugins: [
    visualizer({ filename: 'dist/report.html', gzipSize: true }),
  ],
});
```
