---
title: [CSS-007] padding 的百分比是相对什么计算的？如何用它实现固定宽高比？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-007：padding 的百分比是相对什么计算的？如何用它实现固定宽高比？

**答**：
- padding 的百分比无论上下左右，都是相对**父元素的宽度**计算的。
- 老方案 `padding-top: 50%` 配合 `height: 0` 可以实现 2:1 占位框。
- 现代方案直接用 `aspect-ratio: 16 / 9`，语义更清晰。
- 面试时应能说出两种方案的演进关系与兼容性差异。

```css
/* 旧方案：padding-top 百分比占位，实现 16:9 */
.ratio-box {
  position: relative;
  height: 0;
  padding-top: 56.25%; /* 相对父宽，100/16*9 */
}
.ratio-box > .content {
  position: absolute;
  inset: 0;
}

/* 新方案：aspect-ratio */
.ratio-modern {
  aspect-ratio: 16 / 9;
  width: 100%;
}
```
