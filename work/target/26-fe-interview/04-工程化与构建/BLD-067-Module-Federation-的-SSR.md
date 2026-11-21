---
title: [BLD-067] Module Federation 的 SSR 限制是什么？有哪些缓解方案？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-067：Module Federation 的 SSR 限制是什么？有哪些缓解方案？
**答**：
- 本质问题：MF 依赖浏览器端动态加载（remoteEntry + 动态 import），Node 端 SSR 要求"同步 require 已知模块"，模型冲突。
- webpack 5 的 ModuleFederationPlugin 提供了 server 端支持（target: node、libraryTarget commonjs-module），但 host 与 remote 需在同进程（通过内部请求或本地引用），跨网络容器仍无标准协议。
- 缓解方案一：SSR 时只渲染 host 部分，远端模块 CSR 水合（牺牲 SEO）。
- 方案二：Node 端用 @module-federation/enhanced / module-federation-dts + 联邦服务（如 @module-federation/node）实现服务间拉取。
- 方案三：SSR 渲染时改为"HTML 片段集成"（原生 ESM/iframe 混合），仅客户端用 MF。

```javascript
// webpack.server.config.js：Node 端联邦配置（同进程方案）
const { ModuleFederationPlugin } = require('webpack').container;

module.exports = {
  target: 'node',
  output: { libraryTarget: 'commonjs-module' },
  plugins: [
    new ModuleFederationPlugin({
      name: 'ssrHost',
      library: { type: 'commonjs-module' },
      remotes: {
        // Node 侧：容器从本地构建产物加载（同进程）
        shopRemote: 'shopRemote@./remote/ssrRemoteEntry.js',
      },
      shared: {
        react: { singleton: true, eager: true }, // 服务端必须 eager 避免异步协商
      },
    }),
  ],
};

// server.js（text 代码块）：
// SSR 渲染前先显式初始化容器
// await __webpack_init_sharing__('default');
// const container = window 不可用 -> 需要 module-federation/node 桥接
// const remote = await loadRemoteModule({ remoteName: 'shopRemote', module: './ProductList' });
```
