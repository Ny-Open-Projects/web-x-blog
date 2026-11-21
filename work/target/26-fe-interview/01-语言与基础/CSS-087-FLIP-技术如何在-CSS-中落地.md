---
title: [CSS-087] FLIP 技术如何在 CSS 中落地？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-087：FLIP 技术如何在 CSS 中落地？

**答**：
- FLIP = First 记录起始位置 → Last 应用最终布局 → Invert 用 transform 反向回置 → Play 过渡归零。
- 纯 CSS 无法感知布局前后差异，必须 JS 测量 + transform 过渡配合。
- 只动 transform，全程走合成层，列表重排、卡片换位、拖拽排序的黄金方案。
- 可用 WAAPI `element.animate()` 即用即弃，不污染样式表。
- 与 View Transitions 的关系：VT 是浏览器内置的自动化 FLIP，手写 FLIP 用于更细粒度控制。

```javascript
// 列表重排 FLIP：sortDOM() 内部重排，外部负责过渡
function flip(container, sortDOM) {
  const first = new Map(
    [...container.children].map((el) => [el, el.getBoundingClientRect().top])
  );
  sortDOM(); // Last：真正改变布局

  [...container.children].forEach((el) => {
    const dy = first.get(el) - el.getBoundingClientRect().top; // Invert：反向回置
    if (!dy) return;
    el.animate(
      [{ transform: `translateY(${dy}px)` }, { transform: 'translateY(0)' }],
      { duration: 300, easing: 'cubic-bezier(0.22, 1, 0.36, 1)' } // Play：过渡归零
    );
  });
}
```
