---
title: [BLD-151] SWC transform API 实战：.swcrc 的 jsc 核心配置与 jest 集成。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-151：SWC transform API 实战：.swcrc 的 jsc 核心配置与 jest 集成。
**答**：
- 核心结构：`jsc.parser`（syntax: typescript/ecmascript + tsx/decorators）、`jsc.transform`（react.runtime、legacyDecorator、optimizer.globals? 即 define 替代）、`jsc.target`（输出目标）、`minify`（布尔/选项）。
- programmatic API：`transformSync(code, options)` 与 `transformFileSync`；Next.js/Rspack/swc-loader 都是这层 API 的封装；`jsc.transform.optimizer.globals` 提供 DefinePlugin 式替换。
- jest 集成：`@swc/jest` 直接替换 babel-jest（transform 配置传 `.swcrc` 等价 options）；monorepo 里注意 `moduleDirectories` 与 `moduleNameMapper` 仍归 jest 管，swc 只管单文件转译。
- 与 babel 生态的兼容边界：官方 preset（env/typescript/react）概念等价，但**自定义 babel 插件不可用**（wasm swc-plugin 是另一套 API）。

```json
// .swcrc：核心配置全貌
{
  "$schema": "https://swc.rs/schema.json",
  "jsc": {
    "parser": {
      "syntax": "typescript",
      "tsx": true,
      "decorators": true,
      "dynamicImport": true
    },
    "transform": {
      "react": { "runtime": "automatic", "importSource": "react" },
      "legacyDecorator": true,
      "decoratorMetadata": true,
      "optimizer": {
        "globals": {
          "vars": { "__APP_VERSION__": "'1.2.3'" }     // 等价 DefinePlugin
        },
        "simplify": true
      }
    },
    "target": "es2020",
    "loose": false,
    "externalHelpers": true       // 等价 transform-runtime：helper 从 @swc/helpers 引用而非内联
  },
  "module": { "type": "es6" },
  "minify": false
}
```

```javascript
// 1) programmatic：直接调 transform API（自定义脚手架/分析器常用）
const { transformSync } = require('@swc/core');
const out = transformSync(source, {
  filename: 'app.tsx',
  jsc: { parser: { syntax: 'typescript', tsx: true }, target: 'es2020' },
});
console.log(out.code, out.map);

// 2) jest 集成：jest.config.js
module.exports = {
  transform: {
    '^.+\\.(t|j)sx?$': ['@swc/jest', {
      jsc: { parser: { syntax: 'typescript', tsx: true }, target: 'node18' },
      module: { type: 'commonjs' },        // jest 需要 cjs（或配 ESM 实验模式）
    }],
  },
  // babel-jest → @swc/jest 提速 5-20x（大仓 jest 初始化时间显著下降）
};
```
