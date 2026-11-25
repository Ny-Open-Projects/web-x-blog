---
title: [BLD-045] Vite 与 webpack 的 HMR 本质差异是什么？（先埋个伏笔，详见第十章）
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-045：Vite 与 webpack 的 HMR 本质差异是什么？（先埋个伏笔，详见第十章）
**答**：
- 粒度不同：webpack HMR 以 chunk 为单位重编译（受依赖图影响，改动会重算整条链），Vite 以单模块为单位（ESM import 链精确失效，只重新请求变更模块）。
- 是否打包不同：webpack dev 也是打包后的产物（内存 bundle）；Vite dev 是"未打包"的原生 ESM，浏览器按需发请求，Vite 只做单文件 transform。
- 时间复杂度不同：webpack 与项目规模线性相关（模块图越大编译越慢），Vite dev 启动与项目规模基本解耦（路由级懒加载天然分摊）。
- 相同点：都依赖 websocket 推送、manifest/hash 校验版本、accept 粒度决定冒泡与刷新。
- 生产模式 Vite 仍要打包（用 Rollup），所以"dev 快"不等于"build 快"。

```javascript
// vite.config.js：与 webpack 等价的 HMR 配置（差异对比注释）
import { defineConfig } from 'vite';

export default defineConfig({
  server: {
    hmr: {
      overlay: true,
      // protocol/port 可自定 指向独立 ws 服务
      // clientPort: 443, // 代理场景下 ws 走 https 时需指定
    },
  },
  optimizeDeps: { holdUntilCrawlEnd: true },
});

// text 代码块：两种 HMR 请求模型对比
// webpack dev：
//   页面加载 1 个 bundle.js
//   改模块 A -> 重编译包含 A 的 chunk -> 拉取 A.hot-update.js（chunk 级）
// vite dev：
//   页面加载 main.js -> 浏览器沿 ESM import 请求 /src/A.vue 等上百个模块
//   改模块 A -> 仅失效 A 与其 import 链 -> 浏览器重新请求 /src/A.vue?t=1698（模块级 带时间戳破缓存）
```

## 第七章 性能优化之构建速度（BLD-046 ~ BLD-052）
