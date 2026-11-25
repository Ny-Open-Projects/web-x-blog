---
title: [CSS-252] subgrid 是什么：嵌套网格对齐
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 布局]
type: 面试题
---

## CSS-252：subgrid 是什么：嵌套网格对齐

**答**：
- subgrid：子元素把父网格的轨道定义「继承」下来——嵌套网格与父网格的行列严格对齐
- 解决的问题：卡片网格里「标题区高度不一致」——卡片内部用 subgrid 继承父的行轨道，所有卡片的标题/正文行对齐
- 语法：`grid-template-rows: subgrid;`（沿父行轨道）；可指定 `subgrid auto` 数量
- 与嵌套 grid 的区别：普通嵌套是「独立网格」，尺寸各自算；subgrid 是「共享轨道」
- 兼容：Chrome 117+/Firefox 71+（最早实现）/Safari 16+，已可生产

```css
.grid { display: grid; grid-template-columns: repeat(3, 1fr); }
.card {
  display: grid;
  grid-row: span 3;             /* 占三行 */
  grid-template-rows: subgrid;  /* 继承父的行轨道 */
}
/* 所有卡片：标题行对齐、正文行对齐、底栏对齐 */
```
