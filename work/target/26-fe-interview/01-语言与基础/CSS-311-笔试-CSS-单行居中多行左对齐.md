---
title: [CSS-311] 笔试：CSS 单行居中、多行左对齐
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 排版]
type: 笔试题
---

## CSS-311：笔试：单行居中、多行左对齐

**题目**：经典排版题：文字只有一行时居中显示，超过一行时左对齐（标签、提示语场景）。不能用 JS 判断行数。

**答**：
```css
/* 方案一：text-align: center + 内联块（最经典） */
.wrap {
  text-align: center;      /* 行内内容居中 */
}
.label {
  display: inline-block;   /* 收缩为内容宽 */
  text-align: left;        /* 内部恢复左对齐——多行时生效 */
  max-width: 100%;
}
/* 原理：单行时 inline-block 收缩=行宽，视觉居中；
   多行时内部宽度超过容器触发换行，text-align:left 生效 */

/* 方案二：现代 fit-content 居中 */
.wrap2 { display: flex; justify-content: center; }
.label2 { max-width: 100%; text-align: left; }
```
```html
<div class="wrap">
  <span class="label">短的提示</span>
</div>
<div class="wrap">
  <span class="label">很长很长会换行的提示文字超过容器宽度后自动左对齐显示</span>
</div>
```

**评分点**：
- 「inline-block 收缩 + 父级 text-align: center」的经典组合与原理阐述
- 内部 text-align: left 恢复多行左对齐
- flex + fit-content 的现代等价写法
- 无 JS、无行数检测的思路正确性
