---
title: [CSS-212] 滚动驱动动画 animation-timeline: scroll() 语法详解
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 动画]
type: 面试题
---

## CSS-212：滚动驱动动画 animation-timeline: scroll() 语法详解

**答**：
- 滚动驱动动画：动画进度由滚动位置决定而非时间——滚动条就是时间轴
- 语法两步：`animation-timeline: scroll()` 绑定滚动源 + `animation-fill-mode` 配合；scroll() 参数：`scroll(<scroller> <axis>)`——root/nearest/self 与 block/inline/x/y
- 时间轴两种：scroll()（容器整体滚动进度）与 view()（元素进入视口的可见进度）
- 命名时间轴：scroll-timeline-name 定义在滚动容器，animation-timeline-name 引用（跨元素关联）
- 关键帧语义变化：0% 是滚动起点、100% 是滚动终点，与时间无关

```css
.scroll-progress {
  position: fixed; top: 0; left: 0;
  height: 4px; width: 100%;
  transform-origin: 0 50%;
  background: #4285f4;
  animation: grow linear both;
  animation-timeline: scroll(root block); /* 整页滚动 */
}
@keyframes grow { from { transform: scaleX(0); } to { transform: scaleX(1); } }
```
