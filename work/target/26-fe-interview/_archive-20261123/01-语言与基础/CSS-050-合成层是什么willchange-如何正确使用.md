---
title: [CSS-050] 合成层是什么？will-change 如何正确使用？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-050：合成层是什么？will-change 如何正确使用？

**答**：
- 合成层（compositing layer）是浏览器为提升渲染效率拆分的独立图层，各有自己的纹理，合成时互不重绘。
- 促升条件：3D transform、will-change、opacity < 1 + 动画、video/canvas、fixed 元素等。
- `will-change: transform` 提前告知浏览器做优化，但层是稀缺资源：只加在少量动效元素上，动画结束移除。
- 层爆炸（layer explosion）：滥用导致显存暴涨、初始化变慢，比不掉帧更糟。

```css
/* 正确：精确声明、及时回收 */
.modal-enter {
  will-change: transform, opacity;
  transform: translateY(20px);
  opacity: 0;
}
.modal-enter.active {
  transform: translateY(0);
  opacity: 1;
}
/* JS 在 transitionend 后移除 will-change 与 modal-enter 类 */

/* 错误：全局滥用 */
* { will-change: transform; } /* 层爆炸，禁止 */
```
