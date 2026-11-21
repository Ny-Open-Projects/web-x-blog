---
title: [BLD-084] SWC 是什么？与 Babel 的对比与 .swcrc 怎么写？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-084：SWC 是什么？与 Babel 的对比与 .swcrc 怎么写？
**答**：
- SWC：Rust 编写的可扩展 TS/JS 编译器与压缩器，提供 SWC 核心库（@swc/core）、CLI、swc-loader（webpack）、Next.js 默认编译器。
- 对比 babel：API 对等（parse/transform/minify），速度快 20~70 倍；preset-env 等价物是 env 选项；插件生态弱（Rust WASM 插件门槛高，ECMA 提案类插件不如 babel 丰富）。
- .swcrc：与 babel 配置结构神似——test、jsc.parser/ts/transform、env.targets、minify。
- 选型：新项目优先 SWC（Next/Vite 均内置），需要深度 AST 插件时留 babel 兜底（可混用：SWC 语法降级 + babel 细粒度插件）。

```json
// .swcrc：完整配置示例
{
  "test": ".*\\.tsx?$",
  "jsc": {
    "parser": {
      "syntax": "typescript",
      "tsx": true,
      "decorators": true,
      "dynamicImport": true
    },
    "transform": {
      "react": { "runtime": "automatic", "importSource": "react" },
      "legacyDecorator": true
    },
    "target": "es2020",
    "loose": false,
    "externalHelpers": true
  },
  "module": { "type": "es6" },
  "minify": false,
  "env": {
    "targets": { "chrome": "87" },
    "mode": "usage",
    "coreJs": "3.36"
  }
}
```

```javascript
// webpack.config.js：swc-loader 替代 babel-loader
module.exports = {
  module: {
    rules: [{
      test: /\.(js|jsx|ts|tsx)$/,
      include: /src/,
      use: [{
        loader: 'swc-loader',
        options: { sync: false }, // 复杂配置走 .swcrc 简单配置可内联
      }],
    }],
  },
  cache: { type: 'filesystem' },
};
```
