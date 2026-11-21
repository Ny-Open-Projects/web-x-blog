---
title: [PER-255] 笔试题：手写 Web Vitals 四指标（LCP/INP/CLS/TTFB）统一采集器（含缓冲与一次性上报）
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-255：手写 Web Vitals 四指标（LCP/INP/CLS/TTFB）统一采集器（含缓冲与一次性上报）

**题目**：实现 `trackVitals(report)`：① LCP 取最后候选、CLS 会话窗口最大值、INP 按交互取最差、TTFB 直接从 navigation entry 读；② 四指标各自就绪后统一批量上报（全部就绪或 hidden 超时 10s 兜底）；③ 每指标只定值一次；④ observer 全部 buffered: true。

**答**：要点是各指标"定值时机"不同——TTFB 同步可得、LCP/CLS 等隐藏、INP 累计——统一出口做批量与去重。

```javascript
function trackVitals(report) {
  const vitals = {}; const done = new Set();
  const setDone = (k, v) => {
    if (done.has(k)) return; vitals[k] = v; done.add(k);
    if (done.size >= 4) flush('all-ready');
  };

  // TTFB：navigation 同步可得
  const nav = performance.getEntriesByType('navigation')[0];
  if (nav) setDone('TTFB', Math.round(nav.responseStart - nav.startTime));

  // LCP：最后候选
  new PerformanceObserver((l) => {
    const e = l.getEntries().at(-1);
    if (e) lcpLast = e.startTime;
  }).observe({ type: 'largest-contentful-paint', buffered: true });
  let lcpLast = null;

  // CLS：会话窗口最大值（简化版）
  let cls = 0;
  new PerformanceObserver((l) => {
    for (const e of l.getEntries()) if (!e.hadRecentInput) cls += e.value;
  }).observe({ type: 'layout-shift', buffered: true });

  // INP：最差交互
  let inp = 0;
  new PerformanceObserver((l) => {
    for (const e of l.getEntries()) if (e.interactionId) inp = Math.max(inp, e.duration);
  }).observe({ type: 'event', durationThreshold: 16, buffered: true });

  let flushed = false;
  const flush = (reason) => {
    if (flushed) return;
    if (lcpLast != null) { vitals.LCP = Math.round(lcpLast); done.add('LCP'); }
    vitals.CLS = +cls.toFixed(3); done.add('CLS');
    vitals.INP = Math.round(inp); done.add('INP');
    flushed = true; report({ ...vitals, reason });
  };
  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'hidden') flush('hidden');
  });
  setTimeout(() => flush('timeout'), 10000);       // 长驻页面兜底
}
```

**评分点**：
- 四指标口径各自正确（LCP 最后候选、CLS 去 hadRecentInput、INP 交互最差、TTFB 用 responseStart）。
- 批量出口 + 单次 flush 去重（flushed 标记），hidden 与超时双兜底。
- observer 全带 buffered: true（漏了会丢早期数据）。
- 简化实现中 CLS 未做会话窗口需说明取舍（或直接给出窗口逻辑）。
