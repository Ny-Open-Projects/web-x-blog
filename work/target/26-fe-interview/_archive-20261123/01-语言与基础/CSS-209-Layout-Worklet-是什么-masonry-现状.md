---
title: [CSS-209] Layout Worklet 是什么，masonry 现状如何
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, Houdini]
type: 面试题
---

## CSS-209：Layout Worklet 是什么，masonry 现状如何

**答**：
- Layout Worklet：用 JS 定义自己的布局算法，CSS 里 `display: layout(custom-name)` 引用——CSS Grid 之后布局自由度的终极方案
- 接口：实现 `intrinsicSizes` 与 `layout` 方法，决定子元素的位置与尺寸，可异步（分片布局，长列表友好）
- masonry 现状：原生 `grid-template-rows: masonry`（瀑布流进 Grid 规范）在 Firefox 实验实现中，Chromium/Safari 未见落地；社区方案仍是 CSS columns / JS 布局
- 现状结论：Layout Worklet 只有 Chromium 实现且不活跃——了解概念即可，别在面试中吹生产可用
- 可以给的替代答案：瀑布流用 `columns` 或 JS（如 Masonry 库）是当前正解

```css
/* 概念演示，兼容性差 */
.gallery { display: layout(masonry-layout); }
```
```javascript
registerLayout('masonry-layout', class {
  async layout(children, edges, constraintSpace, styleMap) {
    // 自定义放置算法……
  }
});
```
