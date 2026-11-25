---
title: [XP-373] 跨端滚动吸顶/悬浮 Tab 的实现差异
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-373：跨端滚动吸顶/悬浮 Tab 的实现差异

**答**：
- H5：position: sticky（简单）；小程序：页面 onPageScroll 计算（节流）或 sky-line 原生；RN：Animated + onScroll。
- 性能：滚动回调节流（rAF）、吸顶检测用 IO 预估而非每帧测量。
- 闪烁：吸顶瞬间高度跳变（占位元素预置）。

```javascript
// 吸顶统一
function stickyTab(io) {
  const sentinel = document.createElement('div');
  sentinel.style.height = '1px';
  io.observe(sentinel);
  return new Promise(res => new IntersectionObserver(es => {
    res(es[0].intersectionRatio === 0);              // sentinel 离屏即吸顶
  }).observe(sentinel));
}
```
