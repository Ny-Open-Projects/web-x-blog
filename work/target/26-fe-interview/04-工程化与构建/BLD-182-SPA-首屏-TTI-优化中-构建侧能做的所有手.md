---
title: [BLD-182] SPA 首屏 TTI 优化中，构建侧能做的所有手段清单。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-182：SPA 首屏 TTI 优化中，构建侧能做的所有手段清单。
**答**：
- **体积类**：代码分割（路由级/组件级动态 import）、tree-shaking（sideEffects/ESM 源码依赖）、按需引入组件库、依赖收敛与 dedupe、polyfill 按需（usage）、压缩升级（terser→esbuild/wasm? 或更优配置）。
- **加载编排类**：首屏关键 chunk 优先（manualChunks 拆分 + preload）、非关键资源 defer/modulepreload、prefetch 路由 chunk（webpackPrefetch/vite build.modulePreload）、`output.asyncChunks`? 与 webpackChunkName 语义化命名。
- **运行时配合类**：SSR/预渲染首屏直出、骨架屏（构建期注入 HTML）、HTTP 层（HTTP/2、Brotli、CDN 边缘缓存）、sourcemap 上传后生产剥离。
- **度量闭环**：Lighthouse CI / WebPageTest 基线、`performance.mark` 埋点、budget 卡口——构建侧手段必须配度量，否则"优化"无证据。

```javascript
// 构建侧 TTI 手段的配置全家桶（webpack5）
module.exports = {
  performance: { maxEntrypointSize: 400000, maxAssetSize: 250000, hints: 'error' },  // 预算卡口
  optimization: {
    splitChunks: { chunks: 'all', maxInitialRequests: 6 },
    runtimeChunk: 'single',
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './index.html',
      // 骨架屏构建期注入（替代运行时 JS 渲染，避免骨架屏本身拖慢 FCP）
      templateParameters: { SKELETON: fs.readFileSync('./src/skeleton.html') },
    }),
    new MiniCssExtractPlugin({ filename: 'css/[name].[contenthash].css' }),
  ],
  module: {
    rules: [{
      test: /\.[jt]sx?$/,
      // 关键 chunk 标注：首屏模块 prefetch 次屏（正则 route 匹配）
      // 源码侧等价：import(/* webpackPrefetch: true, webpackChunkName: "dash" */ './Dashboard')
    }],
  },
  output: { filename: 'js/[name].[contenthash:8].js', chunkFilename: 'js/[name].[contenthash:8].async.js' },
  // HTTP 层：CI 构建后补 Brotli
  // plugins.push(new CompressionPlugin({ algorithm: 'brotliCompress', test: /\.(js|css|html)$/ }));
};
// 度量闭环：lighthouserc 断言（<2.5s TTI @ 4G）进 CI，与 size budget 双卡口
```
