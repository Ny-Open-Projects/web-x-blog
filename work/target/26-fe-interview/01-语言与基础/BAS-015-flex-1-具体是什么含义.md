---
title: [BAS-015] flex: 1 具体是什么含义？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-015：flex: 1 具体是什么含义？
**答**：
- 它是 `flex-grow: 1; flex-shrink: 1; flex-basis: 0%` 的缩写。
- grow=1 按比例分配剩余空间；shrink=1 允许在空间不足时被压缩；basis=0 表示自身不占基准宽度，完全按比例分。
- 对比：`flex: auto` 是 1 1 auto（先按内容占位再分剩余），`flex: none` 是 0 0 auto（固定不缩放）。

```css
.sidebar { flex: none; width: 200px; } /* 固定侧栏，不放大也不压缩 */
.main    { flex: 1;  }  /* 等价 flex-grow:1 flex-shrink:1 flex-basis:0% */
/* 两个 flex:1 的区域会严格平分剩余空间，与内容长短无关 */
```
