---
title: [BAS-069] CSS scroll-snap 怎么做轮播/整屏滚动？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-069：CSS scroll-snap 怎么做轮播/整屏滚动？
**答**：
- 滚动容器设 `scroll-snap-type`（如 x mandatory），子项设 `scroll-snap-align: start/center/end`，滚动结束后自动吸附。
- mandatory 强制吸附，proximity 接近吸附点才吸；容器配 scroll-padding 处理吸顶导航遮挡。
- 纯 CSS 轮播 = 横向 overflow 滚动 + snap，比 JS 轮播库轻量且保留原生滚动手感。

```css
.carousel {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-padding-left: 16px;
}
.carousel > * {
  flex: 0 0 100%;
  scroll-snap-align: start;
}
```
