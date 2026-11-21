---
title: [BLD-154] Farm、Mako 等新兴构建工具的定位与现状。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-154：Farm、Mako 等新兴构建工具的定位与现状。
**答**：
- **Farm**（Rust，曾名 Farmer）：对标"全栈一体化"——dev 走无打包按需编译 + Rust 持久缓存，build 也用同一引擎（Vite 的双引擎问题的解法），插件 API 兼容部分 rollup/vite 钩子；CNCF? 国内生态（字节系活跃）。
- **Mako**（蚂蚁，基于 Rust + snowpack 思路演进）：以 antd/umi 生态切入，强调"配置即默认最优"，内置 CSS/压缩/降级链路；与 umi 深度绑定。
- 共同趋势：Rust 内核 + 按需 dev + 同引擎 build + 部分生态兼容层；但都面对 rollup/webpack 插件生态兼容这道天花板——选型看团队框架（umi 选 Mako、独立项目看 Farm/Vite+Rolldown）。
- 面试答法：不背版本号，讲"评估新工具的三维"——引擎一致性（dev/prod 同源）、生态兼容（插件/loader/框架插件）、长期维护主体。

```javascript
// farm.config.ts：感受其配置形态（与 vite 对比）
import { defineConfig } from '@farmfe/core';
export default defineConfig({
  compilation: {
    input: { index: './index.html' },
    output: { path: 'dist', filename: '[name]-[hash].[ext]' },
    persistentCache: {                                 // 内置持久缓存（Rust 层实现）
      namespace: 'v1',
      buildDependencies: ['farm.config.ts', 'pnpm-lock.yaml'],
    },
    presetEnv: { options: { targets: 'chrome >= 87' } },  // 内置降级（无需单独插件）
  },
  plugins: ['@farmfe/plugin-react', '@farmfe/plugin-sass'],
  vitePlugins: [],        // 部分 vite 插件兼容层（能力有限，注意甄别）
  server: { hmr: true, port: 9000 },
});
// 评估清单（可复制进选型文档）：
// 1. dev/prod 是否同引擎  2. 框架插件成熟度（react/vue 的 HMR 边界）
// 3. rollup/vite 插件兼容比例  4. 持久缓存正确性（配置变更探测）
// 5. 出事故时的回退路径是否顺畅
```
