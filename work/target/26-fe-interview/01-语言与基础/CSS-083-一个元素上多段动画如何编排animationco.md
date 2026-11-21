---
title: [CSS-083] 一个元素上多段动画如何编排？animation-composition 和负 delay 是什么？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-083：一个元素上多段动画如何编排？animation-composition 和负 delay 是什么？

**答**：
- 同一元素多动画用逗号分隔同时声明，各自独立控制时长与 delay。
- 两个动画都改 transform 时默认后者 replace 覆盖前者，`animation-composition: add/accumulate` 改为叠加或累加。
- 负 delay 让动画"提前开始"，是多个元素错峰入场（波浪 loading、列表渐入）的核心技巧。
- `animation-fill-mode: both` 保证 delay 期间与结束后都保持关键帧状态。

```css
/* 错峰入场：5 个元素依次延迟 -0.15s 的整数倍，刷新即波浪 */
.stagger > li {
  animation: fade-in 0.5s var(--ease-out) both;
}
.stagger > li:nth-child(1) { animation-delay: 0s; }
.stagger > li:nth-child(2) { animation-delay: -0.4s; } /* 负值：跳过前段直接从中间开始 */
.stagger > li:nth-child(3) { animation-delay: -0.25s; }

/* composition：两个动画的 transform 叠加而不是覆盖 */
.orbit {
  animation: spin 2s linear infinite, bounce 0.5s ease-in-out infinite alternate;
  animation-composition: add;
}
@keyframes spin   { to { transform: rotate(360deg); } }
@keyframes bounce { to { transform: translateY(-12px); } }
```
