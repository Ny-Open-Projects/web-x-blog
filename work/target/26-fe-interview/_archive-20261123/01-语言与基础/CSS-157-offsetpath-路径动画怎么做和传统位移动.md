---
title: [CSS-157] offset-path 路径动画怎么做？和传统位移动画差在哪？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-157：offset-path 路径动画怎么做？和传统位移动画差在哪？

**答**：
- `offset-path: path(...)` 把元素锚定到一条 SVG 路径上，`offset-distance` 从 0% 到 100% 即沿路径运动。
- 传统 keyframes 位移动画只能折线近似曲线且帧数有限；offset-path 是真实贝塞尔轨迹，配合 `offset-rotate: auto` 元素自动沿切线转向。
- 也可引用 SVG 里的 `<path id>`（`offset-path: url(#p)`），设计稿路径可直接复用。
- 兼容：Chrome/Firefox 良好，Safari 较新版本支持；降级方案是拆解 keyframes 模拟。

```css
.orb {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: #096;
  /* 贝塞尔曲线路径，坐标系以元素容器左上角为原点 */
  offset-path: path("M 10 80 C 40 10 65 10 95 80 S 150 150 180 80");
  offset-distance: 0%;
  offset-rotate: auto;      /* 自动沿切线旋转，reverse 为反向 */
  animation: fly 4s linear infinite;
}
@keyframes fly {
  to { offset-distance: 100%; }
}
/* 定点停靠：offset-distance: 50% + transition 即可做路径进度条 */
.orb-halt { offset-distance: 50%; transition: offset-distance 1s; }
```
