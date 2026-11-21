---
title: [PER-195] HTTP 新标准（Early Hints/Priority Hints/Speculation Rules）对性能有什么影响？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-195：HTTP 新标准（Early Hints/Priority Hints/Speculation Rules）对性能有什么影响？

**答**：
- **Early Hints（103）**：服务端在最终响应前提前下发关键资源提示，浏览器在 HTML 到达前就开始 preload，LCP 常见收益 100ms+；需要 CDN 配合透传。
- **Priority Hints（fetchpriority）**：显式声明资源优先级，解决浏览器启发式猜错的场景——首图 high、轮播第二屏 low，是 LCP 优化性价比最高的一招。
- **Speculation Rules**：声明式预取/预渲染，用户点击前完成文档加载；`eagerness` 四档控制激进程度。
- 落地注意：预渲染页面不得有副作用（自动播放、PV 上报），需配文档规则清理；三个标准都是渐进增强，老浏览器自然忽略。

```html
<!-- 新标准红利：Early Hints、Priority Hints、Speculation Rules -->
<!-- 1. Early Hints：nginx 在 103 响应中提前下发，浏览器在 HTML 到达前就开始加载 -->
<!-- add_header Link "</app.css>; rel=preload; as=style, </hero.avif>; rel=preload; as=image; fetchpriority=high"; -->

<link rel="preload" as="style" href="/app.css" fetchpriority="high">

<!-- 2. Priority Hints：显式声明优先级，抑制轮播图对 LCP 资源的争抢 -->
<img src="/hero.avif" fetchpriority="high" alt="首屏主图">
<img src="/banner2.avif" fetchpriority="low" alt="第二屏">

<!-- 3. Speculation Rules：声明式预取与预渲染 -->
<script type="speculationrules">
{
  "prerender": [
    { "where": { "href_matches": "/product/*" }, "eagerness": "moderate" },
    { "where": { "selector": ".nav-hot" }, "eagerness": "eager" }
  ],
  "prefetch": [
    { "where": { "href_matches": "/*" }, "eagerness": "conservative" }
  ]
}
</script>
<!-- 落地注意：预渲染页面不得有副作用（自动播放或 PV 上报），需配清理规则 -->
```
