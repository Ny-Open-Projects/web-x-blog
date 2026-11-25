---
title: [CSS-005] 空块级元素的 margin 合并是什么现象？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-005：空块级元素的 margin 合并是什么现象？

**答**：
- 一个没有内容、没有 border/padding/height 的空块级元素，它自己的 `margin-top` 和 `margin-bottom` 会合并为一个值。
- 它还会和前后兄弟的 margin 继续合并，导致间距“消失”。
- 解决：给它最小高度、border、padding，或加 `overflow: hidden` 建立 BFC。
- 该题常用于考察对 margin 合并三个条件（相邻/父子/空元素）的完整记忆。

```css
.prev { margin-bottom: 40px; }

.empty {
  margin-top: 30px;
  margin-bottom: 30px;
  /* 空元素自身合并为 30px，再与上方 40px 合并 → 40px */
}

.next { margin-top: 20px; } /* 再合并仍为 40px */

/* 修复：阻断合并 */
.empty.fixed {
  overflow: hidden; /* 建立 BFC，自身上下 margin 不再合并 */
}
```
