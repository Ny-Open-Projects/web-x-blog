---
title: [CSS-009] 什么是 BFC？触发条件有哪些？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-009：什么是 BFC？触发条件有哪些？

**答**：
- BFC（Block Formatting Context）块级格式化上下文，是一块独立的渲染区域，内部布局不影响外部。
- 触发条件：根元素、`float` 非 none、`position: absolute/fixed`、`display: inline-block/table-cell/flex/grid/flow-root`。
- `overflow: hidden/auto/scroll` 也可触发，但可能裁剪内容或产生滚动条。
- `display: flow-root` 是无副作用的专用触发方式，现代浏览器首选。
- BFC 三大特性：隔离 margin 合并、包含浮动、不与浮动元素重叠。

```css
/* 各种触发 BFC 的方式 */
.bfc-root   { display: flow-root; }      /* 推荐，无副作用 */
.bfc-overflow { overflow: auto; }         /* 可能有滚动条 */
.bfc-float  { float: left; }              /* 影响文档流 */
.bfc-abs    { position: absolute; }       /* 脱离文档流 */
.bfc-flex   { display: flex; }            /* 内部变成 flex 格式化上下文 */
.bfc-table  { display: table-cell; }
```
