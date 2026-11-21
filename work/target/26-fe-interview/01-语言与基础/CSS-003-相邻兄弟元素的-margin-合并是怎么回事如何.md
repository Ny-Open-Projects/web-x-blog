---
title: [CSS-003] 相邻兄弟元素的 margin 合并是怎么回事？如何避免？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-003：相邻兄弟元素的 margin 合并是怎么回事？如何避免？

**答**：
- 垂直方向上相邻块级元素的 `margin-bottom` 与 `margin-top` 会合并，取较大值而不是相加。
- 水平方向的 margin 永远不合并。
- 避免方式：让两元素不处于同一 BFC、改用 flex/grid 容器（子元素间不合并）、或只使用单侧 margin。
- 工程上推荐统一用 `margin-bottom` 单方向间距，从源头规避。

```css
/* HTML: <div class="a">A</div><div class="b">B</div> */
.a { margin-bottom: 30px; }
.b { margin-top: 20px; }
/* A 与 B 之间间距是 30px（取较大值），不是 50px */

/* 解决方案一：外层用 flex 容器 */
.list {
  display: flex;
  flex-direction: column;
}
.list > .item { margin: 10px 0; } /* flex 子项间不合并 */

/* 解决方案二：BFC 包裹 */
.bfc-wrap { overflow: hidden; }
```
