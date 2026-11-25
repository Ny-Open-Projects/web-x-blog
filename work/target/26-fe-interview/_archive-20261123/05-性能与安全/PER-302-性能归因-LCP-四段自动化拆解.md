---
title: [PER-302] LCP 的四段拆解（TTFB/发现/加载/渲染）如何自动化落地到看板？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-302：LCP 的四段拆解（TTFB/发现/加载/渲染）如何自动化落地到看板？

**答**：
- 四段定义：TTFB（HTML 首字节）、资源发现延迟（元素进入 DOM 到资源请求开始，懒加载/动态注入拉长此段）、资源加载时长（requestStart→responseEnd，体积与网络）、元素渲染延迟（资源就绪到 LCP 时间，render-blocking 与优先级拉长此段）。
- 计算来源：TTFB 取 Navigation Timing；LCP entry 的 url 对应 Resource Timing 拿加载段；"发现延迟" ≈ lcp.startTime 前该资源 requestStart 与 navigation 的时间差；渲染延迟 ≈ LCP 时间 - 资源 responseEnd（文本 LCP 则用字体加载完成时间近似）。Chrome 官方 web-vitals 的 attribution build 就是这套逻辑，可直接用。
- 看板形态：LCP 分布 × 四段堆叠图（每段 p75），一眼看出"哪段吃掉预算"；按页面模板拆分，慢段排行直接对应修复手段（网络段→CDN、渲染段→render-blocking、发现段→懒加载误用）。
- 容错：文本 LCP 无 url；SSR 流式下渲染延迟可能为负差（资源早于 LCP 元素挂载）——按 0 截断并标注场景。

```javascript
import { onLCP } from 'web-vitals/attribution';     // 官方归因版，四段直接给
onLCP((metric) => {
  const { attribution } = metric;
  report({
    type: 'LCP-attribution',
    value: Math.round(metric.value),
    ttfb: Math.round(attribution.ttfb),
    loadDelay: Math.round(attribution.loadDelay),          // 发现延迟
    loadDuration: Math.round(attribution.loadDuration),    // 加载时长
    renderDelay: Math.round(attribution.renderDelay),      // 渲染延迟
    element: attribution.element?.tagName,
    url: attribution.url,
  });
});
// 自实现版本：lcp.url 对齐 performance.getEntriesByName(url)[0]，
// 发现段 = requestStart - (element 挂载时刻 ≈ 首个含该 url 的 DOM readyTime，近似用 responseEnd 反推)
// 看板：stacked bar(四段 p75) × 页面模板，红线 = 2500ms 预算分配（TTFB≤600/加载≤1200/渲染≤400）
```
