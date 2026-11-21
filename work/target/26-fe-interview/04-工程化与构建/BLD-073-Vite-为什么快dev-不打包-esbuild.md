---
title: [BLD-073] Vite 为什么快？dev 不打包、esbuild 预构建、原生 ESM 按需编译分别指什么？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-073：Vite 为什么快？dev 不打包、esbuild 预构建、原生 ESM 按需编译分别指什么？
**答**：
- dev 阶段不打包：浏览器请求到哪个模块，Vite 才 transform 哪个（按需、单文件粒度），启动时间与项目模块总数解耦。
- 原生 ESM：直接复用浏览器 import 图，路由懒加载天然分摊请求，首屏只加载用到的模块。
- esbuild 预构建：node_modules 的 CJS/多入口依赖在启动前用 esbuild 打成单个 ESM 文件（Go 并行，比 babel/webpack 快 10-100 倍），同时合并请求防瀑布。
- 缓存：预构建结果缓存到 node_modules/.vite，二次启动几乎瞬时。
- 原理记忆：webpack dev = "先整图打包再服务"；Vite dev = "按需转译 + 服务原生 ESM"。

```javascript
// vite.config.js：与"为什么快"对应的三个配置锚点
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  optimizeDeps: {
    // 预构建范围：默认扫描入口自动发现 可显式补充扫描不到的（动态拼接 import）
    include: ['lodash-es', 'axios'],
    esbuildOptions: { target: 'esnext' }, // 预构建产物的目标
  },
  server: {
    fs: { strict: true },
  },
});

// text 代码块：dev 请求模型对比
// webpack：浏览器请求 bundle.js（服务端已打包全量模块图）-> 慢启动 快运行
// vite：浏览器请求 index.html -> 沿 import 逐个请求 /src/main.js /src/App.vue /node_modules/.vite/deps/react.js
//       每个文件只有单文件 transform 开销 -> 快启动 慢请求（海量小请求由 HTTP2 缓解）
```
