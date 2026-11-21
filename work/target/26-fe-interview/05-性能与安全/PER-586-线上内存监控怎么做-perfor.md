---
title: [PER-586] 线上内存监控怎么做？performance.memory 有局限，怎么建立可信的线上内存信号？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-586：线上内存监控怎么做？performance.memory 有局限，怎么建立可信的线上内存信号？

**答**：
- `performance.memory`（Chromium only）的三个局限：仅 Chrome/Edge、精度受隐私策略限制（部分版本返回上限值）、`usedJSHeapSize` 波动受 GC 时机影响，单点读数没意义。
- 可信信号靠**趋势而非单点**：页面存活期间周期采样（每 10 秒），看"GC 后基线是否阶梯上升"——连续多个采样点抬升不回落才是泄漏信号；单点高低无所谓。
- 兜底指标：iOS 没有 memory API，用代理信号——`performance.now()` 的时间膨胀（GC 压力导致变慢）、页面被系统杀死的频率（会话存活时长 p10）、慢交互率与内存的相关性。
- 告警设计：内存泄漏告警看长会话样本的斜率"（每小时增长 MB 数），而不是绝对值；样本要过滤短会话（< 1 分钟的没参考价值）。

```javascript

function memMonitor({ intervalMs = 10000, minSessionMs = 60000 } = {}) {
  const samples = [];
  const start = Date.now();
  const timer = setInterval(() => {
    const m = performance.memory;
    if (m) samples.push({ t: Date.now() - start, heap: m.usedJSHeapSize / 1048576 });
  }, intervalMs);
  addEventListener('pagehide', () => {
    clearInterval(timer);
    if (Date.now() - start < minSessionMs) return;        // 短会话无参考价值
    // GC 后基线斜率：取每分钟最小值（近似 GC 后基线）做线性回归
    const byMin = {};
    samples.forEach(s => { const k = Math.floor(s.t / 60000);
      byMin[k] = Math.min(byMin[k] ?? Infinity, s.heap); });
    const pts = Object.entries(byMin).map(([k, v]) => [+k, v]);
    if (pts.length < 5) return;
    const slope = (pts.at(-1)[1] - pts[0][1]) / (pts.at(-1)[0] - pts[0][0]); // MB/min
    navigator.sendBeacon('/collect/mem', JSON.stringify({ slope: +slope.toFixed(2), pts }));
  });
}
// 告警阈值：长会话斜率 > 2MB/min 且持续 5 分钟 -> 泄漏嫌疑样本入库
```
