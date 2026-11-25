---
title: [BAS-078] mix-blend-mode 和 background-blend-mode 的区别？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-078：mix-blend-mode 和 background-blend-mode 的区别？
**答**：
- mix-blend-mode 让元素与其**下方所有内容**混合，常用 multiply（正片叠底）、screen（滤色）、difference（差值反色）。
- background-blend-mode 只在同一元素的**多层 background 之间**混合（背景图与背景色），不影响页面其他内容。
- 经典应用：双色调图片（图片 + 纯色 multiply）、深浅背景上自动反色的文字（difference）。

```css
.duotone {
  background: url(photo.jpg) center / cover, #7c3aed;
  background-blend-mode: multiply;   /* 图片与紫色底混合出双色调 */
}
.invert-text { mix-blend-mode: difference; color: #fff; }  /* 深浅背景上自动反色 */
```
