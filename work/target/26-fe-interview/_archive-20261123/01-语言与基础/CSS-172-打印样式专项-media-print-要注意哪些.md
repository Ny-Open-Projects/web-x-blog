---
title: [CSS-172] 打印样式专项（@media print）要注意哪些点？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-172：打印样式专项（@media print）要注意哪些点？

**答**：
- 隐藏交互件（nav/按钮/侧栏广告），正文黑字白底；链接打印后丢失可点击性，用 `::after content: attr(href)` 补 URL。
- 分页三控：`break-inside: avoid` 防元素被拦腰截断、`break-before: page` 章节起新页、`break-after: avoid` 让标题不孤行。
- 表格跨页：`thead { display: table-header-group }` 让表头每页重复。
- `@page` 控制纸张边距与尺寸；配色打印成本高，默认去掉大面积底色，`print-color-adjust` 仅在必须保留底色时使用。

```css
@media print {
  /* 1. 隐藏交互与辅助元素 */
  nav, .sidebar, button, .ads, .comment-form { display: none; }

  /* 2. 打印友好配色 */
  body { color: #000; background: #fff; }
  a { text-decoration: none; color: inherit; }
  a[href]::after { content: " (" attr(href) ")"; }  /* 补链接地址 */

  /* 3. 分页控制 */
  article { break-inside: avoid; }
  h2 { break-after: avoid; }          /* 标题不与内容分离 */
  .chapter { break-before: page; }    /* 每章新起一页 */
  table { break-inside: avoid; }
  thead { display: table-header-group; }  /* 跨页重复表头 */

  /* 4. 纸张设置 */
  @page { size: A4; margin: 2cm; }
  /* 必须保留底色的元素（如色卡） */
  .swatch { print-color-adjust: exact; -webkit-print-color-adjust: exact; }
```
}

## 二十八、移动端深坑全解
