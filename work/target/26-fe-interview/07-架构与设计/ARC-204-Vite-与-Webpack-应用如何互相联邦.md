---
title: [ARC-204] Vite 与 Webpack 应用如何互相联邦？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-204：Vite 与 Webpack 应用如何互相联邦？
**答**：
- 1.0 时代 Vite 与 Webpack 联邦基本不可行（产物协议不同：Vite 是 ESM 原生导入，Webpack 是自己的 runtime require）。2.0 运行时统一了加载协议，跨构建器互联成为官方能力。
- 关键做法：Vite 侧用 vite-plugin-federation（或 rspack 的 enhanced 产物），expose 输出符合联邦运行时约定的模块；Webpack 侧通过 runtime 的 manifest 加载，不感知对方用什么构建器。
- 两个落地条件：exposed 模块必须是"纯 ESM 可静态分析"的产物；shared 依赖协商要求双方都接入同一运行时（@module-federation/runtime），不能各用各的 share-scope。
- 风险边界：dev 模式（无构建产物）跨构建器联邦不可靠，联调建议走"本地 dev + 远端 stage 产物"的混合模式。

```javascript
// Vite 子应用（vite.config.ts）
import federation from '@originjs/vite-plugin-federation';
export default {
  plugins: [federation({
    name: 'vite-app',
    filename: 'remoteEntry.js',
    exposes: { './Card': './src/components/Card.vue' },
    shared: ['vue'],
  })],
};
// Webpack 主应用：不写 remote 配置，改用 2.0 runtime 按 manifest 加载
import { registerRemotes } from '@module-federation/enhanced/runtime';
registerRemotes([{ name: 'vite-app', entry: 'https://cdn.example.com/vite-app/mf-manifest.json' }]);
// 组件内：const Card = defineAsyncComponent(() => import('vite-app/Card'));
```
