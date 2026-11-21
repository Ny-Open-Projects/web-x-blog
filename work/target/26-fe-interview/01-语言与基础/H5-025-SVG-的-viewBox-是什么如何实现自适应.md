---
title: [H5-025] SVG 的 viewBox 是什么？如何实现自适应缩放？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-025：SVG 的 viewBox 是什么？如何实现自适应缩放？
**答**：
- viewBox 定义 SVG 内部逻辑坐标系（如 `0 0 100 100`），width/height 决定显示尺寸，两者自动缩放映射。
- 内容按逻辑坐标书写，改 width/height 即整体等比缩放，天然矢量清晰。
- `preserveAspectRatio` 控制宽高比不一致时的适配策略（默认 `xMidYMid meet`）。
- 与 canvas 不同：SVG 元素是真实 DOM，可以被 CSS/JS 选择、加事件，改属性即可更新。

```html
<!-- viewBox 100x100 的内容，无论显示尺寸多大都清晰且等比缩放 -->
<svg viewBox="0 0 100 100" width="200" height="200" role="img" aria-label="蓝色圆形">
  <circle cx="50" cy="50" r="40" fill="#3367d6" />
  <rect x="10" y="10" width="20" height="20" fill="#ff3b30" />
</svg>

<!-- 同一份内容，显示 64px 一样清晰 -->
<svg viewBox="0 0 100 100" width="64" height="64">
  <circle cx="50" cy="50" r="40" fill="#3367d6" />
</svg>

<!-- preserveAspectRatio=none 时强行拉伸填满，会变形 -->
<svg viewBox="0 0 100 100" width="200" height="80" preserveAspectRatio="none">
  <circle cx="50" cy="50" r="40" fill="#34c759" />
</svg>
```
