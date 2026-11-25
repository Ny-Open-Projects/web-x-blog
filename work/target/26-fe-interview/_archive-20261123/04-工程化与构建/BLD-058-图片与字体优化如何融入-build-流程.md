---
title: [BLD-058] 图片与字体优化如何融入 build 流程？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-058：图片与字体优化如何融入 build 流程？
**答**：
- 尺寸治理：构建期用 sharp/squoop 压缩 + 按宽度生成多分辨率（srcset），禁止设计稿原图直进仓库；image-webpack-loader 或 vite 插件在产物阶段处理。
- 格式策略：优先 WebP/AVIF，JPEG 保留兜底；svg 走 asset/source 内联染色的同时可用 svgo 瘦身。
- 字体：woff2 优先 + font-display: swap；subset（中文字体按需抽字形，如 fontmin）收益极大。
- 加载：关键小图 dataUrl 内联（BLD-024 的 maxSize），首屏大图 preload，非关键懒加载（loading="lazy"）。

```javascript
// webpack.config.js：图片压缩 + svg 瘦身 + 字体优化
module.exports = {
  module: {
    rules: [
      {
        test: /\.(png|jpe?g|gif|webp)$/i,
        type: 'asset',
        parser: { dataUrlCondition: { maxSize: 8 * 1024 } },
        generator: { filename: 'img/[name].[contenthash:8][ext]' },
        use: [{
          loader: 'image-webpack-loader', // 压缩在后 normal 阶段 作用于 asset 之前
          options: {
            mozjpeg: { quality: 75, progressive: true },
            webp: { quality: 75 },
            avif: { quality: 60 },
          },
        }],
      },
      {
        test: /\.svg$/i,
        type: 'asset/source',
        use: [{ loader: 'svgo-loader', options: { plugins: [
          { name: 'preset-default', params: { overrides: { removeViewBox: false } } },
        ] } }],
      },
      {
        test: /\.woff2?$/i,
        type: 'asset/resource',
        generator: { filename: 'font/[name].[contenthash:8][ext]' },
      },
    ],
  },
};

// CSS 侧字体优化（text 代码块）：
// @font-face {
//   font-family: AppSans;
//   src: url('./app-sans.woff2') format('woff2');
//   font-display: swap;   // 先用回退字体 文字不可见时间最短
//   unicode-range: U+4E00-9FFF; // 只覆盖需要的字形范围
// }
```
