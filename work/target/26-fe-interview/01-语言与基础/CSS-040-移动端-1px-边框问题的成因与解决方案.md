---
title: [CSS-040] 移动端 1px 边框问题的成因与解决方案？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-040：移动端 1px 边框问题的成因与解决方案？

**答**：
- 成因：CSS 的 1px 是逻辑像素，dpr = 2/3 的屏幕上物理像素为 2px/3px，视觉偏粗。
- 方案一：伪元素绘制 200% 尺寸再 `transform: scale(0.5)` 缩回。
- 方案二：`border: 0.5px`（Safari 8+ / 新版 Chrome 支持降级需检测）。
- 方案三：viewport 缩放方案（根缩放 + 反向缩放），实现复杂现已少用。
- 推荐伪元素方案，可配 SCSS mixin 复用并支持单边控制。

```css
/* 方案一：伪元素 + scale（推荐） */
.hairline {
  position: relative;
}
.hairline::after {
  content: "";
  position: absolute;
  left: 0;
  top: 0;
  width: 200%;
  height: 200%;
  border: 1px solid #ddd;
  border-radius: 8px;
  transform: scale(0.5);          /* 视觉 0.5px 逻辑边框 */
  transform-origin: 0 0;
  box-sizing: border-box;
  pointer-events: none;
}

/* 方案二：0.5px 直接声明 */
.thin {
  border-bottom: 0.5px solid #ddd;
}
```
