---
title: [CSS-177] 移动端 1px 边框有哪几种实现方案？如何对比？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-177：移动端 1px 边框有哪几种实现方案？如何对比？

**答**：
- 成因：DPR > 1 时 CSS 的 1px 实际渲染为 2/3 物理像素，设计稿的“发丝线”需要更细。
- 方案一 transform scale：伪元素画 1px 再 `scaleY(0.5)`，兼容性最好，缺点是写法繁琐、圆角需要同样处理。
- 方案二直接写 `0.5px`：iOS 8+ 与现代 Chrome 支持物理像素级渲染，最简单，老 Android 可能被渲染成 0 或 1。
- 方案三背景渐变模拟：`linear-gradient` 画半像素色带，四边都行但要占 background 位。
- 选型：新项目优先 0.5px + @supports 检测，兼容场景用 scale 伪元素。

```css
/* 方案一：transform scale，兼容性最好 */
.hairline { position: relative; }
.hairline::after {
  content: "";
  position: absolute;
  left: 0; top: 0;
  width: 100%;
  height: 1px;
  background: #ddd;
  transform: scaleY(.5);
  transform-origin: 0 0;
  pointer-events: none;
}

/* 方案二：直接 0.5px，现代内核最简单 */
.modern { border-bottom: .5px solid #ddd; }

/* 方案三：渐变画半像素线，不占 border 位 */
.bg-hairline {
  background:
    linear-gradient(#ddd, #ddd) top left / 100% .5px no-repeat,
    #fff;
}

/* 方案四：viewport 缩放方案（整个页面 rem + initial-scale=0.5），
   1px 物理线全局生效，但需要整页适配方案配合，改造量大 */
```
