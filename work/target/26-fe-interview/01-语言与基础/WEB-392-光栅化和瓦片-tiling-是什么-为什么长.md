---
title: [WEB-392] 光栅化和瓦片（tiling）是什么？为什么长页面滚动很顺滑？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 浏览器]
type: 面试题
---

## WEB-392：光栅化和瓦片（tiling）是什么？为什么长页面滚动很顺滑？
**答**：
- 合成器把层切成瓦片（通常 256×256/512×512），光栅化线程按优先级（视口内优先）把瓦片画成位图，合成时按需贴图。
- 滚动时视口外瓦片未光栅 → 先显示 checkerboard 再补齐；预光栅视口附近一圈让滚动不留白。
- 前端含义：超长页面全部 content-visibility: auto 可跳过屏外光栅；超大图片瓦片成本高，控制图层尺寸。

```javascript
const tiles = (w, h, size = 256) => Math.ceil(w / size) * Math.ceil(h / size);
console.log('1920x10000 一层瓦片数:', tiles(1920, 10000)); // 300 片
console.log('content-visibility: auto → 屏外元素跳过布局/光栅');
```
