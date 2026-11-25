---
title: [BAS-068] scroll-behavior 和 overscroll-behavior 分别管什么？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-068：scroll-behavior 和 overscroll-behavior 分别管什么？
**答**：
- scroll-behavior: smooth 让锚点跳转、scrollTo 等程序滚动变为平滑滚动，一行 CSS 替代 JS 动画。
- overscroll-behavior: contain 阻止滚动链——内层滚到头后不再带动外层/body 滚动，弹窗内滚动必备。
- overscroll-behavior 另有 none（还取消过头回弹）、auto（默认）。

```css
html { scroll-behavior: smooth; }        /* 锚点跳转平滑滚动 */
.modal-body {
  overflow: auto;
  overscroll-behavior: contain;          /* 滚到底不再传染给页面 */
}
```
