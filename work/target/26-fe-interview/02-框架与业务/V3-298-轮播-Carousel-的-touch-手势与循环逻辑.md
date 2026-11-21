---
title: [V3-298] 轮播（Carousel）的 touch 手势与循环切换逻辑怎么实现？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-298：轮播（Carousel）的 touch 手势与循环切换逻辑怎么实现？
**答**：
- 手势：touchstart 记录起点，touchmove 计算位移实时 translate（跟手），touchend 按位移+速度（fling）判定切页或回弹；速度阈值防"轻滑误切"。
- 循环：无缝循环用**克隆首尾**（渲染 length+2 个，位置偏移 -1），或双视图切换（渲染当前+相邻，切换时 teleport DOM 节点）；克隆法简单，DOM 数量可控时优先。
- 动画：transition 期间禁用手势打断或支持"跟手中断"（touchstart 立即取当前 translate 作为起点）。
- 自动播放：定时器 + 交互暂停（hover/触摸时 clear），页面不可见时暂停（visibilitychange）。
- 纵向滑动冲突：垂直手势时阻止轮播接管（判定主轴），容器 preventDefault 策略按 scroll 方向配置。

```typescript
function useSwipe(el, { onSwipe, width }) {
  let startX = 0, startY = 0, offset = 0, active = false;
  el.addEventListener('touchstart', (e) => {
    startX = e.touches[0].clientX; startY = e.touches[0].clientY;
    offset = 0; active = true;
  }, { passive: true });
  el.addEventListener('touchmove', (e) => {
    if (!active) return;
    const dx = e.touches[0].clientX - startX;
    const dy = e.touches[0].clientY - startY;
    if (Math.abs(dy) > Math.abs(dx)) { active = false; return; } // 主轴判定：垂直手势不接管
    offset = dx;
    el.style.transform = `translateX(${-current() * width + offset}px)`; // 跟手
  });
  el.addEventListener('touchend', () => {
    if (!active) return;
    active = false;
    if (Math.abs(offset) > width / 3) onSwipe(offset < 0 ? 1 : -1);  // 过半切页
    else el.style.transform = `translateX(${-current() * width}px)`; // 回弹
  });
}
```
