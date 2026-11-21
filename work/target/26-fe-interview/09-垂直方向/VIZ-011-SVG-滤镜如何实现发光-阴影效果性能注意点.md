---
title: [VIZ-011] SVG 滤镜如何实现发光/阴影效果？性能注意点？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-011：SVG 滤镜如何实现发光/阴影效果？性能注意点？
**答**：滤镜通过 `<filter>` 定义原语链：feGaussianBlur 高斯模糊 → feOffset 偏移 → feFlood/feComposite 上色 → feMerge 合并回原图。发光 = 模糊层叠在原图下面；投影 = 模糊 + 偏移 + 变暗。性能上滤镜是**逐像素计算**且开销大：模糊半径越大越贵，动一个带滤镜的元素会触发整个滤镜区域重算，所以要扩大 filter region 防裁切、避免对大面积或高频动画元素加滤镜、能预烘焙就导出成静态资源。

```html
<svg width="300" height="140">
  <defs>
    <!-- 发光：模糊层放在 SourceGraphic 之下叠加 -->
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="4" result="blur"></feGaussianBlur>
      <feMerge>
        <feMergeNode in="blur"></feMergeNode>
        <feMergeNode in="SourceGraphic"></feMergeNode>
      </feMerge>
    </filter>
    <!-- 投影：模糊 + 偏移 + 变暗，垫在原图下方 -->
    <filter id="shadow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="3" result="b"></feGaussianBlur>
      <feOffset in="b" dx="2" dy="3" result="o"></feOffset>
      <feFlood flood-color="#000" flood-opacity="0.35" result="c"></feFlood>
      <feComposite in="c" in2="o" operator="in" result="s"></feComposite>
      <feMerge>
        <feMergeNode in="s"></feMergeNode>
        <feMergeNode in="SourceGraphic"></feMergeNode>
      </feMerge>
    </filter>
  </defs>
  <circle cx="80" cy="70" r="30" fill="#4fc3f7" filter="url(#glow)"></circle>
  <rect x="170" y="40" width="80" height="60" rx="8" fill="#fff" stroke="#94a3b8" filter="url(#shadow)"></rect>
</svg>
```
