---
title: [CSS-029] grid-template-areas 如何实现经典页面布局？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-029：grid-template-areas 如何实现经典页面布局？

**答**：
- 给每个网格区域命名，项目用 `grid-area` 对号入座，布局一目了然。
- 同名区域自动合并成一个矩形块，必须保证每行字符串的列数一致。
- 响应式改版只需改容器一行模板，项目代码完全不动。
- 空区域用 `.` 占位。

```css
/* HTML: header / nav / main / aside / footer 五个语义标签 */
.page {
  display: grid;
  grid-template-areas:
    "header header header"
    "nav    main   aside"
    "footer footer footer";
  grid-template-columns: 200px 1fr 260px;
  grid-template-rows: 64px 1fr 80px;
  min-height: 100vh;
  gap: 12px;
}
.page > header { grid-area: header; }
.page > nav    { grid-area: nav; }
.page > main   { grid-area: main; }
.page > aside  { grid-area: aside; }
.page > footer { grid-area: footer; }
```
