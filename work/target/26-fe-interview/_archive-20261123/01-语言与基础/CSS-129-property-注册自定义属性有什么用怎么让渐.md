---
title: [CSS-129] @property 注册自定义属性有什么用？怎么让渐变动起来？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-129：@property 注册自定义属性有什么用？怎么让渐变动起来？

**答**：
- 未注册的自定义属性是"无类型字符串"，浏览器无法插值，transition/animation 直接跳变。
- `@property --x { syntax: "<angle>"; ... }` 注册类型后，变量获得类型、初始值与继承语义，可参与过渡与动画。
- 经典应用：渐变角度动画、数字滚动（<integer>）、圆环进度（<percentage>）。
- `inherits: false` 控制是否继承；`initial-value` 在 syntax 非通配时必填。
- Baseline 2024，用 `@supports` 或 CSS.registerProperty 降级处理老内核。

```css
/* 注册角度变量：字符串变成可插值的 <angle> */
@property --angle {
  syntax: "<angle>";
  initial-value: 0deg;
  inherits: false;
}

/* 渐变旋转动画：注册前这里只能瞬移，注册后平滑旋转 */
.conic-spin {
  background: conic-gradient(from var(--angle), var(--c1), var(--c2), var(--c1));
  animation: rotate-hue 3s linear infinite;
}
@keyframes rotate-hue { to { --angle: 360deg; } }

/* 数字滚动：注册 <integer> 后 counter 展示可过渡 */
@property --num {
  syntax: "<integer>";
  initial-value: 0;
  inherits: false;
}
.counter {
  transition: --num 1s;
  counter-reset: num var(--num);
}
.counter::after { content: counter(num); }
.counter.is-final { --num: 1024; }
```
