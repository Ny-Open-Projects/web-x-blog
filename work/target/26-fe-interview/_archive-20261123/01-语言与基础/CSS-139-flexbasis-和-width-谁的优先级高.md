---
title: [CSS-139] flex-basis 和 width 谁的优先级高？content 关键字是什么语义？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-139：flex-basis 和 width 谁的优先级高？content 关键字是什么语义？

**答**：
- `flex-basis` 有确定值（非 auto）时优先于 width，width 完全被忽略。
- `flex-basis: auto`（默认）时回退读取 width；width 也没写则用 content 尺寸。
- `flex-basis: content` 显式声明“以内容尺寸为基准”，无视 width，适合让按钮/标签按文字自适应。
- 基准值仍受 `min-width/max-width` 截断；`flex: 1` 复合写法等价 `flex: 1 1 0%`，basis 归零后宽度完全由 grow 比例决定。

```css
.item {
  width: 100px;
  flex-basis: 300px;    /* 有值优先：width: 100px 被忽略 */
  flex-grow: 1;
}
.item-auto {
  /* basis 为 auto，回退用 width */
  width: 120px;
}
.item-content {
  flex-basis: content;  /* 以内容尺寸为基准，无视任何 width */
  flex-shrink: 0;
}
.item-flex1 { flex: 1; } /* 等价 flex: 1 1 0%，宽度完全按 grow 比例分 */
/* 以上基准都会再被 min-width / max-width 截断 */
```
