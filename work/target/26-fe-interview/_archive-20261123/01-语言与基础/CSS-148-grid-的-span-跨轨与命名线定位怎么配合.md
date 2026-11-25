---
title: [CSS-148] grid 的 span 跨轨与命名线定位怎么配合使用？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-148：grid 的 span 跨轨与命名线定位怎么配合使用？

**答**：
- 命名线：在 grid-template-columns 里用 `[name]` 给线命名，同名可重复（自动 name1/name2），定位写 `grid-column: full-start / full-end`。
- span：`grid-column: span 2` 表示“占两轨，具体位置交给自动放置”，与命名线可以混写 `content-start / span 2`。
- 负数线索引从末尾往前数（-1 是最后一条线），动态列数时特别有用。
- 排版系统（全宽通栏 + 居中内容列）是命名线的经典落地。

```css
.layout {
  display: grid;
  grid-template-columns:
    [full-start] minmax(1rem, 1fr)
    [content-start] minmax(0, 720px)
    [content-end] minmax(1rem, 1fr)
    [full-end];
}
.layout .hero    { grid-column: full-start / full-end; }    /* 全宽通栏 */
.layout .article { grid-column: content-start / content-end; } /* 居中正文 */
.layout .wide    { grid-column: content-start / span 2; }   /* 混用 span */
.layout .tail    { grid-column: -2 / -1; }                  /* 最后一列 */

/* 同名线重复时自动带序号：row-start 1 / row-start 2 */
.rows {
  grid-template-rows: [row-start] 80px [row-start] 80px [row-start] 80px;
}
.rows .pick { grid-row: row-start 2 / row-start 4; }
```
