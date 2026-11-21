---
title: [WEB-050] 什么是合成层？为什么动画推荐用 transform 和 opacity？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-050：什么是合成层？为什么动画推荐用 transform 和 opacity？
**答**：
- 页面可拆成多个图层（layer），各自独立栅格化，最后 GPU 合成；`transform`、`opacity` 动画可在合成器线程完成，不占用主线程，不触发重排重绘。
- 提升成独立合成层的条件：3D transform、`will-change: transform/opacity`、`position: fixed`、video、canvas 等。
- 层爆炸：过多元素提升为层会占大量显存，反而掉帧；用 `will-change` 要有节制，动画结束后移除。
- 验证方式：DevTools Layers 面板查看图层与绘制成本。

```css
/* 动画性能三件套：transform 动画 + will-change 适度使用 */
.card {
  transition: transform 0.3s ease, opacity 0.3s ease;
}
.card:hover {
  transform: translate3d(0, -4px, 0); /* 3d transform 提升合成层，动画不掉帧 */
  opacity: 0.9;
}

/* 长列表滚动容器：提示浏览器提前分层的思路，但要节制 */
.scroller {
  will-change: scroll-position;
}

/* 反例：改 width/height/margin/left 都是布局属性，动画全程重排 */
@keyframes bad-move {
  from { left: 0; }   /* 每帧重排 + 重绘 */
  to   { left: 100px; }
}
@keyframes good-move {
  from { transform: translateX(0); }  /* 每帧仅合成 */
  to   { transform: translateX(100px); }
}
```
