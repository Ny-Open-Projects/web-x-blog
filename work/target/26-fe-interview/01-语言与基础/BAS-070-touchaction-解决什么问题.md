---
title: [BAS-070] touch-action 解决什么问题？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-070：touch-action 解决什么问题？
**答**：
- 声明元素上允许哪些触摸手势交给浏览器处理，是"浏览器手势"与"页面滚动"之间的总开关。
- `touch-action: none` 把所有触摸交给 JS（canvas 画板、拖拽）；`pan-y` 只允许纵向滚动、横向手势留给 JS。
- 横滑轮播、自定义滑块设 `pan-y`，可消除横向滑动与浏览器手势的冲突抖动。

```css
.slider {
  touch-action: pan-y;   /* 纵向滚动交还浏览器，横向手势自己处理 */
}
.canvas-board {
  touch-action: none;    /* 画板上所有触摸都给 JS */
}
```

## 九、CSS 补充·视觉与排版
