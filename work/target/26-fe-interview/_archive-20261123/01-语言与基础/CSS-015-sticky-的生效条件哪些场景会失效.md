---
title: [CSS-015] sticky 的生效条件？哪些场景会失效？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-015：sticky 的生效条件？哪些场景会失效？

**答**：
- 必须显式设置 `top/bottom/left/right` 中的至少一个阈值。
- 元素在其最近的滚动祖先内吸附，且**不能超出父容器的边界**，父容器滚出视口时随之消失。
- 祖先设置 `overflow: hidden/auto/scroll` 会改变滚动容器，常导致 sticky 失效。
- 表格中的 `thead th { position: sticky }` 是典型应用，注意父级不能有 overflow 裁剪。

```css
/* 生效示例 */
.sidebar {
  position: sticky;
  top: 20px;          /* 距视口 20px 时吸附 */
  align-self: flex-start; /* flex 子项需此项，防止被拉伸 */
}

/* 失效示例一：没有阈值 */
.bad-sticky-1 { position: sticky; }

/* 失效示例二：父容器 overflow 裁剪 */
.scroll-wrap { overflow: hidden; }
.scroll-wrap .bad-sticky-2 { position: sticky; top: 0; }
```
