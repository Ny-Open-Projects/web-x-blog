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

**追问**：

1. 依赖预构建什么时候要手动 `--force` 重跑？→ 新增依赖、lockfile 变化、`optimizeDeps` 配置改动后缓存 key 失配时；动态拼接的 import（`import('./views/' + name)`) 扫描不到，必须写进 `include`。
2. dev 已经够快了，为什么生产还要打包？→ 生产要 tree-shaking、压缩、chunk 拆分为长缓存、以及语法降级，原生 ESM 在窄带与多模块场景下会产生海量请求。
3. 海量小请求在 dev 环境怎么缓解？→ 预构建把依赖合并成一个文件、HTTP/2 多路复用、源码请求走 `304`/强缓存并只用 `?t=` 破变更文件；深层目录宜用扁平化 alias 减少解析链。
