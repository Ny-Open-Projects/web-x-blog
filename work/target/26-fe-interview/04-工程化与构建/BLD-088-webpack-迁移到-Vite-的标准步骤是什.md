---
title: [BLD-088] webpack 迁移到 Vite 的标准步骤是什么？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-088：webpack 迁移到 Vite 的标准步骤是什么？
**答**：
- 步骤一：入口改造——HTML 模板换成 Vite 的 index.html（`<script type="module" src="/src/main.js">`），删 webpack 的 html-webpack-plugin 模板语法。
- 步骤二：配置翻译——alias/extensions/proxy/define 对齐；babel/polyfill 配置迁到 build.target；loader（less/sass/postcss）用 Vite 内置能力替代。
- 步骤三：插件替换——DefinePlugin → define、CopyPlugin → public 目录或 viteStaticCopy、环境变量 VUE_APP_*/REACT_APP_* → VITE_*（批量重命名 + 全局替换）。
- 步骤四：预构建调优——include 补动态 import 依赖、处理 CJS 包互操作；最后跑全量功能回归（路由懒加载、worker、动态 import）与 build 产物 diff。

```javascript
// vite.config.js：迁移期兼容配置（常见翻译项集中展示）
import { defineConfig } from 'vite';
import { viteStaticCopy } from 'vite-plugin-static-copy';
import legacy from '@vitejs/plugin-legacy';

export default defineConfig({
  resolve: {
    // 原 webpack resolve.alias 翻译
    alias: { '@': '/src', '@assets': '/src/assets' },
  },
  server: {
    // 原 devServer.proxy 翻译
    proxy: { '/api': { target: 'http://backend:7001', changeOrigin: true } },
  },
  define: {
    // 原 DefinePlugin 翻译 注意 process.env 形态
    'process.env.NODE_ENV': JSON.stringify(process.env.NODE_ENV),
    __VERSION__: JSON.stringify(require('./package.json').version),
  },
  optimizeDeps: {
    // 原 webpack 的 CJS 依赖显式进预构建 防运行时 504
    include: ['lodash', 'qs', 'js-cookie'],
  },
  build: { target: 'chrome87', // 替代 babel targets + core-js
    rollupOptions: { output: { manualChunks: undefined } } },
  plugins: [
    viteStaticCopy({ targets: [{ src: 'public/robots.txt', dest: '.' }] }),
    legacy({ targets: ['chrome >= 87'] }), // 低版本兜底
  ],
});
```
