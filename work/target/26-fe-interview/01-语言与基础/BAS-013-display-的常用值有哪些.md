---
title: [BAS-013] display 的常用值有哪些？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-013：display 的常用值有哪些？
**答**：
- 基础三类：block / inline / inline-block。
- 布局容器：flex / grid（以及行内版 inline-flex / inline-grid）。
- none：不渲染不占空间，区别于 visibility: hidden 占空间不可见。
- 进阶：contents 让盒子自身消失、子元素直接参与父级布局；flow-root 用于创建 BFC 清除浮动。

```css
.nav    { display: flex; gap: 12px; }
.grid   { display: grid; grid-template-columns: repeat(3, 1fr); }
.badge  { display: inline-block; padding: 2px 8px; }
.modal  { display: none; }        /* 隐藏且不占空间 */
.helper { display: flow-root; }   /* 创建 BFC，解决子元素浮动塌陷 */
```
