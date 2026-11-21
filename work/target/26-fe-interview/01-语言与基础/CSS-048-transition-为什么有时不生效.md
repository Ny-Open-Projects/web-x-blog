---
title: [CSS-048] transition 为什么有时不生效？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-048：transition 为什么有时不生效？

**答**：
- 起点/终点状态未变化，或属性值本身不可过渡（display: none ↔ block、height: auto）。
- 初始渲染时添加的 class：元素尚未完成首次样式计算，transition 不会触发，需强制 reflow 或下一帧再改。
- 简写覆盖：后面的 `transition` 声明整体覆盖前面的，导致属性丢失。
- 元素在 transition 期间被 display: none 或脱离文档流会直接终止。

```css
/* 错误示例：display 突变无法过渡 */
.dropdown { display: none; opacity: 0; transition: opacity 0.2s; }
.dropdown.open { display: block; opacity: 1; } /* 没有 opacity 过渡效果 */

/* 修复：用 visibility + pointer-events */
.dropdown-fixed {
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity 0.2s, visibility 0.2s;
}
.dropdown-fixed.open {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
}
```

```javascript
// 初始渲染问题：强制一帧后再触发
el.classList.add('fade-enter');            // 初始态
void el.offsetHeight;                      // 强制 reflow
el.classList.add('fade-enter-active');     // 终态，transition 正常触发
```
