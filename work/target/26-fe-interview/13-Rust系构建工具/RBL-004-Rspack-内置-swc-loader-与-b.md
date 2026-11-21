---
title: [RBL-004] 为什么推荐用 builtin:swc-loader 替代 babel-loader？
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-004：为什么推荐用 builtin:swc-loader 替代 babel-loader？
**答**：
- 性能路径：builtin:swc-loader 是 Rust 内置实现，文件内容不经过 napi FFI 往返、不经过 JS 事件循环，直接在 Rayon 线程池里并行转换；babel-loader 每个文件都要跨边界进 JS 再调用 Babel。
- 实测量级：TSX/TS 转换场景 builtin:swc-loader 通常比 babel-loader 快一个数量级（5~20 倍），模块数越多差距越大。
- 能力覆盖：支持 presets/env targets、部分常见 Babel 插件语义（如装饰器、emotion 的 jsx 处理通过 swc 配置或配合 babel 插件兜底）。
- 兜底策略：遇到 swc 不支持的 Babel 专属插件（如某些自定义宏），可对个别目录降级用 babel-loader，缩小 JS loader 的命中范围。
- 追问钩子：swc-loader（JS 版包装）与 builtin:swc-loader 的区别——前者走 FFI 进 JS 调用 swc-core，后者纯 Rust 内置，后者更快。

```javascript
// rspack.config.js
module.exports = {
  module: {
    rules: [
      {
        test: /\.(ts|tsx|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'builtin:swc-loader',
          options: {
            jsc: {
              parser: { syntax: 'typescript', tsx: true, decorators: true },
              transform: { legacyDecorator: true },
              target: 'es2020',
            },
            env: { targets: 'chrome >= 87', mode: 'usage', coreJs: '3.26' },
          },
        },
        type: 'javascript/auto',
      },
      // node_modules 里部分包若依赖 Babel 宏等，单独降级：
      // { test: /src\/legacy/, use: 'babel-loader' },
    ],
  },
};
```
