---
title: [CSS-249] gap 在 flex 里能用吗，与 margin 方案对比
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 布局]
type: 面试题
---

## CSS-249：gap 在 flex 里能用吗，与 margin 方案对比

**答**：
- 能用：flex 容器自 2021 起全面支持 gap——现代 flex 布局首选间距方案
- 相比 margin 的优势：无首尾多余间距问题（margin 要 :last-child 重置）、换行时自动正确（row-gap 处理行距）、间距语义集中一处
- 兼容注意：老项目（2021 前 Safari）回退用 margin 方案；@supports (gap: 1px) 检测后渐进替换
- gap 优先于 justify-content 的 space-between：后者依赖子项数量，gap 更稳定
- 面试钩子：gap 是布局级「间距抽象」，grid/flex/multi-column 三处语义一致

```css
/* 旧方案 */
.list > * + * { margin-left: 12px; }        /* 兄弟选择器 */
/* 新方案 */
.list { display: flex; gap: 12px; }         /* 一行，无边界问题 */
.grid { display: grid; gap: 12px 24px; }    /* 行列独立 */
```
