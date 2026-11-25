---
title: [R19-250] Suspense fallback 对 SEO 与内容可见性的影响？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-250：Suspense fallback 对 SEO 的影响？
**答**：
- SSR 流式：fallback 先进 HTML、真实内容流式补充——爬虫拿到的是完整内容（现代爬虫等待流结束），风险低。
- CSR Suspense：首屏只有 fallback，内容靠 JS 渲染——SEO 弱，核心页面必须 SSR/SSG。
- 爬虫兼容：Googlebot 支持 JS 渲染但配额有限，fallback 阶段过长会收录 fallback 内容；TTFB 内尽快 resolve。
- 实践：关键内容（标题/正文）不走异步边界或使用服务端渲染；异步边界留给次要模块；流式 SSR + 合理超时。
- 监控：以「爬虫视角」定期抽查（curl 看首屏 HTML 内容完整性）。
