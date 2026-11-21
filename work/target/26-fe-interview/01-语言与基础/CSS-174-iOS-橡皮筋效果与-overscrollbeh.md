---
title: [CSS-174] iOS 橡皮筋效果与 overscroll-behavior 局部滚动怎么处理？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-174：iOS 橡皮筋效果与 overscroll-behavior 局部滚动怎么处理？

**答**：
- 橡皮筋是 iOS 全局滚动到边界后的回弹动画；整页禁用思路是 body 不滚动，滚动交给内部容器。
- `overscroll-behavior: contain`：滚动链到边界后不再传给父级/页面，阻断“弹窗内滚到底把背后列表也拖动”。
- `overscroll-behavior: none`：更彻底，边界回弹/Glow 动画也取消；`auto` 为默认联动。
- 注意 iOS Safari 对 none 的支持在较新版本才完整，老版本需 JS touchmove 阻止默认行为兜底。

```css
/* 全局禁橡皮筋：body 不滚，内部容器滚动 */
html, body { height: 100%; overflow: hidden; }
.app {
  height: 100%;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
  overscroll-behavior: contain;  /* 到边界不传导给页面 */
}

/* 弹窗内滚动区：滚到底不拖动背后内容 */
.modal-scroll {
  max-height: 60vh;
  overflow-y: auto;
  overscroll-behavior: contain;
}

/* 下拉刷新区域：彻底关闭边界效果 */
.feed {
  overscroll-behavior-y: none;
}
```
