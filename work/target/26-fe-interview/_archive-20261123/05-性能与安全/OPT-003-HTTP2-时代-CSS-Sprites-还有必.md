---
title: [OPT-003] HTTP2 时代 CSS Sprites 还有必要吗？如何取舍？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-003：HTTP2 时代 CSS Sprites 还有必要吗？如何取舍？

**答**：
- 雪碧图的核心收益是"减少 HTTP1.1 并发请求数"，HTTP2 多路复用后该收益基本消失，且雪碧图定位难维护、任一图标改动会导致整图缓存失效。
- 彩色/多态图标优先用 SVG symbol 雪碧（合并进一个 svg 文件，`<use>` 引用），可继承 currentColor、随意缩放。
- 单色图标用 iconfont 或直接内联 SVG；只有大量极小、颜色固定的装饰图才偶尔考虑位图雪碧。
- 结论：新项目默认不做 CSS Sprites，选 SVG symbol 集合。

```html
<!-- 一一对应：SVG symbol 集合替代传统 CSS Sprites -->
<svg style="display: none">
  <symbol id="icon-cart" viewBox="0 0 24 24">
    <path d="M7 18a2 2 0 1 0 0 4 2 2 0 0 0 0-4zm10 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4z" />
  </symbol>
  <symbol id="icon-user" viewBox="0 0 24 24">
    <circle cx="12" cy="8" r="4" />
  </symbol>
</svg>

<!-- 页面任意位置引用，颜色跟随 currentColor -->
<button style="color: #1677ff">
  <svg width="16" height="16"><use href="#icon-cart" /></svg>
  购物车
</button>
```
