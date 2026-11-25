---
title: [PER-970] rAF 与合成器动画的关系：为什么 opacity/transform 动画能脱离主线程
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-970：rAF 与合成器动画的关系：为什么 opacity/transform 动画能脱离主线程

**答**：
- 合成器动画（transform/opacity）由合成器线程直接驱动，主线程阻塞时动画依旧流畅；其他属性动画需主线程逐帧重算。
- 判断方法：DevTools Performance 看"Compositor-driven"标记；或动画期间制造长任务，动画仍顺滑即为合成器动画。
- 限制：合成器动画无法读取/影响布局（如 height 动画必须主线程），也无法响应中途 DOM 变化。
- 深水：scroll-driven animations 让动画进度绑定滚动位置，由合成器计算，无需主线程 scroll 监听。

```javascript
// 合成器驱动 + 滚动驱动动画（零 JS 每帧成本）
// CSS:
// @keyframes grow { from { transform: scaleX(0) } to { transform: scaleX(1) } }
// .bar { animation: grow linear; animation-timeline: scroll(root); }
// 等价的 JS 检测：
function isCompositorDriven(el) {
  const before = getComputedStyle(el).transform;
  // 制造长任务：若动画仍推进则为合成器驱动
  const t0 = performance.now();
  while (performance.now() - t0 < 200) { /* 忙等 */ }
  return getComputedStyle(el).transform !== before;
}
// 结论：进度条/视差/入场动画全部改用 timeline，滚动监听删除
```
