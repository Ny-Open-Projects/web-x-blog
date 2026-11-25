---
title: [VIZ-254] 可视化 SSR：服务端渲染图表与客户端水合
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-254：可视化 SSR：服务端渲染图表与客户端水合

**答**：
- 图表 SSR：服务端用 node-canvas/svg 渲染首屏图（SEO/首屏），客户端水合接管交互。
- 双渲染一致性：同一份渲染逻辑跑在 node（canvas 包）与 browser——渲染层抽象（HW-400 思想）。
- 水合：SSR 输出静态 SVG/PNG + 数据内联；客户端检测到 JS 就绪后重建交互层（不重绘静态部分）。

```javascript
// server.js
import { createCanvas } from 'canvas';
function renderChartSSR(data, size) {
  const canvas = createCanvas(size.w, size.h);             // node-canvas
  paintStatic(canvas.getContext('2d'), data);               // 与浏览器共用 paint 逻辑
  return { svg: toSVG(data), data };
}
// client.js
function hydrateChart(el, ssrData) {
  if (supportsGPU()) mountInteractive(el, ssrData.data);    // 客户端全功能接管
  else enhanceStatic(el, ssrData.svg);                      // 低端：只加交互层
}
// 一致性保障：paintStatic 抽象成纯函数（输入 ctx + data），node 与 browser 同实现
// 差异兜底：字体差异导致布局偏移——服务端用同款字体文件（fontkit）
```
