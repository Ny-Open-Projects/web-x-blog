---
title: [R19-306] RSC 页面 TTFB 与流式的全链路优化怎么做？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-306：RSC 页面 TTFB 与流式优化全链路？
**答**：
- DNS/TLS：CDN 边缘接入、HTTP/2/3、预连接关键第三方。
- 服务端：renderToPipeableStream 立即 flush 静态壳；数据并行化（Promise.all + cache() 去重）；慢接口独立 Suspense 洞。
- 缓存：静态壳 CDN/PPR、Data Cache（tag 化）、组件级缓存。
- 客户端：关键 CSS 内联、字体预加载、payload 与 HTML 并行。
- 度量：TTFB、FCP、LCP、流式完成时间（全部洞 resolve），按 route 维度看板。
