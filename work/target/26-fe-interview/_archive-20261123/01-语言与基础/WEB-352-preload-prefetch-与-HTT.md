---
title: [WEB-352] preload / prefetch 与 HTTP 缓存怎么交互？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 缓存]
type: 面试题
---

## WEB-352：preload / prefetch 与 HTTP 缓存怎么交互？
**答**：
- preload 当前页关键资源（高优先级，as 必须写对）；prefetch 下一页可能资源（空闲时低优先级）。
- 预加载的资源会进入 HTTP 缓存（或 preload cache），后续同 URL 请求直接复用，双请求防重复靠 as+href 匹配。
- 坑：preload 的资源如果因 as 不匹配、CORS 模式不一致导致二次请求头不同，会"preload 了又重新下载"，Console 会有警告。

```javascript
<link rel="preload" href="/font.woff2" as="font" crossorigin>
<link rel="prefetch" href="/next-page.js">
// as=font 但 fetch 无 crossorigin → 匹配失败二次下载
const reuse = (link, req) => link.as === req.as && link.href === req.url
  && link.crossOrigin === req.mode;
console.log('as + CORS 模式一致才能复用 preload');
```
