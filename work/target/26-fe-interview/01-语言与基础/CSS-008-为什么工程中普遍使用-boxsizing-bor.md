---
title: [CSS-008] 为什么工程中普遍使用 box-sizing: border-box 全局重置？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-008：为什么工程中普遍使用 box-sizing: border-box 全局重置？

**答**：
- content-box 下改 padding 就会改变元素总宽，栅格与弹性布局很容易被撑破。
- border-box 让 `width` 所见即所得，配合百分比宽度做加减法更直观。
- 现代重置常用 `box-sizing: border-box` + 继承，避免第三方组件被波及时难以覆盖。
- 注意 `min-width/max-width` 同样受 `box-sizing` 影响（计算方式与 `width` 一致），重点还是统一心智模型。

```css
/* 现代重置写法：继承式 border-box */
*,
*::before,
*::after {
  box-sizing: border-box;
}

/* 更稳妥：允许第三方组件改回 content-box */
html {
  box-sizing: border-box;
}
*, *::before, *::after {
  box-sizing: inherit;
}
```

## 二、BFC 与 IFC
