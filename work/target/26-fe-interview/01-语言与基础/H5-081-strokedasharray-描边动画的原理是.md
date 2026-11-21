---
title: [H5-081] stroke-dasharray 描边动画的原理是什么？如何做"线条描绘"效果？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-081：stroke-dasharray 描边动画的原理是什么？如何做"线条描绘"效果？
**答**：
- 原理：`stroke-dasharray` 把描边切成"实线-空隙"重复段；`stroke-dashoffset` 把段起点平移。当实线段长 = 路径全长时，调整 offset 即可"从无到有"画出整条线。
- 标准三步：`len = path.getTotalLength()` → `dasharray = dashoffset = len`（完全隐藏）→ 动画把 offset 变到 0（逐渐显露）。
- 用 CSS 动画（`@keyframes` 或 transition）驱动 offset，GPU 友好且能复用缓动；`stroke-linecap: round` 让端点圆润。
- 多条线错峰：给每条 path 不同 `animation-delay` 形成依次描绘；配合 `animation-fill-mode: forwards` 定格。
- 注意：offset 的方向感取决于路径书写方向（M 点到终点的顺序），"从哪头开始画"由 d 决定而不是 CSS。

```html
<style>
  .draw path {
    fill: none;
    stroke: #333;
    stroke-width: 4;
    stroke-linecap: round;
    stroke-dasharray: var(--len);
    stroke-dashoffset: var(--len);          /* 初始完全隐藏 */
    animation: draw 1.2s ease-out forwards;
  }
  /* 每条线自带长度变量 + 错峰延迟 */
  .draw path:nth-child(1) { --len: 480; animation-delay: 0s; }
  .draw path:nth-child(2) { --len: 300; animation-delay: 0.8s; }
  .draw path:nth-child(3) { --len: 260; animation-delay: 1.4s; }

  @keyframes draw { to { stroke-dashoffset: 0; } }
</style>

<svg class="draw" viewBox="0 0 300 150" width="300">
  <path d="M 20 130 L 120 30 L 180 90"/>          <!-- 折线 -->
  <path d="M 30 40 Q 90 -20 150 40"/>             <!-- 曲线 -->
  <path d="M 200 130 A 45 45 0 1 1 200.1 130"/>   <!-- 圆 -->
</svg>

<script>
  // 工程化：长度不再手填，JS 读真实长度写回 CSS 变量（支持任意复杂路径）
  document.querySelectorAll('.draw path').forEach((p, i) => {
    const len = Math.ceil(p.getTotalLength());
    p.style.setProperty('--len', len);
    p.style.animationDelay = `${i * 0.5}s`;
  });
</script>
```
