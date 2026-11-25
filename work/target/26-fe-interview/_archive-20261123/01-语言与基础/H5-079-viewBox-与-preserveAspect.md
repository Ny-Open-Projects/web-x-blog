---
title: [H5-079] viewBox 与 preserveAspectRatio 的组合语义是什么？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-079：viewBox 与 preserveAspectRatio 的组合语义是什么？
**答**：
- `viewBox="min-x min-y w h"` 定义 SVG 内部坐标系；绘制坐标全在这个系统里，与元素显示尺寸（CSS）解耦。
- `preserveAspectRatio="xMidYMid meet"`（默认）决定"坐标系如何装进视口"：`meet` 等比缩放完整显示（留边），`slice` 等比缩放铺满（裁边）。
- 前缀 `xMin/xMid/xMax` 与 `YMin/YMid/YMax` 九种组合控制对齐方向；`none` 表示不保比例、拉伸填满。
- 高频坑：默认行为下 SVG 上下或左右会有"留白"，导致"图标没占满容器"——需要铺满时用 `slice` 或 `none`。
- `slice` + 对齐组合是实现"SVG 版 object-fit: cover"的标准做法，用于插画封面、装饰背景。

```html
<style>
  .box { width: 200px; height: 200px; border: 1px solid #999; }
</style>

<!-- meet（默认）：等比缩小，完整显示，左右留白 -->
<svg class="box" viewBox="0 0 400 200" preserveAspectRatio="xMidYMid meet">
  <rect width="400" height="200" fill="#6cf"/>
  <text x="200" y="110" text-anchor="middle" font-size="24">400x200 内容</text>
</svg>

<!-- slice：等比放大铺满，上下被裁掉，等价 object-fit cover -->
<svg class="box" viewBox="0 0 400 200" preserveAspectRatio="xMidYMid slice">
  <rect width="400" height="200" fill="#fc6"/>
  <circle cx="200" cy="100" r="90" fill="coral"/>
</svg>

<!-- none：拉伸变形填满，两个尺寸都不保比例 -->
<svg class="box" viewBox="0 0 400 200" preserveAspectRatio="none">
  <rect width="400" height="200" fill="#9c6"/>
</svg>

<!-- 左下角对齐 + slice：裁切方向可控 -->
<svg class="box" viewBox="0 0 400 200" preserveAspectRatio="xMinYMax slice">
  <rect width="400" height="200" fill="#c6f"/>
  <rect x="0" y="150" width="400" height="50" fill="purple"/>
</svg>
```
