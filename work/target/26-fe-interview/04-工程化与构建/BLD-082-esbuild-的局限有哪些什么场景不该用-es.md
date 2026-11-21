---
title: [BLD-082] esbuild 的局限有哪些？什么场景不该用 esbuild？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-082：esbuild 的局限有哪些？什么场景不该用 esbuild？
**答**：
- 无 JS 级插件系统：扩展必须写 Go（esbuild 原生插件），JS API 只能做 onResolve/onLoad 级别的有限拦截——复杂 AST 级变换做不了（对比 babel/rollup 插件生态）。
- 降级能力有限：不支持旧于 es5 的 target（无 IE 支持），语法降级不如 @babel/preset-env 全；polyfill 不自动注入（只有有限 builtin 降级）。
- code splitting 有限：仅 ESM 输出、动态 import 才分 chunk，无 webpack 级 splitChunks 策略；HMR、loader 生态缺失。
- 结论：适合"语法转换、压缩、预构建、库打包（tsup）"，不适合需要重插件/旧浏览器兼容/HMR 的完整应用构建（这正是 Vite dev 用 esbuild、build 用 Rollup 的原因）。

```javascript
// esbuild 有限扩展能力示例：onLoad 拦截（非 AST 级）
const esbuild = require('esbuild');

esbuild.build({
  entryPoints: ['src/index.ts'],
  bundle: true,
  outdir: 'dist',
  plugins: [{
    name: 'env-virtual',
    setup(build) {
      // 只能拦截"解析与加载" 不能进入 AST 内部做细粒度变换
      build.onLoad({ filter: /\.env$/ }, (args) => ({
        contents: `export default ${JSON.stringify(process.env.APP_ENV)}`,
        loader: 'js',
      }));
      // 想做 AST 级变换（如替换类名、i18n）只能正则粗处理 或换 babel/rollup
      build.onLoad({ filter: /special\.js$/ }, (args) => ({
        contents: require('fs').readFileSync(args.path, 'utf-8').replace('__NAME__', '"app"'),
        loader: 'js',
      }));
    },
  }],
});
```
