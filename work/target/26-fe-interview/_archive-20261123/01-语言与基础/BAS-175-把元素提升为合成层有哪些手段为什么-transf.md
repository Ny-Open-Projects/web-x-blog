---
title: [BAS-175] 把元素提升为合成层有哪些手段？为什么 transform 动画快？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-175：把元素提升为合成层有哪些手段？为什么 transform 动画快？
**答**：
- 手段：will-change: transform、transform 非 none（如 translateZ(0) hack）、opacity < 1、filter、position: fixed 等。
- transform/opacity 动画快，是因为它们只发生在合成阶段，跳过 Layout 和 Paint，主线程卡住时也能靠合成线程维持。
- 代价是显存，所以 will-change 要"用时加、用完删"，别全局铺开。

```css
.promote { will-change: transform; }  /* 提前告知浏览器要动画，预先提升 */
.hack { transform: translateZ(0); }   /* 老式强制提升 hack，能救急也易滥用 */
/* transform 动画只走合成线程：跳过 layout 与 paint */
.animate { transition: transform .2s; }
.animate:hover { transform: translateX(10px); }
```
