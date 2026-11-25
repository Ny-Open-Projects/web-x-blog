---
title: [PER-026] Tree Shaking 的原理是什么？什么情况下会失效？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-026：Tree Shaking 的原理是什么？什么情况下会失效？

**答**：
- 原理：ESM 的 import/export 是**静态结构**，打包器据此做依赖图分析，`usedExports` 标记未使用的导出，压缩器（Terser/esbuild）删除死代码。
- 失效场景：CommonJS 的 `require`（动态不可分析）、`import *` 整体导入、模块有副作用被保守保留。
- `package.json` 的 `sideEffects: false` 告诉打包器"没被引用的文件可以整文件摇掉"；CSS、polyfill 等有副作用的文件要列入白名单。
- 验证方式：生产模式构建后用 `webpack-bundle-analyzer` 或 rollup-plugin-visualizer 看产物构成。

```javascript
// webpack.config.js —— 生产模式开启标记与压缩
module.exports = {
  mode: 'production',
  optimization: {
    usedExports: true,  // 标记未被使用的导出
    minimize: true,     // 压缩时删除被标记的死代码
    splitChunks: { chunks: 'all' }
  }
};

// 生效前提：全量使用 ESM 静态导入；package.json 声明副作用范围
// { "sideEffects": ["*.css", "./src/polyfill.js"] } —— 有副作用的文件必须排除在摇树之外
```
