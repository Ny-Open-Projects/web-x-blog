---
title: [BLD-052] 从 webpack 4 升级到 5 有哪些实测收益？升级要动哪些点？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-052：从 webpack 4 升级到 5 有哪些实测收益？升级要动哪些点？
**答**：
- 实测收益项：持久缓存（二次构建快 60%~90%）、asset modules 砍掉 file/url-loader 链、node polyfill 移除后包更小、terser 分阶段缓存、Deterministic ids 缓存更稳。
- 破坏性变更：Node 10.13+ 要求、`module`/`mainFields` 行为微调、polyfill 自动注入被移除（需显式 fallback）、loaders 中 fs 路径改、`optimization.hashedModuleIds` 改 `moduleIds: 'deterministic'`、output.filename 不再自动加 hash。
- 迁移路径：先跑 `npx webpack-cli migrate` 自动改配置，再处理 deprecation 警告（指向未来 webpack 6 的 API，如 stage 钩子）。

```javascript
// webpack.config.js：webpack 5 迁移对照片段
module.exports = {
  // webpack4: node: { fs: 'empty', dgram: 'empty' }
  // webpack5: polyfill 不再自动注入 需要显式声明
  resolve: {
    fallback: { path: false, fs: false }, // 或 path-browserify 等 polyfill 包
  },
  optimization: {
    // webpack4: hashedModuleIds: true
    moduleIds: 'deterministic',
  },
  module: {
    rules: [
      // webpack4: url-loader + limit
      // webpack5: asset modules（见 BLD-024）
      { test: /\.(png|jpg)$/i, type: 'asset', parser: { dataUrlCondition: { maxSize: 8 * 1024 } } },
    ],
  },
  plugins: [
    // webpack4: NamedModulesPlugin
    // webpack5: 内建
    // new (require('webpack').NamedModulesPlugin)(),  // 已移除
  ],
};

// bash 代码块：官方迁移命令
// npx webpack-cli migrate webpack.config.js
// npx webpack --watch   # 观察 deprecation 警告逐条清理
```

## 第八章 性能优化之产物体积（BLD-053 ~ BLD-060）
