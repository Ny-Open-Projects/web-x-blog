---
title: [SCN-034] 移动端 1px 边框在高清屏上显示偏粗，怎么解决？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-034：移动端 1px 边框在高清屏上显示偏粗，怎么解决？
**答**：
- 成因：CSS 的 1px 是设备独立像素，DPR=3 的屏幕会用 3 个物理像素渲染，视觉明显偏粗。
- 主流方案：伪元素画 1px 边框再 transform: scaleY(0.5) 压扁（DPR=3 可用 0.33）；也可用 border-image 或 SVG 背景。
- scaleY 只能压缩 Y 方向，需要四边都细时用整体 scale 缩放伪元素并放大尺寸补偿，或直接引入PostCSS 插件统一处理。

```css
/* 底部 1px 细线：伪元素压扁，兼容所有 DPR */
.hairline-bottom {
  position: relative;
}
.hairline-bottom::after {
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 1px;
  background: #e5e5e5;
  transform: scaleY(0.5);        /* DPR=3 屏可用 scaleY(0.33) */
  transform-origin: 0 0;
  pointer-events: none;
}
```
