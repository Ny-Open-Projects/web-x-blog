---
title: [BLD-150] esbuild 接入 webpack/vite 做压缩或转译：esbuild-loader 与 minify 的语义差异坑。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-150：esbuild 接入 webpack/vite 做压缩或转译：esbuild-loader 与 minify 的语义差异坑。
**答**：
- 接入方式：webpack 用 **esbuild-loader**（rule 替 babel-loader/ts-loader 做转译；TerserPlugin 位置换 EsbuildPlugin 做压缩）；vite 原生用 esbuild 做**依赖预构建与 TS/JSX 转译**、`build.minify: 'esbuild'` 做压缩。
- **压缩语义差异**：Terser 支持更多精细选项（pure_funcs、mangle properties、keep_classnames、IE 兼容），esbuild minify 选项少且激进——错误上报栈可读性、class/function name（依赖 Function.name 的库！如 Angular、旧的 mobx 装饰器）可能被破坏。
- **转译语义差异**：esbuild 转译只做语法降级+类型剥离，**不注入 helper/polyfill**（目标是 es2015 时 async 会内联 regenerator? 实际 esbuild 会内联 helper 到每个文件，无 transform-runtime 等价物），目标过旧时产物反而膨胀。
- 排错口诀：换 esbuild 后先查 `console.log` 裁剪行为、`Function.name` 依赖、sourcemap 精度（esbuild 的 map 有时行级偏差）。

```javascript
// webpack：esbuild 全家桶接入 + 语义差异防御配置
const { EsbuildPlugin } = require('esbuild-loader');
const webpack = require('webpack');

module.exports = {
  module: {
    rules: [
      {
        test: /\.[jt]sx?$/,
        include: path.resolve('src'),               // 必须 include，别全量过
        loader: 'esbuild-loader',
        options: {
          target: 'es2020',                          // 语法降级目标（注意：不注入 polyfill！）
          loader: 'tsx',
          // 与 babel 的差异防御：需要 helper 复用/老浏览器目标时退回 babel
        },
      },
    ],
  },
  optimization: {
    minimizer: [
      new EsbuildPlugin({
        target: 'es2020',
        css: true,                                   // 同时压缩 css
        // terser 独有能力的缺失应对：
        //   1) pure_funcs：用 esbuild 的 pure 注解代替（源码加 /*#__PURE__*/）
        //   2) keep_fnames：esbuild 无等价物 → 依赖 Function.name 的代码改显式命名
        drop: ['console', 'debugger'],               // 裁剪能力（等价 drop_console）
      }),
    ],
  },
  plugins: [
    // esbuild 不做 polyfill → API 垫片交给 core-js 手动入口：
    new webpack.ProvidePlugin({}),   // 或 entry 首行 import 'core-js/stable'（按 browserslist 取舍）
  ],
};
// vite 侧：
// build: { minify: 'esbuild' }    默认即是；要 terser 语义时改 'terser'（构建变慢数倍）
```
