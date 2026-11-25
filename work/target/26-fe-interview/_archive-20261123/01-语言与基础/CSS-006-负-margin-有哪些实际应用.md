---
title: [CSS-006] 负 margin 有哪些实际应用？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-006：负 margin 有哪些实际应用？

**答**：
- 负 `margin-top/left` 会把元素向上/向左拉，负 `margin-bottom/right` 会让后续元素贴上来。
- 经典应用：等高多列布局、圣杯/双飞翼布局的中间列让位。
- 消除列表最后一项的多余间距：给容器加负 margin-bottom 抵消。
- 配合 `padding` 可以实现“撑大自身但不改变内容宽度”的视觉扩展（如输入框 focus 外扩）。

```css
/* 应用一：列表末项多余间距抵消 */
.tag-list {
  margin-right: -10px; /* 抵消每个 tag 的右边距 */
  overflow: hidden;
}
.tag-list .tag {
  float: left;
  margin-right: 10px;
  margin-bottom: 10px;
}

/* 应用二：双飞翼布局，中间列优先渲染 */
.main { float: left; width: 100%; }
.sub  { float: left; width: 190px; margin-left: -100%; }
.extra{ float: left; width: 230px; margin-left: -230px; }
```
