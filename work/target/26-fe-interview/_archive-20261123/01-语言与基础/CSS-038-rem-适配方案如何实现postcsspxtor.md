---
title: [CSS-038] rem 适配方案如何实现？postcss-pxtorem 在其中扮演什么角色？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-038：rem 适配方案如何实现？postcss-pxtorem 在其中扮演什么角色？

**答**：
- rem 相对根元素 `font-size`，设计稿适配的核心是“按屏宽动态设置 html 的 font-size”。
- JS 方案：`html.style.fontSize = clientWidth / 设计稿宽度 * 基准值`，如 375 稿对应 37.5px。
- postcss-pxtorem 在构建期把 px 自动换算成 rem，开发者仍按设计稿写 px。
- 简化方案：`html { font-size: calc(100vw / 7.5) }`，750 稿下 1rem = 100px，无需 JS。

```css
/* 纯 CSS 方案：750 设计稿，1rem = 100px */
html {
  font-size: calc(100vw / 7.5);
}
.title {
  font-size: 0.32rem;   /* 对应设计稿 32px */
  padding: 0.24rem;     /* 对应设计稿 24px */
}
/* 需要限制最大字号时叠加媒体查询 */
@media (min-width: 560px) {
  html { font-size: 75px; }
}
```

```javascript
// JS 动态方案（flexible 思路）
function setRem() {
  const designWidth = 375;
  const baseSize = 37.5; // 375 稿下 1rem = 37.5px，配 pxtorem rootValue: 37.5
  const scale = document.documentElement.clientWidth / designWidth;
  document.documentElement.style.fontSize = baseSize * Math.min(scale, 3) + 'px';
}
setRem();
window.addEventListener('resize', setRem);
```
