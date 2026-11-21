---
title: [CSS-137] 表单的 label 有哪几种对齐方案？各自适用场景？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-137：表单的 label 有哪几种对齐方案？各自适用场景？

**答**：
- 顶对齐（label 在输入框上方）：标签与输入框阅读视线最短，移动端和长表单首选；纵向占用高。
- 左对齐（固定宽度列）：label 右对齐 + 输入框左对齐形成两列，桌面后台最常见；label 过长会挤压空间。
- 内嵌浮动 label（Material 风格）：label 融入输入框，聚焦或已有值时上浮缩小，靠 `:focus` 与 `:not(:placeholder-shown)` 两个状态驱动。
- 内嵌方案要求 label 写在 input 之后（兄弟选择器向后看），且 input 必须带 placeholder=" "。

```css
/* 方案一：顶对齐，移动端首选 */
.form-top .field { display: flex; flex-direction: column; gap: 4px; }

/* 方案二：左对齐，固定 label 列宽，输入框纵向对齐 */
.form-left .field {
  display: grid;
  grid-template-columns: 96px 1fr;
  align-items: center;
  gap: 12px;
}
.form-left label { text-align: right; }

/* 方案三：内嵌浮动 label，DOM 顺序 input 在前 label 在后 */
.form-inline .field { position: relative; }
.form-inline input { padding: 14px 12px 4px; }
.form-inline label {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  color: #999;
  transition: all .2s;
  pointer-events: none;
}
.form-inline input:focus + label,
.form-inline input:not(:placeholder-shown) + label {
  top: 12px;
  transform: none;
  font-size: 12px;
  color: #096;
}
```
