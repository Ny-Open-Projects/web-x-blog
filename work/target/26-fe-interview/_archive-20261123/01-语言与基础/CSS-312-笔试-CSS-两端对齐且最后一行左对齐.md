---
title: [CSS-312] 笔试：两端对齐且最后一行左对齐
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 排版]
type: 笔试题
---

## CSS-312：笔试：两端对齐且最后一行左对齐

**题目**：实现标签列表：所有行两端对齐（space-between 效果），但最后一行（可能不满）左对齐不被拉伸。常见于筛选标签组。

**答**：
```css
/* 方案一：text-align: justify + ::after 占位行 */
.tags {
  text-align: justify;
  text-align-last: justify;  /* 部分浏览器让末行也 justify */
  /* 关键：::after 占满一行，把真末行顶成「非末行」 */
}
.tags::after {
  content: '';
  display: inline-block;
  width: 100%;
}
.tag { display: inline-block; text-align: left; }

/* 方案二：flex 多行 + 伪元素补位（更可控） */
.tags-flex {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 8px;
}
/* 补充足够多的空占位，让真末行前的行都满足 space-between 条件 */
.tags-flex::after,
.tags-flex::before {
  content: '';
  order: 1;         /* 排到最后占位 */
  width: 30%;       /* 近似标签宽度 */
}
```

**评分点**：
- justify + ::after width:100% 占位行的经典技巧与原理（顶替末行）
- text-align-last 的浏览器差异意识
- flex 方案中占位元素数量/宽度不精确的局限说明
- gap 与 space-between 混用时的间距注意
