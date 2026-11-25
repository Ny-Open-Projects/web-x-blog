---
title: [H5-082] SVG 的 filter 与 mask 各自解决什么问题？边界在哪？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-082：SVG 的 filter 与 mask 各自解决什么问题？边界在哪？
**答**：
- `filter`（`<filter>` + feGaussianBlur/feColorMatrix/feDropShadow…）做**像素级处理**：模糊、阴影、色相变换，基于源图形生成新像素。
- `mask`（`<mask>` 元素或 CSS `mask`）做**显隐裁剪**：用亮度/alpha 决定"哪里可见"，不改变可见部分的颜色。
- 记忆口径：滤镜改"样子"，蒙版改"范围"；图片渐隐边缘用 mask，发光阴影用 filter，两者可叠加。
- feDropShadow 是 CSS box-shadow 之外给任意 SVG 图形加阴影的最短路径；feColorMatrix 可做置灰（灰阶矩阵）。
- 性能提醒：filter 在部分浏览器走 CPU/慢路径，动画中频繁变化的大面积滤镜要谨慎，优先用 opacity/transform 实现类似效果。

```html
<svg viewBox="0 0 300 160" width="300">
  <defs>
    <!-- filter：高斯模糊 + 投影 -->
    <filter id="soft">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#0003"/>
    </filter>

    <!-- mask：白色=可见，黑色=隐藏，渐变实现边缘渐隐 -->
    <linearGradient id="fade" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#fff"/>
      <stop offset="0.7" stop-color="#fff"/>
      <stop offset="1" stop-color="#000"/>
    </linearGradient>
    <mask id="fade-mask">
      <rect width="300" height="160" fill="url(#fade)"/>
    </mask>

    <!-- 置灰滤镜：常用作"禁用态图标" -->
    <filter id="gray">
      <feColorMatrix type="matrix"
        values="0.33 0.33 0.33 0 0
                0.33 0.33 0.33 0 0
                0.33 0.33 0.33 0 0
                0 0 0 1 0"/>
    </filter>
  </defs>

  <rect x="20" y="30" width="120" height="80" rx="8" fill="#36f" filter="url(#soft)"/>

  <image href="/img/banner.png" x="0" y="0" width="300" height="160"
         mask="url(#fade-mask)"/>

  <text x="160" y="140" font-size="20" fill="#333" filter="url(#gray)">置灰文字</text>
</svg>

<style>
  /* CSS 侧也能用 mask：对任意 HTML 元素做形状显隐 */
  .avatar {
    width: 48px; height: 48px;
    mask: radial-gradient(circle at center, #000 60%, transparent 61%);
  }
</style>
```
