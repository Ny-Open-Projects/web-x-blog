---
title: [CSS-271] mask 遮罩的语法与滑动揭晓效果
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 效果]
type: 面试题
---

## CSS-271：mask 遮罩的语法与滑动揭晓效果

**答**：
- mask：用图像/渐变的 alpha 通道决定元素的可见度——白色（不透明）显示、透明隐藏
- 语法现代化：`mask-image / mask-size / mask-position / mask-repeat` 简写 `mask`；渐变做 mask 最常用
- 经典效果：滑动揭晓（linear-gradient mask + background-position 动画）、边缘淡出（照片底部渐隐）、文字镂空
- 与 clip-path 分工：clip-path 是「几何形状裁剪」（硬边界），mask 是「透明度渐变」（软边界）——羽化效果只能 mask
- 兼容：需 -webkit-mask 前缀（Safari），Chrome 120+ 无前缀

```css
.fade-bottom {
  -webkit-mask-image: linear-gradient(black 60%, transparent);
  mask-image: linear-gradient(black 60%, transparent);
}
.reveal {
  -webkit-mask-image: linear-gradient(to right, black 40%, transparent 60%);
  mask-image: linear-gradient(to right, black 40%, transparent 60%);
  -webkit-mask-size: 250%; mask-size: 250%;
  -webkit-mask-position: 100% 0; mask-position: 100% 0;
  animation: sweep 1.2s ease forwards;
}
@keyframes sweep { to { -webkit-mask-position: 0 0; mask-position: 0 0; } }
```
