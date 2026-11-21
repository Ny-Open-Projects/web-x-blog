---
title: [CSS-164] Tooltip 的小箭头用边框法还是 clip-path 法？如何对比？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-164：Tooltip 的小箭头用边框法还是 clip-path 法？如何对比？

**答**：
- 边框法（经典）：transparent 边框拼三角形，兼容到上古浏览器；缺点是只能做实心三角，带边框/阴影的气泡要两个三角叠放模拟。
- clip-path 法（现代）：`clip-path: polygon(...)` 直接裁剪一个带边框气泡的伪元素，或裁剪投影层，箭头可带边框与阴影。
- 更彻底的做法：伪元素正方形 rotate 45° 一半露出气泡外，配同色边框，天然带边框阴影。
- 选型：内部系统/新项目 clip-path 或 rotate 法；需要兼容老内核的库组件用边框法。

```css
/* 方案一：边框法，兼容性最强 */
.tip-border {
  position: relative;
  background: #333;
  color: #fff;
  padding: 6px 10px;
  border-radius: 4px;
}
.tip-border::after {
  content: "";
  position: absolute;
  bottom: -10px;
  left: 50%;
  margin-left: -5px;
  border: 5px solid transparent;
  border-top-color: #333;    /* 只留上边框形成下箭头 */
}

/* 方案二：clip-path 裁剪伪元素，箭头可带阴影 */
.tip-clip {
  position: relative;
  background: #333;
  color: #fff;
  padding: 6px 16px;
  border-radius: 4px;
  filter: drop-shadow(0 2px 4px rgba(0,0,0,.3));
}
.tip-clip::after {
  content: "";
  position: absolute;
  bottom: -8px;
  left: 50%;
  width: 16px;
  height: 8px;
  transform: translateX(-50%);
  background: #333;
  clip-path: polygon(0 0, 100% 0, 50% 100%);  /* 裁出三角 */
}
/* filter 加在带 clip-path 的整体上，箭头阴影随裁剪形状走 */
```
