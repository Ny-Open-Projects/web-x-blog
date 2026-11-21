---
title: [OPT-125] 如何量化第三方脚本（统计/客服/A/B）的性能税并治理？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-125：如何量化第三方脚本（统计/客服/A/B）的性能税并治理？

**答**：
- 量化四个维度：下载体积（字节数）、主线程占用（long task 归因到 script）、阻塞时长（同步脚本 blocking 时间）、请求阻塞数（head 里的串行请求）。
- 归因手段：`PerformanceObserver` 的 longtask 没有直接 attribution，用 `PerformanceLongAnimationFrameTiming`（LoAF）可拿到 `scripts[].invoker`，精确到"哪个脚本吃了多少毫秒"。
- 治理优先级：同步改 async/defer、可延迟的按 idle 加载、纯计算类搬 Web Worker（Partytown 思路）、不用的直接下线。
- 建立"第三方准入预算"：新增脚本必须报告体积与主线程成本，超预算要走审批。

```javascript
// 一一对应：用 Long Animation Frames API 归因第三方脚本的主线程成本
const scriptCost = new Map(); // scriptURL -> {ms, count}

const loafObserver = new PerformanceObserver(list => {
  for (const entry of list.getEntries()) {
    for (const s of entry.scripts) {
      const url = s.invoker || s.sourceURL || 'inline';
      const prev = scriptCost.get(url) || { ms: 0, count: 0 };
      prev.ms += s.duration; prev.count += 1;
      scriptCost.set(url, prev);
    }
  }
});
loafObserver.observe({ type: 'long-animation-frame', buffered: true });

// 页面卸载前上报"性能税"清单
addEventListener('pagehide', () => {
  const tax = [...scriptCost.entries()]
    .map(([url, v]) => ({ url, ms: Math.round(v.ms), count: v.count }))
    .sort((a, b) => b.ms - a.ms).slice(0, 10);
  navigator.sendBeacon('/api/perf/third-party-tax', JSON.stringify({ tax }));
});

// 治理改造模板：非关键第三方统一 idle 加载
function loadIdleScript(src) {
  if (document.querySelector(`script[src="${src}"]`)) return;
  const s = document.createElement('script');
  s.src = src; s.async = true;
  (window.requestIdleCallback || setTimeout)(() => document.head.appendChild(s));
}
loadIdleScript('https://cdn.third.com/survey.js'); // 问卷类：空闲时加载
```
