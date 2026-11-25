---
title: [CSS-047] animation 与 @keyframes 的用法？常用子属性有哪些？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-047：animation 与 @keyframes 的用法？常用子属性有哪些？

**答**：
- `@keyframes` 定义关键帧，`animation` 应用到元素；简写顺序 duration 与 delay 同 transition。
- 常用子属性：name、duration、timing-function、delay、iteration-count、direction、fill-mode、play-state。
- `fill-mode: forwards` 让动画停留在最后一帧，`backwards` 应用 delay 期间的第一帧样式。
- `direction: alternate` 来回播放，`play-state: paused` 配合 JS 做播放控制。

```css
@keyframes fade-slide-in {
  from {
    opacity: 0;
    transform: translateY(16px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.toast {
  animation: fade-slide-in 0.3s ease-out 0.1s both;
  /* both = backwards + forwards：延迟期间就位 + 结束保持 */
}

.carousel-track {
  animation: scroll 8s linear infinite alternate;
  animation-play-state: running;
}
.carousel-track.paused { animation-play-state: paused; }
@keyframes scroll {
  from { transform: translateX(0); }
  to   { transform: translateX(-50%); }
}
```
