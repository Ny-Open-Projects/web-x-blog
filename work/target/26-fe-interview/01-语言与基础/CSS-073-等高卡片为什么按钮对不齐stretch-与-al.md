---
title: [CSS-073] 等高卡片为什么按钮对不齐？stretch 与 align-items 有什么陷阱？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-073：等高卡片为什么按钮对不齐？stretch 与 align-items 有什么陷阱？

**答**：
- flex 默认 `align-items: stretch` 已让卡片等高，但一行代码 `align-items: center` 就会覆盖成各自高度。
- 卡片等高后，内容长短不同导致 footer 位置参差：给 footer 加 `margin-top: auto` 把它推到底部。
- Grid 单行同样自动等高；多行不等高时用 `grid-auto-rows: 1fr` 强制每行等分。
- 图片/标题占位高度用 `aspect-ratio` 或固定 min-height 锁定，从源头减少参差。

```css
.card-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 16px;
  align-items: stretch;  /* 默认已等高，别写成 center */
}

.card {
  display: flex; flex-direction: column;
  height: 100%;
}
.card .thumb { aspect-ratio: 16 / 9; }        /* 占位锁定，防高度参差 */
.card .desc  { flex: 1; }                      /* 中间内容吃掉剩余空间 */
.card footer { margin-top: auto; }             /* 按钮一律沉底对齐 */

/* 多行场景：每行内部也等高 */
.card-list.even-rows { grid-auto-rows: 1fr; }
```
