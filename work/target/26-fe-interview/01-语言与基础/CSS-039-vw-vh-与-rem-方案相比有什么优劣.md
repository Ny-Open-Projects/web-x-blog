---
title: [CSS-039] vw/vh 与 rem 方案相比有什么优劣？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-039：vw/vh 与 rem 方案相比有什么优劣？

**答**：
- vw 直接绑定视口宽度，1vw = 视口宽的 1%，无 JS、无根字号，链路更简单。
- rem 可以通过限制根字号范围避免大屏元素过大，vw 需要配合 clamp/max。
- vh 在移动端受地址栏收展影响，可用 dvh（dynamic viewport height）改善。
- 工程上常混合：布局用 vw/rem，文本用 clamp 做流式排版。

```css
/* vw 版本：750 设计稿 1vw = 7.5px，换算系数 100/7.5 */
.title {
  font-size: 4.27vw; /* 32px @375 */
}

/* 用 clamp 限制极端屏幕 */
.banner-title {
  font-size: clamp(20px, 4.27vw, 40px);
}

/* 移动端 100vh 问题 */
.full-screen {
  height: 100dvh;           /* 动态视口高度，地址栏收展自适应 */
  /* 兼容回退 */
  height: 100vh;
}
```
