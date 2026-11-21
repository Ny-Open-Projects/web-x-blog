---
title: [BAS-075] content-visibility 是做什么的？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-075：content-visibility 是做什么的？
**答**：
- `content-visibility: auto` 让屏幕外元素跳过渲染（布局与绘制），长列表/长页面首屏渲染大幅提速。
- 配合 `contain-intrinsic-size` 给屏幕外元素估算占位尺寸，防止滚动条跳动。
- 与虚拟滚动区别：零 JS、保留真实 DOM，优化的是渲染而非 DOM 数量。

```css
section.feed-item {
  content-visibility: auto;
  contain-intrinsic-size: auto 300px;  /* 屏幕外按估算高度占位 */
}
```
