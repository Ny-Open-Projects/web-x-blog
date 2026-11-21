---
title: [MFW-163] SSR 应用的 Web Vitals 监控体系怎么建？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-163：SSR 应用的 Web Vitals 监控体系怎么建？
**答**：
- 指标分层：核心三指标 LCP/INP/CLS + 辅助（TTFB、FCP）；SSR 场景 TTFB 特别重要——它是服务端渲染能力的直接体检（p75/p95 按路由拆）。
- 采集：`web-vitals` 库的 `onLCP/onINP/onCLS`，`sendBeacon` 上报（页面卸载也可靠）；上报体带路由、构建版本、设备分级、采样率——没有维度的指标无法归因。
- 服务端指标同轨采集：SSR 渲染耗时（middleware 计时）、取数耗时、缓存命中率；用 traceId 把 TTFB 拆成「服务端渲染 + 网络传输」。
- 告警与回归：p75 超阈值告警（不是平均值）；发版后 Web Vitals 与上一版本自动对比，劣化即告警；Lighthouse CI 卡实验室数据，RUM 卡真实数据，双轨互补。

```ts
// app/WebVitals.tsx —— 客户端采集
'use client';
import { useReportWebVitals } from 'next/web-vitals';

export function WebVitals({ buildId }: { buildId: string }) {
  useReportWebVitals((metric) => {
    const body = JSON.stringify({
      name: metric.name,          // 'LCP' | 'INP' | 'CLS' | 'TTFB' | 'FCP'
      value: Math.round(metric.name === 'CLS' ? metric.value * 1000 : metric.value),
      id: metric.id,              // 去重
      rating: metric.rating,      // good/needs-improvement/poor
      route: window.__ROUTE__,    // 路由维度
      buildId,                    // 版本维度：发版对比的关键
      deviceClass: navigator.hardwareConcurrency <= 4 ? 'low' : 'high',
      ts: Date.now(),
    });
    // sendBeacon：unload 阶段也可靠，且不阻塞
    navigator.sendBeacon('/api/vitals', body);
  });
  return null;
}
```

```ts
// app/api/vitals/route.ts —— 服务端聚合
export async function POST(req: Request) {
  const m = await req.json();
  // 采样入库（全量打点对日志系统压力大）：poor 全采，good 采样 10%
  if (m.rating === 'poor' || Math.random() < 0.1) {
    await metrics.write(m);
  }
  return new Response(null, { status: 204 });
}
```
