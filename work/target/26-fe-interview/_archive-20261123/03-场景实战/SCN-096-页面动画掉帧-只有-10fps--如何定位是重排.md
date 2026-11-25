---
title: [SCN-096] 页面动画掉帧（只有 10fps），如何定位是重排、重绘还是合成层问题，并修复？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-096：页面动画掉帧（只有 10fps），如何定位是重排、重绘还是合成层问题，并修复？
**答**：
- 定位用 DevTools：Performance 录制看主线程与合成器线程；Rendering 面板开 Paint flashing（绿闪为重绘）与 Layout Shift Regions，区分掉帧来自 layout/paint/composite 哪一层。
- 修复三原则：只动 transform/opacity 合成属性；will-change 提前提升合成层但用完即删（防层爆炸）；contain 与 content-visibility 缩小重排范围、跳过视口外渲染。
- 修复后用 FPS 探针量化验证（稳定接近 60 才算达标），不靠肉眼。

```css
/* 动画性能三原则落地：只动合成属性 + 层隔离 + 防层爆炸 */
.card {
  /* 反例：transition: left .3s  每帧触发 layout，必掉帧 */
  transform: translateX(0);
  transition: transform .3s;     /* transform 走合成器线程，不占主线程 */
  will-change: transform;        /* 提前提升合成层，首帧不掉坑 */
  contain: layout paint;         /* 内部变化不外溢，缩小重排重绘范围 */
}

/* 长列表：视口外的行跳过渲染，滚动立刻流畅 */
.long-list > * {
  content-visibility: auto;
  contain-intrinsic-size: auto 48px;   /* 占位高度防滚动条跳动 */
}

/* 防层爆炸：will-change 用完即删，不能全量加在几百个节点上 */
.card.animating { will-change: transform; }
.card:not(.animating) { will-change: auto; }
```
