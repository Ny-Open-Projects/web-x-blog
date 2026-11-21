---
title: [BAS-064] flex/grid 的 gap 和用 margin 排间距有什么区别？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-064：flex/grid 的 gap 和用 margin 排间距有什么区别？
**答**：
- gap 只作用于项目之间，首尾项目外侧没有多余空隙，不需要负 margin 或 :last-child 清理。
- margin 方案会在末尾多出一份间距，需要容器负 margin 抵消或选择器摘除，写法繁琐。
- gap 语义更清晰，支持 row-gap/column-gap 分开设值，是现代布局排间距的首选。

```css
/* margin 方案：需要抵消尾部空隙 */
.list-margin { display: flex; margin: 0 -8px; }
.list-margin > * { margin: 0 8px; }

/* gap 方案：一行解决 */
.list-gap { display: flex; gap: 16px; }
```
