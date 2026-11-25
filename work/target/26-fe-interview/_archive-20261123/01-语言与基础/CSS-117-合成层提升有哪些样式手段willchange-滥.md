---
title: [CSS-117] 合成层提升有哪些样式手段？will-change 滥用怎么治理？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-117：合成层提升有哪些样式手段？will-change 滥用怎么治理？

**答**：
- 提升手段：`will-change: transform`、`transform: translateZ(0)`、`opacity < 1`、`position: fixed`、`filter/mask` 等都会创建合成层。
- 每个合成层都要独立位图与内存（大图放大十倍内存也放大），层爆炸是滚动卡顿与崩溃的常见根因。
- 治理原则：只给"确定要动画的元素"提升；动画开始前加 will-change，结束后移除（或由动画库托管）。
- translateZ(0) 强提是历史 hack，现代浏览器会自动为运行中动画提升，无脑全站加是反模式。
- 审计工具：DevTools Layers 面板逐层看内存与尺寸，Memory 面板看层树总量。

```css
/* 1. 正确用法：预告即将发生的动画，动完即撤 */
.carousel-track { transition: transform 0.4s var(--ease-out); }
.carousel-track.is-animating { will-change: transform; }

/* 2. 反例：全站无脑提升，内存白花 */
/* .card, .list-item, .badge, .modal { transform: translateZ(0); } ← 禁止 */

/* 3. 动画结束移除（JS 侧） */
track.addEventListener('transitionend', () => {
  track.classList.remove('is-animating'); // 释放合成层
}, { once: true });
```
