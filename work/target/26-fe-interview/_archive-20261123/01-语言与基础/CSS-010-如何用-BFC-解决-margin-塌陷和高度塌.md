---
title: [CSS-010] 如何用 BFC 解决 margin 塌陷和高度塌陷？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-010：如何用 BFC 解决 margin 塌陷和高度塌陷？

**答**：
- margin 塌陷：给父元素建 BFC，父子 margin 不再合并，子元素 margin 被包含在内。
- 高度塌陷：子元素浮动后父元素高度为 0，BFC 容器在计算高度时会把浮动子元素包含进来。
- 对比 `clear: both` 的伪元素方案：BFC 是“包含”，clear 是“让开”，语义不同。
- 两种场景都推荐 `display: flow-root` 一行解决。

```css
/* 场景一：margin 塌陷 */
.parent-margin {
  display: flow-root;  /* 子元素 margin-top 不再穿透 */
  background: #f5f5f5;
}
.parent-margin > .child { margin-top: 40px; }

/* 场景二：浮动导致父元素高度塌陷 */
.parent-float {
  display: flow-root;  /* 高度被浮动子元素撑起 */
}
.parent-float > .left {
  float: left;
  width: 200px;
  height: 100px;
  background: #096;
}
```
