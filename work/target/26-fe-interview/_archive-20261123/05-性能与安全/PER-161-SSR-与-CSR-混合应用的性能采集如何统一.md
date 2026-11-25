---
title: [PER-161] SSR 与 CSR 混合应用的性能采集如何统一？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-161：SSR 与 CSR 混合应用的性能采集如何统一？

**答**：
- 关键是**分段口径**：SSR 段（服务端渲染耗时）由服务端注入 HTML（如 `window.__SSR_MARK__`），网络段看 navigation timing，客户端段看 LCP 与 hydration 耗时，三段拼出完整首屏链路。
- hydration 是 SSR 应用的隐藏成本：`__HYDRATE_START__` 到 hydration 完成的时间单独上报，这部分用户"看得见但点不动"。
- 看板分列：SSR 页面与纯 CSR 页面的 FCP/LCP **分开统计**，直接平均会误导（SSR 天然占优）。
- 统一采集入口：无论渲染形态，上报字段结构一致（ssr/ttfb/lcp/hydration_cost），下游分析不需要感知页面类型。

```javascript
// SSR/CSR 混合采集统一：以 hydration 为分界，三段拼接完整首屏链路
// 服务端注入：<script>window.__SSR_MARK__={serverRenderMs:320};window.__HYDRATE_START__=performance.now();</script>

export function collectFirstScreen() {
  const nav = performance.getEntriesByType('navigation')[0];
  return new Promise((resolve) => {
    const obs = new PerformanceObserver((list) => {
      const e = list.getEntries().at(-1);
      if (!e) return;
      obs.disconnect();
      resolve(report('first_screen', {
        ssr: window.__SSR_MARK__,                                  // 服务端段
        ttfb: Math.round(nav.responseStart),                       // 网络段
        lcp: Math.round(e.startTime),                              // 客户端渲染段
        hydration_cost: Math.round(performance.now() - window.__HYDRATE_START__), // 可交互前隐藏成本
        pageType: document.documentElement.dataset.renderType,     // ssr 或 csr，看板分列
      }));
    });
    obs.observe({ type: 'largest-contentful-paint', buffered: true });
  });
}
```
