---
title: [RBL-090] Next.js 的 turbo.rules 配置有哪些常用写法？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-090：Next.js 的 turbo.rules 配置有哪些常用写法？
**答**：
- rules 结构：glob 模式 → { loaders: [...], as: '目标模块类型' }；loaders 为 webpack 风格 loader（兼容子集），as 决定该文件被当作什么模块处理。
- 常用一：SVG 转 React 组件——'*.svg': { loaders: ['@svgr/webpack'], as: '*.js' }。
- 常用二：MDX/自定义 DSL——挂 @mdx-js/loader；需要 options 时用 { options: {...} } 形式。
- resolveAlias/resolveExtensions：对应 webpack 的 resolve.alias/extensions，写法收敛（别名值为相对路径字符串）。
- 与 webpack 配置互斥：启用 Turbopack 后 webpack() 函数配置不再生效，必须迁移到 turbo 字段。
- 追问钩子：rules 的匹配是 glob 而非 webpack 的正则 test，写法迁移时注意 './src/**/*.mdx' 风格。

```javascript
// next.config.js
module.exports = {
  experimental: {
    turbo: {
      rules: {
        '*.svg': { loaders: ['@svgr/webpack'], as: '*.js' },
        './src/**/*.mdx': {
          loaders: [{ loader: '@mdx-js/loader', options: { jsx: true } }],
          as: '*.tsx',
        },
      },
      resolveAlias: { '@/components': './src/components' },
      resolveExtensions: ['.tsx', '.ts', '.jsx', '.js', '.json'],
    },
  },
};
```
