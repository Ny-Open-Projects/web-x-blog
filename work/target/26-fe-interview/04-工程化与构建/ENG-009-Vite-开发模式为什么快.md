---
title: [ENG-009] Vite 开发模式为什么快？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-009：Vite 开发模式为什么快？
**答**：
- dev 阶段完全不打包：利用浏览器原生 ESM，请求哪个模块就按需编译返回哪个。
- 源码模块由 esbuild 转译（TS/JSX），速度远超 Babel；依赖则在启动时预构建进缓存。
- HMR 精确到模块级：改一个文件只让该模块失效，不再像 webpack 一样按 entry 重算模块图。
- 项目越大启动优势越明显，因为冷启动工作量与页面首屏需要的模块数成正比，与全项目体积无关。

```javascript
// vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
  },
  optimizeDeps: {
    // 提前把深层依赖纳入预构建，减少首屏请求瀑布
    include: ['lodash-es'],
  },
});
```
