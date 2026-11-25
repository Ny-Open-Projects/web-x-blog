---
title: [CSS-082] animation-timing 曲线怎么设计？cubic-bezier 如何调出回弹？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-082：animation-timing 曲线怎么设计？cubic-bezier 如何调出回弹？

**答**：
- `cubic-bezier(x1, y1, x2, y2)` 用两个控制点描述进度-时间曲线，x 限 0~1，y 可以超出产生过冲。
- y > 1 即"冲过头再回来"，是 CSS 里模拟 spring 回弹的通用手法，如 `cubic-bezier(0.34, 1.56, 0.64, 1)`。
- 进场用 ease-out（快进缓停），退场用 ease-in，位移切换用 ease-in-out；默认 ease 反而多数场景不合适。
- Chrome DevTools 中点击 timing 图标可拖拽贝塞尔手柄实时预览，调好再固化。
- 多属性动画可各自指定 timing，让位移与透明度节奏分离更高级。

```css
/* 常用曲线 token 化，全站统一动效语言 */
:root {
  --ease-out:    cubic-bezier(0.22, 1, 0.36, 1);   /* 进场：快进缓停 */
  --ease-in:     cubic-bezier(0.64, 0, 0.78, 0);   /* 退场 */
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1); /* 回弹：y 超过 1 产生过冲 */
}

.toast-enter  { animation: slide-up 0.3s var(--ease-out) both; }
.toast-leave  { animation: slide-up 0.25s var(--ease-in) both reverse; }

.pop-confirm {
  animation: pop 0.4s var(--ease-spring) both;
}
@keyframes pop {
  from { transform: scale(0.6); opacity: 0; }
  to   { transform: scale(1);   opacity: 1; }
}
```
