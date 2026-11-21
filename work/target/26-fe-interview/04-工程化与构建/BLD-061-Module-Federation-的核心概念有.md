---
title: [BLD-061] Module Federation 的核心概念有哪些？host/remote/exposed/shared/remotes 分别是什么？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-061：Module Federation 的核心概念有哪些？host/remote/exposed/shared/remotes 分别是什么？
**答**：
- host：消费方，页面外壳，声明 remotes（要引用哪些远端）与 shared（可与远端共享的依赖）。
- remote：提供方，声明 exposes（对外暴露的模块路径映射）与 filename（打包出的容器入口 containerEntry）。
- exposed：remote 暴露的"模块"（不是整页应用），host 按路径异步拉取。
- shared：双方声明共同依赖（如 react），运行时协商用哪个版本，避免重复下载与实例不一致。
- 运行时本质：MF 把 webpack 模块图拆到多个可独立部署的容器里，通过 container reference 在浏览器端动态连接（remoteEntry.js + 动态 script 加载模块）。

```javascript
// remote 端 webpack.config.js
const { ModuleFederationPlugin } = require('webpack').container;

module.exports = {
  plugins: [
    new ModuleFederationPlugin({
      name: 'shopRemote',
      filename: 'remoteEntry.js',                 // 容器入口
      exposes: {
        './ProductList': './src/components/ProductList.vue',
        './CartButton': './src/components/CartButton.jsx',
      },
      shared: {
        react: { singleton: true, requiredVersion: '^18.0.0' },
        'react-dom': { singleton: true },
        vue: { singleton: true },
      },
    }),
  ],
};
```
