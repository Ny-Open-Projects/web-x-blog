---
title: [WEB-051] CSS 和 JS 分别如何阻塞渲染？defer 和 async 怎么选？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-051：CSS 和 JS 分别如何阻塞渲染？defer 和 async 怎么选？
**答**：
- CSS 不阻塞 DOM 解析但阻塞渲染（渲染树要等 CSSOM），还会阻塞其后 JS 的执行（JS 可能读样式）。
- 默认 `<script>` 下载和执行都阻塞 HTML 解析；`async` 下载不阻塞、下载完立即执行（顺序不保证，适合独立脚本如埋点）；`defer` 下载不阻塞、DOM 解析完后按序执行（适合依赖 DOM 和彼此顺序的业务脚本）。
- 关键 CSS 内联首屏样式，其余异步加载；module script 默认行为类似 defer。

```html
<head>
  <!-- 同步 script：下载+执行都阻塞解析，放这里会拖慢首屏 -->
  <!-- <script src="/analytics.js"></script> -->

  <!-- async：下载不阻塞，下载完立即执行，执行顺序不确定，适合独立脚本 -->
  <script async src="/analytics.js"></script>

  <!-- defer：下载不阻塞，DOMContentLoaded 前按序执行，适合业务脚本 -->
  <script defer src="/vendor.js"></script>
  <script defer src="/app.js"></script>
  <!-- 保证 vendor.js 先于 app.js 执行 -->

  <!-- module 默认 defer 语义 -->
  <script type="module" src="/main.js"></script>

  <!-- 首屏关键 CSS 内联，非关键 CSS 异步加载 -->
  <style>/* 首屏关键样式 */ header{display:flex}</style>
  <link rel="preload" href="/non-critical.css" as="style" onload="this.rel='stylesheet'" />
</head>
```
