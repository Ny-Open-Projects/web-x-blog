---
title: [CSS-093] background 多层叠加有哪些工程技巧？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-093：background 多层叠加有哪些工程技巧？

**答**：
- 多背景用逗号分隔，先声明的层绘制在最上方，position/size 逐层对应。
- 纯 CSS 网格线：两条 linear-gradient 1px 线 + background-size 重复。
- 角标：radial/linear 渐变放在四角 position 上，省掉四个伪元素。
- 半透明遮罩：`linear-gradient(rgb(0 0 0 / .5), ...)` 叠在图上，替代额外遮罩元素。

```css
/* 1. 纯 CSS 表格线网格 */
.grid-bg {
  background-image:
    linear-gradient(var(--border-color) 1px, transparent 1px),
    linear-gradient(90deg, var(--border-color) 1px, transparent 1px);
  background-size: 40px 40px;
}

/* 2. 四角圆点角标：一个元素完成 */
.corners {
  background-image: radial-gradient(circle, var(--brand) 3px, transparent 3px);
  background-repeat: no-repeat;
  background-position: top left, top right, bottom left, bottom right;
  background-size: 8px 8px;
}

/* 3. 图上遮罩 + 底部渐变压暗，保证白字可读 */
.hero {
  background-image:
    linear-gradient(transparent 40%, rgb(0 0 0 / 0.6)),
    url("/images/hero.avif");
  background-size: cover;
  background-position: center;
}
```
