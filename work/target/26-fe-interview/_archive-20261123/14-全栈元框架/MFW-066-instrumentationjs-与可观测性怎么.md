---
title: [MFW-066] Next.js 的 instrumentation 是什么，SSR 应用怎么做可观测性？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-066：Next.js 的 instrumentation 是什么，SSR 应用怎么做可观测性？
**答**：
- `instrumentation.ts` 是 Next 提供的服务端生命周期钩子，`register()` 在 server 启动时执行一次（每个进程），用来初始化 OpenTelemetry、APM SDK、全局错误兜底——相当于 SSR 应用的 main 入口。
- SSR 可观测性三层：服务端（RSC 渲染耗时、action 耗时、DB 查询）、网络（TTFB）、客户端（web-vitals 上报）。trace 要把 requestId 从浏览器 → middleware → RSC → DB 串起来。
- 采样策略：全量 trace 成本高，按路由采样 + 错误全量；慢查询（p99 > 阈值）自动升级采样。
- 上报要异步不阻塞响应（`waitUntil` / 后台队列），失败静默，不能让监控拖垮业务。

```ts
// instrumentation.ts（项目根）
export async function register() {
  // 只在 Node runtime 初始化，Edge 沙箱里跳过重 SDK
  if (process.env.NEXT_RUNTIME === 'nodejs') {
    const { initOTel } = await import('./otel-server');
    initOTel({
      serviceName: 'shop-web',
      sampler: { sampleRate: Number(process.env.TRACE_SAMPLE ?? 0.1) },
    });
    process.on('unhandledRejection', (err) => {
      // 兜底上报，进程不退出
      reportError(err, { source: 'unhandledRejection' });
    });
  }
}
```

```ts
// 客户端 web-vitals 上报
'use client';
import { useReportWebVitals } from 'next/web-vitals';

export function WebVitals() {
  useReportWebVitals((m) => {
    navigator.sendBeacon('/api/vitals', JSON.stringify({
      name: m.name,           // LCP / INP / CLS / FCP / TTFB
      value: m.value,
      route: location.pathname,
      ts: Date.now(),
    }));
  });
  return null;
}
```
