---
title: [RBL-015] Rspack 如何支持 Module Federation？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-015：Rspack 如何支持 Module Federation？
**答**：
- 一等支持：@rspack/core 内置 container 模块类型与 ModuleFederationPlugin（与 webpack 版配置同构），shared 依赖的版本协商 runtime 在 Rust 侧实现。
- 适用场景：微前端"运行时共享模块"、跨团队组件按需加载；Rspack 的价值是宿主与远端的构建速度同时受益。
- 配置平移：name/filename/exposes/remotes/shared 原样迁移；注意 shared 的 singleton/requiredVersion/eager 语义需逐项验证，特别是 react 单例。
- 已知差异：加载时序相关的边界行为（如 remote 初始化失败的降级）、部分 stats 输出格式有差异，灰度期要做联邦加载链路的 E2E。
- 与 rollup 系工具的对比：MF 是 webpack 系独有的运行时共享协议，这也是很多存量微前端团队绑定 Rspack 而非 Rolldown 的原因之一。
- 追问钩子：MF2.0（module-federation/enhanced）的 runtime 插件体系 Rspack 也在跟进，迁移时确认版本。

```javascript
// rspack.config.js（宿主）
const { ModuleFederationPlugin } = require('@rspack/core').container;
module.exports = {
  plugins: [new ModuleFederationPlugin({
    name: 'host',
    remotes: { shop: 'shop@https://cdn.example.com/shop/remoteEntry.js' },
    shared: {
      react: { singleton: true, eager: true, requiredVersion: '^18' },
      'react-dom': { singleton: true },
    },
  })],
};
// 远端 exposes: { './Page': './src/Page.tsx' }
```
