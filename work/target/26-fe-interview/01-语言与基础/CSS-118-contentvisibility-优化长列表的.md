---
title: [CSS-118] content-visibility 优化长列表的原理与实测注意点？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-118：content-visibility 优化长列表的原理与实测注意点？

**答**：
- `content-visibility: auto` 让视口外子树跳过布局与绘制，接近"按需渲染"，首屏渲染时间可降数倍。
- 必须配 `contain-intrinsic-size`（如 `auto 500px`）给出占位高度，否则滚动条乱跳、锚点错位。
- `auto` 状态下浏览器保留最近渲染结果，来回滚动不闪烁；`hidden` 则完全跳过（适合折叠面板）。
- 实测注意：视口附近内容进入时仍有一次性布局成本；大量图片场景配合 lazy 加载。
- 与虚拟滚动的取舍：content-visibility 零 JS、DOM 全保留（利于搜索/无障碍），超长列表（万级）仍推荐虚拟滚动。

```css
/* 长列表项：视口外跳过渲染 */
.feed-item {
  content-visibility: auto;
  contain-intrinsic-size: auto 320px; /* 估算高度，接近真实值防跳动 */
}

/* 折叠面板：隐藏内容完全跳过渲染 */
details .panel-inner {
  content-visibility: hidden;
  contain-intrinsic-size: auto 400px;
}
details[open] .panel-inner { content-visibility: visible; }
```
