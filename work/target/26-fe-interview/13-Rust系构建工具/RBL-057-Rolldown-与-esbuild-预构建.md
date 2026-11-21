---
title: [RBL-057] Rolldown 在 Vite 中如何接管 esbuild 的预构建？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-057：Rolldown 在 Vite 中如何接管 esbuild 的预构建？
**答**：
- 旧 Vite 的依赖预构建（optimizeDeps）用 esbuild 把 node_modules 里的 CJS/散装 ESM 预打成单文件浏览器可用包；rolldown-vite 里这个环节换成 rolldown。
- 收益：预构建速度与 esbuild 同量级（oxc_transformer 比 esbuild transform 更快部分场景），并且预构建产物与 prod 打包共用同一内核语义，减少 dev/prod 差异。
- 行为变化：optimizeDeps 的 esbuildOptions 迁移到 rolldownOptions；部分 esbuild 专属字段（define 全局注入写法）有对应映射。
- 冷启动链路：扫描 import（rolldown 的 scanner）→ 确定依赖清单 → rolldown 预构建到 node_modules/.vite/deps → 缓存，lockfile/config 变更自动失效。
- 调试：vite optimize 命令可单独跑预构建；--force 强制重建。
- 追问钩子：rolldown-vite 目前主要变化在 dev 预构建与 prod 打包器替换，HTML/CSS 处理等 vite 特有管线由 vite 层适配。

```javascript
// rolldown-vite 的 vite.config.ts
import { defineConfig } from 'rolldown-vite'; // 换 import 即可
export default defineConfig({
  optimizeDeps: {
    include: ['react', 'react-dom', 'lodash-es'],
    // rolldownOptions: {...}  // 替代旧 esbuildOptions
  },
  build: { minify: true }, // 默认用 oxc 压缩
});
```
