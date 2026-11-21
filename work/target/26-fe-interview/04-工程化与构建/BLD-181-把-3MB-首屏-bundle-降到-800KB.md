---
title: [BLD-181] 把 3MB 首屏 bundle 降到 800KB 的完整案例。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-181：把 3MB 首屏 bundle 降到 800KB 的完整案例。
**答**：
- 定位（webpack-bundle-analyzer + source-map-explorer）：moment locales 600KB、lodash 全量 540KB、antd 全量 780KB、业务重复依赖（两个版本 react-dnd）400KB、polyfill 全量 300KB、CSS 未拆分 200KB。
- 措施：moment → dayjs（-580KB）；lodash → lodash-es 按需 + tree-shaking（-420KB）；antd 按需引入（unplugin? babel-plugin-import）（-640KB）；依赖收敛（pnpm overrides 锁单版本 react-dnd）（-260KB）；useBuiltIns: usage（-280KB）；路由级代码分割 + manualChunks 拆 vendor（首屏 -350KB）；CSS code split。
- 数据：3.0MB → 795KB（gzip 2.1MB → 380KB）；TTI 从 6.8s → 2.4s（4G 模拟）。
- 治理收尾：size budget 卡口（BLD-117）防回弹——"降下来"容易，"守得住"才是工程能力。

```javascript
// 优化后的关键配置汇总
module.exports = {
  resolve: { alias: { 'dayjs$': 'dayjs' } },
  optimization: {
    splitChunks: {
      chunks: 'all',
      maxInitialRequests: 6,                       // 首屏并行请求数控制
      cacheGroups: {
        react: { test: /[\\/]node_modules[\\/](react|react-dom|scheduler)[\\/]/, name: 'react', priority: 20 },
        antd: { test: /[\\/]node_modules[\\/](antd|@ant-design)[\\/]/, name: 'antd', priority: 15 },
        vendors: { test: /[\\/]node_modules[\\/]/, name: 'vendors', priority: 10, minSize: 40000 },
      },
    },
  },
  module: {
    rules: [
      { test: /\.js$/, include: /node_modules[\\/](antd|rc-/), enforce: 'pre',
        use: 'babel-plugin-import-loader' },       // antd 按需（或用 esbuild 侧 unplugin）
    ],
  },
};
// 源码侧治理：
// - import dayjs from 'dayjs'（替换 moment，插件全删）
// - import debounce from 'lodash-es/debounce'   ← ESM 命名空间可摇
// - pnpm.overrides: { 'react-dnd': '16.0.1' }   ← 消灭双版本
// babel.config.js: presets: [['@babel/preset-env', { useBuiltIns: 'usage', corejs: 3 }]]
// 结果：3.0MB→795KB（gzip 380KB），budget 卡口：首屏 gzip > 420KB 时 CI 失败
```
