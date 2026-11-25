---
title: [MFW-787] 流式响应的缓存交互
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-787：流式响应的缓存交互

**答**:
- 流式响应与缓存层的交互：1) **CDN 缓存流式响应**（Cloudflare Cache API/CloudFront——流式的 chunked 响应可以被 CDN 缓存（缓存完整响应后下次直发——非流式（缓存的响应是一次性发送——丢失流式特性）；2) **缓存的流式 vs 非流式**：缓存命中 = 全量返回（非流式——但速度更快）；缓存 miss = 源站流式（CDN 边缓存边转发——流式透传）；3) **缓存的条件**：流式响应的缓存要求 Content-Length 可确定或 CDN 支持流式缓存（Varnish 的 streaming cache）；4) **缓存策略的粒度**：整页缓存（Full Route Cache——Next 的 ISR 在 server 侧）vs CDN 缓存（边缘缓存——两层缓存的 TTL 对齐 RBL-581）。
- 追问钩子：为什么「CDN 缓存流式响应」会丢失流式特性？——CDN 缓存 miss 时：源站流式发送 → CDN 边缓冲边转发（客户端感知流式）；CDN 缓存完成 → 下次请求 CDN 直接发缓存体（一次性发送——非流式——chunked 边界丢失）；「缓存的序列化」：缓存存储的是完整响应体——发送时无源站流式节奏——流式变成了批量发送；用户感知差异：缓存命中的 LCP 可能更快（全量一次发）但 INP 可能更差（大量 JS 一次性解析）；「缓存的流式丢失」对用户体验的影响是微妙的（LCP 更快但交互响应可能更差）。

```typescript
// CDN 缓存流式响应的行为
// 第一次请求（缓存 miss）：
// client ← CDN ← origin（流式）
// ← chunk1(t=200ms) ← chunk1
// ← chunk2(t=400ms) ← chunk2
// ← chunk3(t=3s) ← chunk3
// CDN 同时缓存：chunk1+chunk2+chunk3 = 完整响应

// 第二次请求（缓存 hit）：
// client ← CDN（一次性发送全部）
// ← 完整响应（非流式——t=10ms 全部到达）
// LCP 更快（无流式等待）但 JS 解析突发
// 交互模式差异
const cacheMode = {
  streaming: { ttfb: 200, lcp: 1000, chunks: 5 },       // miss：流式
  cached: { ttfb: 10, lcp: 500, chunks: 1 },            // hit：全量
};
// 缓存命中的 TTFB 更快但 chunked 特性丢失
// 对 SEO 无影响（爬虫拿到完整内容——无论流式与否）
```
