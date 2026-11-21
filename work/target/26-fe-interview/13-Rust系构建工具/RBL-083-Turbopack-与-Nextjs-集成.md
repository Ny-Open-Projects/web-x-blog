---
title: [RBL-083] Turbopack 与 Next.js 是如何集成的？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-083：Turbopack 与 Next.js 是如何集成的？
**答**：
- 开关方式：next dev --turbo（或 next.config 里 experimental.turbo）启用 Turbopack dev；生产构建在较新版本逐步开放（next build --turbo）。
- 配置位置：webpack 配置不生效，改用 `turbo` 字段（rules/resolveAlias/resolveExtensions），语义与 webpack rules 类似但更收敛。
- 深度集成：Next 的 RSC（React Server Components）、App Router、字体/图片优化、CSS 管线都是按 Turbopack 任务模型实现的，这是它比通用打包器在 Next 里更快的深层原因。
- 迁移边界：不支持 webpack loader 的全部生态——Turbopack 有自己的 loader 机制（rust loader 与 JS loader），第三方 webpack 插件大多不可用；Next 团队按场景提供替代。
- HMR 与 Fast Refresh：Next 的 Fast Refresh 语义在 Turbopack 上重新实现，功能对齐。
- 追问钩子：为什么只在 Next 生态推？——Turbopack 是"框架专属构建器"，不做通用 webpack 兼容，生态换来了架构自由度。

```javascript
// next.config.js
module.exports = {
  experimental: {
    turbo: {
      rules: {
        '*.svg': { loaders: ['@svgr/webpack'], as: '*.js' }, // loader 配置
      },
      resolveAlias: { '@': './src' },
      resolveExtensions: ['.tsx', '.ts', '.jsx', '.js'],
    },
  },
};
// 启动
// next dev --turbo
```
