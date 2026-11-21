---
title: [PER-467] 滚动驱动的 JS 动画帧预算：视差/跟随效果如何保证 60fps（读写分离 + 合成器路径最大化）？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-467：视差/跟随滚动效果的 60fps 帧预算管理？

**答**:
- 帧预算拆解（16.7ms）：滚动事件本身 0（合成器线程）、JS 回调 ≤ 5ms（只做计算不做布局）、style/layout ≤ 5ms（transform-only 无 layout）、合成 ≤ 3ms、余量 3ms。
- 实现纪律：① 滚动值在 rAF 内一次读取（读写分离，PER-404）；② 效果全部走 transform（合成器路径，PER-347）——视差位移、缩放、透明度；③ 多层视差的每层独立 will-change（层预算内，PER-405）；④ 复杂视差用 Web Animations API + scrollTimeline（CSS 滚动驱动动画——Chrome 115+，动画完全脱离 JS 主线程）。
- scrollTimeline 的意义：`animation-timeline: scroll()` 让动画与滚动位置直接绑定在合成器线程——主线程零参与，是滚动驱动的终极形态（降级 rAF JS 驱动）。

```css
/* CSS 滚动驱动动画（Chrome 115+）：主线程零参与 */
@keyframes parallax { from { transform: translateY(0); } to { transform: translateY(-40%); } }
.parallax-layer {
  animation: parallax linear forwards;
  animation-timeline: scroll();          /* 与滚动位置绑定，合成器线程驱动 */
  will-change: transform;
}
```
```javascript
// 降级：rAF + 读写分离 + transform-only（帧预算 5ms JS / 5ms style / 3ms 合成）
let ticking = false;
container.addEventListener('scroll', () => {
  if (ticking) return;
  ticking = true;
  requestAnimationFrame(() => {
    ticking = false;
    const y = container.scrollTop;                    // 一次读
    for (const [layer, factor] of layers) {
      layer.el.style.transform = `translateY(${y * factor}px)`;   // 纯 transform 写
    }
  });
}, { passive: true });
```
