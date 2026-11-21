---
title: [H5-163] SMIL/CSS/JS/WAAPI 四种 SVG 动画方案怎么选？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-163：SMIL/CSS/JS/WAAPI 四种 SVG 动画方案怎么选？
**答**：
- **SMIL**（`<animate>`/`<animateTransform>`/`animateMotion`）：声明式、独立于 CSS、可做"沿路径运动"与 d 属性动画；官方曾标记 deprecated 但实际不弃用，缺点是无交互控制。
- **CSS**：transform/opacity 动画性能最好、可配合 :hover 交互；`offset-path` 可替代 animateMotion；缺点是 x/y/width 等属性动画会触发布局。
- **WAAPI**：元素级控制（暂停/倒放/调速/精确回调），SVG 图形也是元素所以完全适用；编排复杂交互动效首选。
- **JS（rAF）**：物理模拟、手势驱动、复杂绑定的兜底。选型：装饰循环动效 CSS、路径跟随 SMIL/offset-path、可编程控制 WAAPI、复杂逻辑 JS。

```html
<svg width="220" height="90" viewBox="0 0 220 90">
  <!-- 方案 1 SMIL：声明式，可做"沿路径运动"，不依赖 CSS/JS -->
  <circle r="4" fill="#2563eb">
    <animateMotion dur="3s" repeatCount="indefinite"
                   path="M10 40 C 60 0, 160 80, 210 40" />
  </circle>

  <!-- 方案 2 CSS：transform/opacity 动画性能最好 -->
  <rect x="10" y="62" width="30" height="10" fill="#10b981" class="pulse"/>
  <style>
    .pulse { transform-origin: 25px 67px; animation: pulse 1.5s infinite; }
    @keyframes pulse { 50% { transform: scale(1.6); opacity: .4; } }
  </style>

  <!-- 方案 3 JS/rAF：完全控制（物理、缓动、交互打断） -->
  <rect id="bar" x="60" y="20" width="10" height="40" fill="#f59e0b"/>
  <script>
    const bar = document.getElementById('bar');
    let t0 = performance.now();
    (function tick(now) {
      const t = (now - t0) / 1000;
      bar.setAttribute('transform', 'rotate(' + (Math.sin(t) * 20).toFixed(2) + ' 65 40)');
      requestAnimationFrame(tick);
    })(t0);
  </script>
</svg>
<script>
// 方案 4 WAAPI：元素级控制（暂停/倒放/合成），SVG 图形也是元素
document.querySelector('.pulse').animate(
  [{ transform: 'scale(1)' }, { transform: 'scale(1.6)' }, { transform: 'scale(1)' }],
  { duration: 1500, iterations: Infinity }
);

// 选型口径：
// 1) 装饰性循环动效 → CSS（GPU、零 JS）
// 2) 沿任意路径运动 → SMIL animateMotion；新项目也可用 CSS offset-path 替代
// 3) 需要精确回调/暂停/倒放/编排 → WAAPI
// 4) 需要物理模拟、手势驱动、复杂数据绑定 → JS（rAF）或 GSAP/D3
// 5) d 属性（形状）动画：SMIL 或 JS 插值；CSS 的 d:path() 要求路径结构兼容
</script>
```
