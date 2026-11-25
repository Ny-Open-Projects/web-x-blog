---
title: [CSS-124] subgrid 解决什么问题？怎么用？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-124：subgrid 解决什么问题？怎么用？

**答**：
- 问题：嵌套 Grid 的子网格轨道与父网格对不上，卡片内标题/正文/按钮无法跨卡对齐。
- `grid-template-rows: subgrid`（或 columns）让子元素继承父网格的对应轨道定义，共享行高。
- 子元素占多行用 `grid-row: span 3`，内部再按继承轨道摆放，天然跨卡对齐。
- Baseline 2023，三大家族全支持；不支持的环境回退为普通轨道（布局仍可用，仅对齐退化）。

```css
.cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

.card {
  display: grid;
  grid-row: span 3;
  grid-template-rows: subgrid;  /* 三段行高继承父网格，跨卡严格对齐 */
  gap: 8px;
}

.card h3 { grid-row: 1; }      /* 标题行 */
.card p  { grid-row: 2; }      /* 内容行 */
.card footer { grid-row: 3; }  /* 按钮行：所有卡片底部对齐 */
```
