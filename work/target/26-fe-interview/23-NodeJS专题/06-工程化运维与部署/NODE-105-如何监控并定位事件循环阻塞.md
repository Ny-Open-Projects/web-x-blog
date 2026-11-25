---
title: [NODE-105] 如何监控并定位事件循环阻塞？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-105：如何监控并定位事件循环阻塞？
**答**：
- 量化：`perf_hooks.monitorEventLoopDelay` 直方图输出 P99 lag，超阈值（如 100ms）告警。
- 探针：每 100ms 的哨兵 `setImmediate` 实测漂移，漂移大时**自动抓取火焰图快照**，事后有据可查。
- 定位分流：lag 高 + CPU 高 → CPU 密集（正则回溯/大 JSON 序列化），看火焰图；lag 高 + CPU 低 → 同步调用（readFileSync/execSync）或线程池饥饿。
- 上报指标进 Prometheus（NODE-135），与 QPS/CPU 关联看，避免误判。

```javascript
const { monitorEventLoopDelay, performance } = require('perf_hooks');

// 方法一：直方图量化 lag
const lag = monitorEventLoopDelay({ resolution: 10 });
lag.enable();
setInterval(() => {
  const p99 = lag.percentile(99) / 1e6; // 纳秒转毫秒
  metrics.gauge('node_eventloop_lag_p99_ms', p99);
  if (p99 > 100) logger.error({ p99 }, 'event loop lag 超阈值');
  lag.reset();
}, 5000).unref();

// 方法二：哨兵探针，漂移大时自动采样火焰图
setInterval(() => {
  const start = performance.now();
  setImmediate(() => {
    const drift = performance.now() - start;
    if (drift > 50) captureProfilerSnapshot(); // 内部调 inspector/0x 采 5s 剖析
  });
}, 100).unref();
```
