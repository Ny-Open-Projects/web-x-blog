---
title: [CSS-037] 不用 flex/grid 的传统垂直居中方案有哪些？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-037：不用 flex/grid 的传统垂直居中方案有哪些？

**答**：
- 单行文本：`line-height` 等于容器高度。
- 多行文本或未知高度：`display: table-cell; vertical-align: middle`。
- 伪元素幽灵节点法：`::before` 撑起 inline-block 全高，内容 vertical-align: middle。
- absolute + translate 也属于传统方案，见上一题。

```css
/* 单行文本 */
.one-line {
  height: 48px;
  line-height: 48px;
}

/* table-cell */
.cell {
  display: table-cell;
  vertical-align: middle;
  height: 200px;
}

/* 幽灵节点法 */
.ghost {
  text-align: center;
  height: 300px;
}
.ghost::before {
  content: "";
  display: inline-block;
  height: 100%;
  vertical-align: middle;
}
.ghost > .inner {
  display: inline-block;
  vertical-align: middle;
}
```

## 七、移动端适配与媒体查询
