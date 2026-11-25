---
title: [OPT-068] contain 和 content-visibility 深入：怎么用、坑在哪？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-068：contain 和 content-visibility 深入：怎么用、坑在哪？

**答**：
- `contain` 声明"子树变化的影响边界"，让引擎跳过范围外的布局/绘制计算；`content-visibility: auto` 更进一步——视口外的子树**连渲染树都跳过**，长列表/长页面收益可达渲染时间减半。
- `contain: layout` 隔离布局、`paint` 隔离绘制溢出、`strict` 等价 `layout paint` 组合，适合独立卡片/列表项。
- content-visibility 必须配 `contain-intrinsic-size`，否则滚动条先按 0 高度算，滚动到底会疯狂跳动（CLS 恶化）。
- 坑：`contain: paint` 会裁剪溢出内容，遮挡 sticky/下拉阴影；`content-visibility` 内的锚点定位与 Ctrl+F 查找行为有差异，重要内容慎用。

```css
/* 一一对应：contain 与 content-visibility 落地 */
/* 场景 1：商品列表项——独立卡片用 strict，滚动/布局影响被限制在单项内 */
.card {
  contain: layout paint style;   /* 等价 strict 去掉 size */
}

/* 场景 2：超长页面（评论流/文档）——视口外整块跳过渲染 */
.comment-item {
  content-visibility: auto;
  /* 必须给预估高度：让滚动条稳定，跳过渲染期间占位 */
  contain-intrinsic-size: auto 120px; /* auto：真实渲染后记忆实际尺寸，越用越准 */
}

/* 场景 3：首屏关键区不要套 content-visibility，反而多一层判断 */
.hero { contain: layout; } /* 只隔离，不跳过 */

/* 验证与避坑 */
/* 1. 对比收益：DevTools Rendering 面板开 Frame Rendering Stats，
      或录制滚动 Performance，看 Recalculate Style 耗时下降比例 */
/* 2. 避坑：paint 会裁溢出，阴影被切的卡片要改成外层建层或去掉 contain: paint */
.card-shadow { contain: layout; } /* 想要 box-shadow 溢出可见就别加 paint */
/* 3. 锚点跳转目标在视口外时，先手动触发渲染：
      document.getElementById(hash)?.scrollIntoView(); */
```
