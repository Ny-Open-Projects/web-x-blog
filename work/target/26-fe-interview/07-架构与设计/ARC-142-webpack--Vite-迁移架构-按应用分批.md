---
title: [ARC-142] webpack → Vite 迁移架构（按应用分批）如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-142：webpack → Vite 迁移架构（按应用分批）如何设计？
**答**：
- 分批单位是"应用"而不是"整个 monorepo"：先选独立工具型小应用试点（验证链路、沉淀 preset），再迁业务应用，最后统一移除 webpack——不同构建器共存期靠包导出与 CI 隔离。
- 配置收敛：抽 `@corp/vite-preset`（alias、环境变量、插件、postcss、构建优化统一内置），应用侧配置只剩几行——迁移的过程也是配置治理的过程。
- 兼容点清单：环境变量前缀（VITE_）、require 语法、CommonJS 依赖预构建（optimizeDeps include）、特殊 loader 的 Vite 等价物（svg sprite/global sass 注入）。
- 双跑验证：迁移分支用两套构建产物跑视觉回归与关键 E2E，产物一致性确认后才切流水线；保留 webpack 分支随时可回退。

```typescript
// @corp/vite-preset：统一配置收敛，应用侧一行接入
import { defineConfig, mergeConfig, type UserConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { visualizer } from 'rollup-plugin-visualizer';

export function corpPreset(appName: string, overrides: UserConfig = {}): UserConfig {
  const base: UserConfig = {
    plugins: [react(), visualizer({ emit: true })],
    resolve: {
      alias: {                                  // 与原 webpack alias 一一映射（迁移清单核对）
        '@': '/src',
        '@corp/ui': resolveMonorepo('packages/ui'),
      },
    },
    server: { proxy: { '/api': { target: 'http://localhost:8080', changeOrigin: true } } },
    build: {
      target: 'es2018',
      rollupOptions: { output: { manualChunks: vendorSplit } },   // 与原 webpack splitChunks 对齐
    },
  };
  return mergeConfig(base, overrides);
}
// 应用侧 vite.config.ts：
// export default defineConfig(corpPreset('mall-web'));
// 迁移双跑验证：
//   webpack 分支 + vite 分支各构建一次 → 视觉回归截图对比 + E2E 冒烟
//   通过 → CI 切换 vite 构建，webpack 配置标记 deprecated 一个版本后删除
```
