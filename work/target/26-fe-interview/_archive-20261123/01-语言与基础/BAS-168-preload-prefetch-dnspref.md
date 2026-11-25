---
title: [BAS-168] preload、prefetch、dns-prefetch、preconnect 有什么区别？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-168：preload、prefetch、dns-prefetch、preconnect 有什么区别？
**答**：
- dns-prefetch：只提前 DNS 解析，成本最低，适合第三方域。
- preconnect：提前完成 DNS + TCP + TLS 全套握手，适合确定要请求的关键第三方域。
- preload：当前页面马上要用的高优先级资源（字体、关键 CSS/JS），as 必须写对；prefetch：空闲时下载未来导航可能用的资源，优先级低。

```html
<link rel="dns-prefetch" href="//cdn.example.com">
<!-- 只提前 DNS 查询 -->
<link rel="preconnect" href="https://cdn.example.com" crossorigin>
<!-- DNS + TCP + TLS 全部提前 -->
<link rel="preload" as="font" href="/brand.woff2" crossorigin>
<!-- 当前页马上要用的字体，as 与 crossorigin 必须匹配否则会二次下载 -->
<link rel="prefetch" href="/checkout.js">
<!-- 空闲时预取下一页可能用的资源 -->
```
