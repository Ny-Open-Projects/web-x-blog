---
title: [DP-327] 笔试题：手写 Web Vitals 上报（LCP/INP/CLS）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-327：笔试题：手写 Web Vitals 上报（LCP/INP/CLS）？
**题目**：实现 vitals 上报：1) LCP（PerformanceObserver largest-contentful-paint，页面隐藏时上报最终值）；2) INP（event entries 取最差交互延迟）；3) CLS 累计布局偏移（exclude 首帧）；4) 统一 beacon 上报。
**评分点**：
- LCP observer buffered: true 补早事件。
- 最终 LCP 取最后一次（隐藏时定值）。
- INP 计算正确（duration 或 interaction 延迟近似）。
- CLS 过滤 500ms 内连续偏移（会话窗口）。
```javascript
function vitals(report) {
  // LCP
  new PerformanceObserver(list => {
    const last = list.getEntries().at(-1);
    lcp = last?.startTime;
  }).observe({ type: 'largest-contentful-paint', buffered: true });   // 1)
  // INP：取所有交互中最差 duration
  let inp = 0;
  new PerformanceObserver(list => list.getEntries().forEach(e => inp = Math.max(inp, e.duration)))
    .observe({ type: 'event', buffered: true, durationThreshold: 16 });
  // CLS：会话窗口（500ms 内连续偏移合并）
  let cls = 0, session = 0, sessionTs = 0;
  new PerformanceObserver(list => list.getEntries()
    .filter(e => !e.hadRecentInput)
    .forEach(e => {
      if (e.startTime - sessionTs > 500) session = 0;      // 4)
      session += e.value; sessionTs = e.startTime;
      cls = Math.max(cls, session);
    })).observe({ type: 'layout-shift', buffered: true });
  const flush = () => report({ lcp, inp, cls });           // 2) 隐藏时定值
  addEventListener('visibilitychange', () => document.visibilityState === 'hidden' && flush(), { once: false });
  addEventListener('pagehide', flush);
}
```
