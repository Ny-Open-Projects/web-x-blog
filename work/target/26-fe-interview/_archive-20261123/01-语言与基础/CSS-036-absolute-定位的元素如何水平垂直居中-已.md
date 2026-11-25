---
title: [CSS-036] absolute 定位的元素如何水平垂直居中（已知和未知宽高）？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-036：absolute 定位的元素如何水平垂直居中（已知和未知宽高）？

**答**：
- 已知宽高：`left/top: 50%` + 负 margin（宽高的一半），兼容性最好。
- 未知宽高：`transform: translate(-50%, -50%)`，注意 transform 会创建层叠上下文。
- 弹性法：四个方向都设 0 + `margin: auto`，元素需要有明确 width/height。
- 需要动画时推荐保留 translate 方案并把动画放在 transform 上，减少重排。

```css
.overlay { position: relative; }

/* 已知宽高 300x200 */
.known {
  position: absolute;
  left: 50%; top: 50%;
  width: 300px; height: 200px;
  margin: -100px 0 0 -150px;
}

/* 未知宽高 */
.unknown {
  position: absolute;
  left: 50%; top: 50%;
  transform: translate(-50%, -50%);
}

/* 四方向归零 + auto */
.stretch-center {
  position: absolute;
  inset: 0;
  margin: auto;
  width: max-content;   /* 需要确定尺寸 */
  height: max-content;
}
```
