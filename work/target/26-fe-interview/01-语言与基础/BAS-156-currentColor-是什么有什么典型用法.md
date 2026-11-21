---
title: [BAS-156] currentColor 是什么？有什么典型用法？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-156：currentColor 是什么？有什么典型用法？
**答**：
- currentColor 引用元素自身的 color 计算值，是 CSS 里的"活引用"。
- 典型用法：边框/阴影跟随文字颜色、SVG 图标 fill 继承文字颜色——只改一处 color，整组视觉同步变化。
- 补充：border-color 等缺省值本身就是 currentColor。

```css
.link {
  color: #1677ff;
  border: 1px solid currentColor;  /* 边框跟随文字颜色 */
  box-shadow: 0 0 0 3px color-mix(in srgb, currentColor 30%, transparent);
}
.link:hover { color: #4096ff; }    /* 改一处，边框阴影一起变 */
.icon { fill: currentColor; }      /* SVG 图标继承文字颜色 */
```
