---
title: [BAS-199] CSR 和 SSR 怎么一句话辨析？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-199：CSR 和 SSR 怎么一句话辨析？
**答**：
- CSR：浏览器下载 JS 后客户端渲染，首屏慢（白屏）、SEO 弱，但后续交互是 SPA 体验。
- SSR：服务端直接吐出完整 HTML，首屏快、SEO 好，代价是服务端开销和 hydration 复杂度。
- 折中方案：纯静态内容用 SSG 预渲染；Next/Nuxt 做同构渲染，两者兼得但架构复杂度上升。

```html
<!-- CSR：服务端只发一个空壳，内容靠 JS 渲染 -->
<div id="root"></div>
<script src="app.js"></script>

<!-- SSR：服务端直接返回带内容的 HTML，首屏立即可读 -->
<div id="root">
  <h1>服务端渲染好的标题</h1>
  <p>SEO 爬虫直接可读</p>
</div>
<script src="app.js"></script>
<!-- app.js 负责 hydration：接上事件与状态 -->
```
