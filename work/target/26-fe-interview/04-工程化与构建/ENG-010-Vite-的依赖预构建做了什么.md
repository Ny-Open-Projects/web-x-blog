---
title: [ENG-010] Vite 的依赖预构建做了什么？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-010：Vite 的依赖预构建做了什么？
**答**：
- 启动时扫描入口，收集所有裸模块导入，交给 esbuild 预构建。
- 作用一：把 CJS/UMD 依赖转换成 ESM，浏览器才能直接 import。
- 作用二：把 lodash-es 这类几百个小文件合并成单文件，减少请求数量。
- 预构建产物缓存在 node_modules/.vite，依赖锁文件或配置变化时才重新构建。

```javascript
// vite.config.ts
import { defineConfig } from 'vite';

export default defineConfig({
  optimizeDeps: {
    // 手动指定需要预构建的依赖
    include: ['react', 'react-dom', 'lodash-es'],
    // 链接的本地包不需要预构建
    exclude: ['linked-local-package'],
    // 强制重新预构建（排查缓存问题时使用）
    force: true,
  },
});
```
