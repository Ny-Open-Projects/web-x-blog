---
title: [VIZ-012] SVG 动画有哪些方案？如何选型？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-012：SVG 动画有哪些方案？如何选型？
**答**：三种方案：**CSS**（transition/animation）声明式，transform/opacity 走合成器性能最好，适合状态切换与 hover，但插值能力弱；**SMIL**（animate/animateTransform）内嵌于 SVG、可沿路径运动，但兼容性收缩且趋于废弃，新项目不推荐；**JS + rAF**（或 Web Animations API）完全可控——逐帧插值、串行动画编排、物理缓动、数据驱动的形变，是图表库的标准选择。选型口诀：简单状态用 CSS，路径动画看兼容，其余一律 JS。

```html
<style>
  /* CSS：声明式，transform/opacity 走合成器，适合状态切换 */
  .bar { transition: transform .6s ease; transform-origin: left center; }
  .bar.active { transform: scaleX(1); }
</style>
<svg width="220" height="60">
  <rect class="bar" width="200" height="30" style="transform: scaleX(0.2)"></rect>
</svg>
<script>
  document.querySelector('.bar').classList.add('active');
  const rect2 = document.querySelector('rect');
  // JS + rAF：完全可控（逐帧插值/编排/物理缓动），图表库的标准方案
  function animate(from, to, dur, onFrame) {
    const t0 = performance.now();
    (function step(t) {
      const p = Math.min((t - t0) / dur, 1);
      const ease = 1 - Math.pow(1 - p, 3); // easeOutCubic
      onFrame(from + (to - from) * ease);
      if (p < 1) requestAnimationFrame(step);
    })(t0);
  }
  animate(0, 200, 600, v => { rect2.setAttribute('width', v); });
  // SMIL（animate/set 元素）已趋于废弃，新项目不推荐使用
</script>
```
