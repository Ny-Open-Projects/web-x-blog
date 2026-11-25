---
title: [CSS-098] ::first-letter 首字下沉怎么做？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-098：::first-letter 首字下沉怎么做？

**答**：
- `::first-letter` 匹配块级容器首行首个字母（含紧邻标点），可独立设置字号/浮动/颜色。
- 首字下沉两板斧：`initial-letter: 3`（Chrome/Safari 支持，自动占 3 行）或 `float: left + font-size`（兼容全）。
- `::first-line` 可给首行整行加样式，常与 first-letter 搭配。
- 只对块级容器生效，行内元素与 display: contents 无效。

```css
/* 兼容方案：float 下沉 */
.article > p:first-of-type::first-letter {
  float: left;
  font-size: 3.2em;
  line-height: 1;
  padding-inline-end: 8px;
  font-weight: 600;
  color: var(--brand);
}

/* 现代方案：initial-letter 精确占 N 行，无需算行高 */
@supports (initial-letter: 3) {
  .article > p:first-of-type::first-letter {
    float: none;
    initial-letter: 3 3;   /* 占 3 行，基线对齐第 3 行 */
    font-size: unset;
  }
}

/* 首行整体加粗 */
.article > p::first-line { font-weight: 600; }
```
