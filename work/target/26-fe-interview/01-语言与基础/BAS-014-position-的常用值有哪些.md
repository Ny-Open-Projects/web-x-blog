---
title: [BAS-014] position 的常用值有哪些？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-014：position 的常用值有哪些？
**答**：
- static：默认值，不参与定位。
- relative：相对自身原位偏移，同时是 absolute 子元素的包含块。
- absolute：相对最近的非 static 祖先定位，脱离文档流。
- fixed：相对视口定位；父级有 transform/filter 时会改为相对该祖先（高频坑）。
- sticky：滚动到阈值前是 relative、达到阈值后吸顶；需要指定 top，且祖先不能有 overflow: hidden。

```css
.tip    { position: relative; top: 4px; }               /* 原位偏移 */
.dialog { position: absolute; inset: 0; margin: auto; } /* 相对定位祖先居中 */
.toast  { position: fixed; top: 20px; right: 20px; }    /* 相对视口 */
.header { position: sticky; top: 0; }                   /* 滚动吸顶 */
```
