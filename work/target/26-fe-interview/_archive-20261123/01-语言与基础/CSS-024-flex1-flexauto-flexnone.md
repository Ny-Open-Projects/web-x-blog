---
title: [CSS-024] flex:1、flex:auto、flex:none 的区别？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-024：flex:1、flex:auto、flex:none 的区别？

**答**：
- `flex: 1` = `1 1 0%`：完全忽略内容尺寸，按 grow 份数严格均分。
- `flex: auto` = `1 1 auto`：先按内容分配，再均分剩余空间，各项基础尺寸不同。
- `flex: none` = `0 0 auto`：固定内容尺寸，不伸不缩。
- `flex: initial` = `0 1 auto`：不伸但可缩，即默认值。
- 布局诉求“等分”用 flex:1，“自适应内容但瓜分剩余”用 auto。

```css
.eq   { flex: 1; }    /* 1 1 0%   严格等分 */
.grow { flex: auto; } /* 1 1 auto 内容优先 */
.fixed{ flex: none; } /* 0 0 auto 固定尺寸，如固定侧栏 */
/* 经典三栏：固定侧栏 + 自适应主区 */
.layout { display: flex; }
.layout .side  { flex: none; width: 220px; }
.layout .main  { flex: 1; min-width: 0; }
```
