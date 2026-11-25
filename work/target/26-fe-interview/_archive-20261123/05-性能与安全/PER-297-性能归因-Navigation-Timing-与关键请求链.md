---
title: [PER-297] Navigation Timing 与"关键请求链"怎么用？如何还原首屏的资源依赖瀑布？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-297：Navigation Timing 与"关键请求链"怎么用？如何还原首屏的资源依赖瀑布？

**答**：
- Navigation Timing 是"页面级 Resource Timing"：含 HTML 文档自身的 DNS/TCP/TLS/请求/响应全链路，是 TTFB 的权威来源；`domContentLoadedEventEnd`（DCL）与 `loadEventEnd`（L）分别标记 DOM 就绪与全资源就绪。
- 关键请求链（Critical Request Chain）：从 HTML 出发的"依赖瀑布"——HTML → CSS → CSS 里的字体/背景图 → JS → JS 发起的 XHR → XHR 后才渲染的内容。链深每加一层就多一个串行 RTT。DevTools Network 的 Priority 列 + Performance 面板可还原；Chrome 2024+ 的 Lighthouse 直接输出 Critical Request Chains 诊断。
- 缩短手段：链上的每一跳都是优化点——CSS 精简/内联砍掉"HTML→CSS→字体"的第三跳；模块预加载（modulepreload）砍掉"JS→动态 import"跳；数据内联到 HTML（SSR）或 preload 砍掉"JS→XHR"跳。
- RUM 落地：按 initiatorType 与 initiator 关系构建链（Resource Timing 有 initiatorType，跨资源引用要靠 URL 解析近似），输出"链长 > 4 的首屏请求链"清单进治理。

```javascript
// 估算首屏关键链长：以 LCP 资源为终点回溯
const nav = performance.getEntriesByType('navigation')[0];
const lcpRes = performance.getEntriesByType('resource').filter(r => r.initiatorType === 'img' || r.initiatorType === 'css');
console.log('HTML 自身:', {
  ttfb: Math.round(nav.responseStart - nav.startTime),
  domReady: Math.round(nav.domContentLoadedEventEnd - nav.startTime),
  load: Math.round(nav.loadEventEnd - nav.startTime),
});
// 关键链典型形态与跳数：
// HTML(1) → CSS(2) → 字体(3) → 文本渲染          ← font preload 砍第三跳
// HTML(1) → JS(2) → XHR(3) → LCP 图(4)           ← 数据预载/SSR 直出砍后两跳
// 治理目标：首屏关键链 ≤ 3 跳；每跳预算一个 RTT
```
