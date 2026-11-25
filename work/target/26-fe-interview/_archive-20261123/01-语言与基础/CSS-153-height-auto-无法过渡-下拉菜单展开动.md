---
title: [CSS-153] height: auto 无法过渡，下拉菜单展开动画怎么做？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-153：height: auto 无法过渡，下拉菜单展开动画怎么做？

**答**：
- 困境：transition 需要起止都是确定值，auto ↔ 固定 px 只有一端确定，动画直接跳变。
- 现代方案：容器 `grid-template-rows: 0fr ↔ 1fr`，fr 轨道可以插值；内层 `min-height: 0 + overflow: hidden` 让内容被轨道裁剪。
- 效果等同 height auto 动画且零 JS 测量；Baseline 已覆盖主流浏览器，旧内核降级为 max-height 方案或直接瞬切。
- 配合 `visibility` 延迟切换，保证收起后不可聚焦。

```css
/* 结构：.dropdown > .panel > 真实内容 */
.dropdown {
  display: grid;
  grid-template-rows: 0fr;              /* 收起：轨道高 0 */
  transition: grid-template-rows .3s ease, visibility .3s;
  visibility: hidden;                   /* 收起后不可聚焦不可读屏 */
}
.dropdown.open {
  grid-template-rows: 1fr;              /* 展开：轨道吃满内容高 */
  visibility: visible;
}
.dropdown > .panel {
  overflow: hidden;                     /* 内容被 0fr 轨道裁掉 */
  min-height: 0;                        /* 允许轨道收缩，关键 */
}
/* 旧内核降级：max-height 给一个足够大的固定值近似动画 */
.dropdown-fallback > .panel {
  max-height: 0;
  overflow: hidden;
  transition: max-height .3s;
}
.dropdown-fallback.open > .panel { max-height: 400px; }
```
