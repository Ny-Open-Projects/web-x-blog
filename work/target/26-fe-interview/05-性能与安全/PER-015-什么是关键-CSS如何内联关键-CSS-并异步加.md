---
title: [PER-015] 什么是关键 CSS？如何内联关键 CSS 并异步加载剩余样式？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-015：什么是关键 CSS？如何内联关键 CSS 并异步加载剩余样式？

**答**：
- 关键 CSS：渲染首屏内容所必需的样式。外链 CSS 是渲染阻塞资源，浏览器要下载解析完才能绘制。
- 做法：构建期用 critters/penthouse 抽取首屏样式**内联**到 `<head>`，剩余 CSS 用 `media="print"` 技巧或 preload + onload 异步加载。
- 记得加 `noscript` 兜底，保证 JS 禁用时样式仍可加载。
- 判断标准：内联体积控制在 14KB 左右（一个 RTT 可传完），过大反而拖慢 HTML 传输。

```html
<head>
  <!-- 关键 CSS：首屏必需样式直接内联，避免渲染阻塞的外链请求往返 -->
  <style>
    .header { display: flex; height: 56px; }
    .hero { padding: 40px 16px; font-size: 24px; }
  </style>
  <!-- 其余 CSS 异步加载：先按 print 低优先级拉取，加载完切回 all 应用 -->
  <link rel="stylesheet" href="/styles/main.css" media="print" onload="this.media='all'">
  <!-- JS 被禁用时兜底 -->
  <noscript><link rel="stylesheet" href="/styles/main.css"></noscript>
</head>
```
