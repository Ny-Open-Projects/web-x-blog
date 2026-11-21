---
title: [PER-211] TTFB 对 LCP 有多大影响？流式渲染（Streaming SSR）如何压低 TTFB？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-211：TTFB 对 LCP 有多大影响？流式渲染（Streaming SSR）如何压低 TTFB？

**答**：
- TTFB 是 LCP 时间轴的第一段，是硬地板：TTFB 500ms 的页面 LCP 不可能低于 500ms。CDN 边缘缓存与 HTML 短缓存（stale-while-revalidate）是第一杠杆。
- 传统 SSR 的问题：必须等所有数据接口返回才能吐完整 HTML，最慢的接口决定 TTFB。流式渲染（React 18 `renderToPipeableStream` / Suspense）把页面切成骨架 + 多个可延迟块，HTML 分块下发，先到的部分立刻可解析、可预加载资源。
- 收益本质：把"串行等待最慢数据"变成"并行发送已就绪部分 + 局部 fallback"，TTFB 取决于最慢块的首字节而非全部数据；配合 `<Suspense fallback>` 避免整页白屏。
- 注意成本：流式下 LCP 元素可能从骨架变成后到的真实内容（LCP 变大或被替换两次）；fallback 尺寸要贴近真实内容防 CLS；SEO 上后注水内容对爬虫友好（React 19 起流式注水标记完整）。

```javascript
// React 18 流式 SSR：先吐导航/首屏，评论区等慢接口用 Suspense 挂起
import { renderToPipeableStream } from 'react-dom/server';
app.get('/', (req, res) => {
  const { pipe } = renderToPipeableStream(<App />, {
    bootstrapScripts: ['/main.js'],
    onShellReady() {
      res.setHeader('Content-Type', 'text/html; charset=utf-8');
      pipe(res);           // 骨架立刻下发，TTFB 不再被慢接口拖住
    },
  });
});
// <Suspense fallback={<CommentSkeleton />}><SlowComments /></Suspense>
// 数据就绪后浏览器收到续块，自动替换 fallback —— 首帧提前，LCP 提前
```
