---
title: [RBL-086] Turbopack 如何处理 webpack loader 生态？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-086：Turbopack 如何处理 webpack loader 生态？
**答**：
- 官方内置：常用转换（TS/JSX、PostCSS、Tailwind、sass/less）由 Turbopack 内部（SWC + 内置工具链）直接实现，覆盖 Next 项目绝大多数 loader 场景。
- 兼容机制：turbo.rules 里可挂 loader（如 @svgr/webpack），Turbopack 通过 JS loader 桥执行 webpack 风格 loader，但只支持子集（无完整的 webpack loader this 上下文）。
- 不可用项：依赖 webpack compiler/compilation 的插件完全不可用；依赖冷门 loader 特性（pitch、this.query 深度定制）的 loader 需要改造。
- 迁移建议：先把 Next 项目里 webpack 配置清单化（Next 团队提供了不支持的 feature 列表），逐项找 Turbopack 等价物；没有等价物的功能要评估放弃或改造。
- 性能注意：JS loader 桥同样是跨界开销，能用内置就不挂自定义 loader。
- 追问钩子：Turbopack 不追求 webpack 兼容是"刻意的"——它押注框架层吸收复杂度，把通用性让给 Rspack/Rolldown。

```javascript
// next.config.js：Turbopack 的 loader 配置范式
module.exports = {
  experimental: {
    turbo: {
      rules: {
        // 内置覆盖不了的，挂 webpack 风格 loader（子集兼容）
        '*.svg': { loaders: ['@svgr/webpack'], as: '*.js' },
      },
    },
  },
};
// 兼容判定：loader 是否依赖 webpack 特有 this API
// - 仅用 content/resource → 大概率可用
// - 用 this.emitFile / compilation → 不可用
```
