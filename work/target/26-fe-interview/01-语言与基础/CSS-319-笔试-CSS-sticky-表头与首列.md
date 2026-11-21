---
title: [CSS-319] 笔试：CSS sticky 表头与首列
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 布局]
type: 笔试题
---

## CSS-319：笔试：sticky 表头与首列

**题目**：实现大表格：滚动容器内表头固定在顶部、第一列固定在左侧（交叉角单元格两者都固定），滚动时层级正确无穿透。

**答**：
```css
.table-wrap {
  max-height: 400px;
  overflow: auto;
}
table { border-collapse: separate; border-spacing: 0; }

/* 表头吸顶 */
thead th {
  position: sticky;
  top: 0;
  background: #f6f8fa;
  z-index: 2;
}
/* 首列吸左 */
td:first-child, th:first-child {
  position: sticky;
  left: 0;
  background: #f6f8fa;
  z-index: 1;
}
/* 交叉角：两个方向都吸 + 最高层 */
thead th:first-child {
  z-index: 3;                 /* 同时吸顶和左，层级最高 */
}

/* 边界问题：sticky 需要背景遮挡滚过的内容；border-collapse: collapse 会破坏 sticky，
   必须用 separate + 每格 border */
th, td { border-bottom: 1px solid #eee; border-right: 1px solid #eee; }
```

**评分点**：
- border-collapse: separate 的必要性（collapse 会让 sticky 失效或边框错乱）——高频踩坑点
- z-index 层级分配：交叉角 3 > 表头 2 > 首列 1
- 吸附元素必须有背景色（否则透出滚动内容）
- thead th 与 td:first-child 的选择器区分
