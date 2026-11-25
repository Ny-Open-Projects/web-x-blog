---
title: [BAS-062] position: sticky 生效需要什么条件？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-062：position: sticky 生效需要什么条件？
**答**：
- 必须至少指定 top/right/bottom/left 之一，否则等于 relative 不吸附。
- 任一祖先的 overflow 不是 visible（如 hidden/auto/scroll）会让 sticky 失效——最常见的坑；父级 B 和祖先链都要检查。
- 吸附范围被限制在父元素内：父元素滚出视口，sticky 元素跟着离开；且元素不能比父容器还高。

```css
/* 表头吸顶：注意父级链上不能有 overflow: hidden */
.table-wrap { height: 500px; overflow: auto; }
th {
  position: sticky;
  top: 0;
  background: #fff;
  z-index: 1;
}
```
