---
title: [PER-009] preload 与 prefetch 有什么区别？dns-prefetch 和 preconnect 又各自解决什么问题？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-009：preload 与 prefetch 有什么区别？dns-prefetch 和 preconnect 又各自解决什么问题？

**答**：
- `dns-prefetch`：只提前解析 DNS，成本最低，适合第三方域名。
- `preconnect`：提前完成 DNS + TCP + TLS 三步握手，适合确定要请求的关键第三方源（API、字体 CDN）。
- `preload`：以高优先级**提前加载当前页面马上要用**的资源（首屏字体、关键图片），必须写对 `as`。
- `prefetch`：浏览器**空闲时**拉取下一跳可能用到的资源，优先级低，用于加速后续导航。
- 滥用 preload 会与首屏关键资源抢带宽，反而劣化 LCP。

```html
<!-- dns-prefetch：提前解析第三方域名 DNS，成本最低 -->
<link rel="dns-prefetch" href="https://cdn.example.com">

<!-- preconnect：提前完成 DNS + TCP + TLS，适合关键第三方源 -->
<link rel="preconnect" href="https://api.example.com" crossorigin>

<!-- preload：当前页面马上要用的高优先级资源，如首屏字体 -->
<link rel="preload" href="/fonts/inter.woff2" as="font" type="font/woff2" crossorigin>

<!-- prefetch：浏览器空闲时拉取下一跳页面可能用到的资源 -->
<link rel="prefetch" href="/next-page-chunk.js">

<!-- modulepreload：提前加载并解析 ESM 模块及其依赖 -->
<link rel="modulepreload" href="/src/app-entry.js">
```
