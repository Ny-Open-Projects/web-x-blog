---
title: [ALG-181] 监控 SDK 要在 Chrome 上采样 JS 堆内存趋势，但 GC 锯齿波动大，直接报警全是误报。如何做平滑与趋势判断？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-181：监控 SDK 要在 Chrome 上采样 JS 堆内存趋势，但 GC 锯齿波动大，直接报警全是误报。如何做平滑与趋势判断？
**答**：定时采样 `performance.memory`（Chrome 专属，非标准），每样本记 usedJSHeapSize；用指数移动平均（EMA：`smooth = α × 当前 + (1-α) × 上次`）滤掉 GC 锯齿；再在平滑序列上做趋势判断——连续 N 个样本单调上升或超过堆上限的阈值比例才告警，区分"GC 波动"与"真泄漏"（泄漏特征：每次 GC 后谷值持续抬高）。

```javascript
function trackMemory(intervalMs = 10000) {
  const samples = [];
  const timer = setInterval(() => {
    const m = performance.memory;      // Chrome 专属，非标准 API
    if (!m) { clearInterval(timer); return; }
    samples.push({ t: Date.now(), used: m.usedJSHeapSize });
    if (samples.length > 60) samples.shift();   // 滑动窗口
    const n = samples.length;
    if (n < 2) return;
    // 指数平滑滤掉 GC 锯齿：α = 0.3
    const smooth = samples[n - 2].used * 0.7 + samples[n - 1].used * 0.3;
    samples[n - 1].smooth = smooth;
    // 趋势告警：连续 5 个平滑样本上升，或超堆上限 80%
    const rising = n >= 5 && samples.slice(-5)
      .every((s, i, a) => i === 0 || s.smooth >= a[i - 1].smooth);
    if (rising || smooth > m.jsHeapSizeLimit * 0.8) {
      reportMemoryWarning({ smooth, samples: samples.slice(-5) }); // 疑似泄漏
    }
  }, intervalMs);
  return () => clearInterval(timer);
}
```

## 二十一、综合大题

> ALG-182 ~ ALG-200：压轴综合题——公式引擎、低代码渲染、协同编辑、布局算法、diff、导出、限流、权限树、命令栈。每题都是"场景设计 + 算法内核"的双层考察。
