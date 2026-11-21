---
title: [OPT-050] fetchpriority 属性怎么用？优先级提示比 preload 强在哪？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-050：fetchpriority 属性怎么用？优先级提示比 preload 强在哪？

**答**：
- 浏览器对资源默认优先级有猜测，`fetchpriority` 直接显式干预：`high`/`low`/`auto`，是唯一能**降级**资源优先级的手段（preload 只能升）。
- 高频场景一：LCP 主图 `fetchpriority="high"`，配合懒加载图 `loading="lazy"`（隐式低优先级），把带宽让给首屏。
- 高频场景二：`async` 脚本默认 high，埋点/客服类脚本加 `fetchpriority="low"`，避免抢关键路径带宽。
- fetchpriority 不改变发现时机（还是要写进 HTML），preload 不改变优先级（还是默认），两者可组合：`<link rel="preload" as="image" fetchpriority="high">` 抢救动态插入的 LCP 图。

```html
<!-- 一一对应：fetchpriority 资源优先级编排 -->
<head>
  <!-- LCP 主图：显式高优先级，最先抢带宽 -->
  <img src="hero.avif" fetchpriority="high" decoding="async" width="1200" height="630" />

  <!-- async 脚本默认就是 high，必须手动压低，否则与首屏 JS 抢带宽 -->
  <script async src="https://analytics.example.com/collect.js" fetchpriority="low"></script>
  <script async src="https://static.example.com/chat-widget.js" fetchpriority="low"></script>

  <!-- 动态拼装的 LCP 图（首屏靠接口渲染）：提前声明且给高优先级 -->
  <link rel="preload" as="image" href="/api/cover.avif" fetchpriority="high" />

  <!-- 下一页资源：提前拉但要绝对让路，与 prefetch 组合 -->
  <link rel="prefetch" href="/next-page-data.json" fetchpriority="low" />
</head>
```
