---
title: [BLD-082] esbuild 的局限有哪些？什么场景不该用 esbuild？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-082：esbuild 的局限有哪些？什么场景不该用 esbuild？
**答**：
- 插件只能用 JS 写：onResolve/onLoad 只做路径解析与内容加载两层，拿不到 AST，节点级变换做不了（对比 babel/rollup 插件生态）；Go 侧不开放插件钩子，所以"写 Go 扩展"这条路不存在。
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

**追问**：

1. 为什么 esbuild 撑不起一个完整应用的构建？→ 没有 HMR、loader 生态薄弱、code splitting 只认 ESM 动态 import、缺 AST 级插件，按需引入、i18n 提取这类业务定制做不到。
2. tsup（底层用 esbuild）打包库有什么坑？→ 类型声明要另跑 `tsc` 或 `rollup-plugin-dts`，多入口的 CJS/ESM 要分别输出，`external` 默认策略和自己预期不一致时会把 peer 依赖打进产物。
3. 需要兼容老浏览器怎么办？→ esbuild 的 target 只能降到相对新的语法级别，es5 要靠 babel/swc 二次处理，或者直接放弃 IE；这不是配置能绕过的。
