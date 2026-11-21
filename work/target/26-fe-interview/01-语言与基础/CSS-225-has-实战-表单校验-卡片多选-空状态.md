---
title: [CSS-225] :has 实战：表单校验/卡片多选/空状态
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 选择器]
type: 面试题
---

## CSS-225：:has 实战三例：表单校验、卡片多选、空状态

**答**：
- 表单校验态：`:has(input:invalid)` 让错误态样式上浮到整组（label、边框一起变）——以前要 JS 加 class
- 卡片多选：checkbox 隐藏 + `label:has(input:checked)` 选中态样式，零 JS 实现多选 UI
- 空状态：`:has(~)` 兄弟检测或 `:has(+ :last-child)` 判断列表为空显示占位（配合 :only-child）
- 共同价值：把「结构关系驱动的 UI 状态」还给 CSS，JS 只管数据

```css
/* 表单组校验态 */
.form-group:has(input:invalid) { --border: #e33; }
.form-group:has(input:invalid) .hint { visibility: visible; }

/* 卡片多选 */
.card:has(input:checked) { outline: 2px solid #4285f4; }
.card input { position: absolute; opacity: 0; }

/* 空状态 */
.list:not(:has(li)) { display: none; }
.list:has(li) + .empty { display: none; }
```
