---
title: [BLD-166] publicPath 运行时注入：__webpack_public_path__ 与动态 CDN 场景。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-166：publicPath 运行时注入：__webpack_public_path__ 与动态 CDN 场景。
**答**：
- 静态 publicPath 写死在 runtime 的 `__webpack_require__.p`；**运行时注入**解决"同一份产物发到多环境/多 CDN"：入口**最顶部**（任何 import 生效前）执行 `__webpack_public_path__ = window.__CDN__`——必须在 webpack 处理的第一个模块里，因为 `.p` 在模块加载前就可能被动态 import 读取。
- webpack5 的 `output.publicPath: 'auto'`：从 `document.currentScript.src` 自动推导（AutoPublicPathRuntimeModule），多 CDN 域名场景天然适配；SSR 下无 document，需要手动注入。
- 动态 CDN 进阶：按 chunk 维度分流（`chunkLoadingGlobal` + 自定义 loadScript、或插件改写 `__webpack_require__.p` 为函数化? 常规做法是 publicPath 用相对路径 + 前端网关重写）。
- 坑：`__webpack_public_path__` 赋值写在 `import` 之后的模块里会失效（模块加载顺序）；ESM 严格模式下它是 webpack 定义的 free var，TS 需要 `declare` 声明。

```javascript
// webpack.config.js
module.exports = {
  output: {
    publicPath: 'auto',       // 运行时自动推导（推荐）；或 '/' 静态默认
    crossOriginLoading: 'anonymous', // CDN 场景必配（错误上报需要跨域脚本栈）
  },
};
```

```typescript
// src/public-path.ts：必须是构建处理的第一个模块（entry 数组第一项）
// webpack.config.js entry: ['./src/public-path', './src/index']
declare const __webpack_public_path__: string;
// 方案一：部署平台注入的 window 变量（同产物多环境）
__webpack_public_path__ = (window as any).__CDN_BASE__ ?? '//cdn.example.com/static/';
// 方案二：currentScript 推导（auto 模式的手动版，兼容场景用）
// const cur = (document.currentScript as HTMLScriptElement)?.src;
// __webpack_public_path__ = cur?.slice(0, cur.lastIndexOf('/') + 1) ?? '/';

// webpack.config.js 的 entry 保证顺序：
// entry: { main: ['./src/public-path.ts', './src/main.tsx'] }
// 产物运行时对应：__webpack_require__.p = window.__CDN_BASE__
// 之后所有 chunk/worker/动态 import 都从注入的 CDN 基址拉取——一份产物多环境发布的核心机制
```
