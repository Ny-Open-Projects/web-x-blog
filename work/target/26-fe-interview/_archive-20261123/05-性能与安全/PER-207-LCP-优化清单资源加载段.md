---
title: [PER-207] LCP 优化：从 TTFB 到资源加载，各段都有哪些落地手段？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-207：LCP 优化：从 TTFB 到资源加载，各段都有哪些落地手段？

**答**：
- LCP 时间轴分四段：TTFB（服务器/网络）→ 资源加载延迟（发现资源的时间）→ 资源加载时长 → 元素渲染延迟。先用 DevTools Lighthouse 的 LCP phase 拆解定位大头，再对症下药。
- TTFB 段：CDN 边缘缓存、SSR/流式渲染（早发 HTML 骨架）、接口与 HTML 的预取（Service Worker 或 `<link rel=prefetch>`）；警惕 HTML 不缓存导致每次回源。
- 资源发现段：LCP 图片必须是 `priority` 高优——加 `fetchpriority="high"`、首屏图不懒加载、preload 关键资源；避免 LCP 元素被 JS 动态注入（延迟发现）；字体用 `font-display: swap` + preload。
- 加载与渲染段：图片用 AVIF/WebP + 合理尺寸、压缩；避免 `loading=lazy` 误用于首屏；减少 render-blocking（关键 CSS 内联、JS defer）；保证 LCP 元素不被骨架屏替换两次（LCP 只认最后一次变更）。
- 度量闭环：优化前后必须看 RUM p75 LCP，实验室数据只做回归回归参考。

```javascript
// 定位当前页面 LCP 元素与其归属段落
new PerformanceObserver((list) => {
  const entries = list.getEntries();
  const last = entries[entries.length - 1];   // LCP 候选会被更晚元素取代，取最后一个
  console.log('LCP:', last.startTime.toFixed(0), 'ms');
  console.log('元素:', last.element?.tagName, last.url || '', last.size);
  // 若 element 为空/为 div：多半是 JS 动态渲染，资源发现段耗时被拉长
  // 若 last.url 存在且 startTime 大：加载段问题，看图体积与优先级
}).observe({ type: 'largest-contentful-paint', buffered: true });
```
