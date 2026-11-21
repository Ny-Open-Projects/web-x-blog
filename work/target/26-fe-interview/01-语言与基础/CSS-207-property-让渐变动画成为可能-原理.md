---
title: [CSS-207] @property 让渐变动画成为可能的原理
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 动画]
type: 面试题
---

## CSS-207：@property 让渐变动画成为可能的原理

**答**：
- 渐变函数的参数（角度/色标位置）以前是字符串的一部分，浏览器整体计算——无法逐帧插值
- @property 注册后，`--angle` 成为「数值类型」，动画引擎逐帧对数值插值，再代入 conic-gradient 重新渲染
- 本质：把「字符串动画」变成「数值动画」，插值发生在属性层而非函数层
- 性能注意：渐变重绘在 paint 阶段，不能合成层加速——大范围动画会掉帧，适合小元素（按钮、进度环）
- 同理可动画：--percent 数字（配合 counter）、--x 长度位移

```css
@property --p { syntax: '<number>'; initial-value: 0; inherits: false; }
.progress::after {
  counter-reset: p var(--p);
  content: counter(p) '%';
  animation: fill 1s ease forwards;
}
@keyframes fill { to { --p: 78; } } /* 数字从 0 滚到 78，纯 CSS 计数器 */
```
