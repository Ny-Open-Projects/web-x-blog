---
title: [BLD-167] SSR 产物与客户端产物差异：manifest 与资源映射协议。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-167：SSR 产物与客户端产物差异：manifest 与资源映射协议。
**答**：
- 三份产物：**client bundle**（浏览器，含 hydration 逻辑）、**server bundle**（Node，渲染 React/Vue 树，external node_modules）、**manifest**（映射协议：源模块→产物 chunk/css）。
- server bundle 里 `import App from './App'` 需要知道 App 在客户端对应哪个 chunk、依赖哪些 CSS——`ssr-manifest.json`/`webpack manifest`（StatsPlugin）提供 `module.id → chunk files[]` 映射，SSR 渲染时遍历已执行模块收集 `preload <link>` 与关键 CSS 注入 HTML。
- webpack 侧等价物：`webpack-manifest-plugin` + `stats.json`（chunksByModule? 通过 stats 的 modules 字段聚合），React 生态的 loadable-components/babel-plugin-react-loadable 都是这套协议的封装。
- 一致性风险：server 与 client 产物必须**同一次构建产出**（同一 hash 集合），分次构建会造成 hydration 不匹配——CI 上 SSR 项目发布 = client+server+manifest 原子发布。

```javascript
// webpack.ssr.config.js：manifest 协议的生产实现（webpack5）
const { WebpackManifestPlugin } = require('webpack-manifest-plugin');
const { StatsWriterPlugin } = require('webpack-stats-plugin');

module.exports = [
  { // ── client 构建 ──
    name: 'client',
    entry: './src/entry-client.tsx',
    output: { path: 'dist/client', filename: '[name].[contenthash].js', publicPath: '/static/' },
    plugins: [
      new WebpackManifestPlugin({ fileName: 'manifest.json' }),   // 入口级映射
      // stats.json：模块→chunk 映射（SSR 收集 preload/css 用）
      new StatsWriterPlugin({
        filename: '../stats.json',
        stats: { all: false, modules: true, chunks: true, assets: true },
        transform: (data) => JSON.stringify({
          assetsByChunkName: data.assetsByChunkName,
          // 模块级映射：moduleId -> 所属 chunk 产物
          modules: data.modules.map((m) => ({ id: m.id, chunks: m.chunks, name: m.name })),
        }),
      }),
    ],
  },
  { // ── server 构建 ──
    name: 'server',
    entry: './src/entry-server.tsx',
    target: 'node',
    output: { path: 'dist/server', filename: 'server.js', libraryTarget: 'commonjs2' },
    externals: [/^(?!\.|\/)[^/]+$/],    // node_modules 全外部化
    // resolve.alias: { 'loadable-manifest': './dist/client/loadable-stats.json' }
  },
];
// entry-server 内：loadableChunks() 收集渲染中命中的模块 → 查 manifest →
// 产出 { html, preloadTags, cssTags } 注入模板 —— SSR 资源映射协议的闭环
```
