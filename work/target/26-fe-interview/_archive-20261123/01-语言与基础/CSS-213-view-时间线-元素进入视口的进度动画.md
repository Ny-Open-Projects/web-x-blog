---
title: [CSS-213] view() 时间线：元素进入视口的进度动画
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 动画]
type: 面试题
---

## CSS-213：view() 时间线：元素进入视口的进度动画

**答**：
- `animation-timeline: view()`：动画进度绑定「该元素自己在视口中的可见进度」——元素从视口底部进入（0%）到顶部离开（100%）
- 三个阶段：entry（进入视口）、cover（贯穿）、exit（离开）；默认 cover 全程
- range 截取：`view-timeline-range: entry 0% entry 100%` 只在进入阶段播放动画——配合关键帧实现「进入时浮现」
- 典型应用：滚动列表逐项浮现、图片进出视口的视差、阅读进度高亮
- 注意：view() 绑定的是「应用动画的元素自身」，父容器才是滚动源；需在支持浏览器加 @supports 降级

```css
.reveal-item {
  opacity: 0;
  transform: translateY(40px);
  animation: fade-up linear both;
  animation-timeline: view();
  animation-range: entry 10% entry 80%; /* 进入视口前 80% 完成 */
}
@keyframes fade-up { to { opacity: 1; transform: none; } }
```
