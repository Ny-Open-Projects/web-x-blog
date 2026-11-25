---
title: [XP-380] 跨端轮播图（Swiper）的性能
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-380：跨端轮播图（Swiper）的性能

**答**：
- 实现：transform 平移 + 循环克隆（首尾无缝）、自动播放暂停（页面不可见）。
- 性能：图片懒加载（相邻预载）、拖拽手势与动画统一（拖拽中禁自动播）。
- 跨端：各端 swiper 组件参数映射（autoplay/loop/circular）。

```javascript
// 轮播核心
function carousel({ count, w }) {
  let index = 0;
  return {
    go(i) { index = ((i % count) + count) % count;
      return `translateX(${-index * w}px)`; },
    next() { return this.go(index + 1); },
    visibilityPause(hidden, timer) {
      if (hidden) clearInterval(timer);                // 页面隐藏暂停
      else return timer = setInterval(() => this.next(), 3000);
    },
  };
}
```
