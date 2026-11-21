---
title: [CSS-021] align-items 与 align-self 的关系？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-021：align-items 与 align-self 的关系？

**答**：
- `align-items` 是容器属性，设置所有项目的交叉轴对齐方式，默认 `stretch`。
- `align-self` 是项目属性，可单独覆盖某个项目的对齐，默认 `auto`（继承容器的 align-items）。
- `stretch` 只在项目交叉轴尺寸为 auto 时生效，设置了 height 就不再拉伸。
- `baseline` 按文本基线对齐，常用于图文混排的对齐微调。

```css
.row {
  display: flex;
  height: 120px;
  align-items: center; /* 全部垂直居中 */
}
.row .top    { align-self: flex-start; }
.row .bottom { align-self: flex-end; }
.row .full   { align-self: stretch; } /* 单独拉伸占满 */
.row .text   { align-self: baseline; }
```
