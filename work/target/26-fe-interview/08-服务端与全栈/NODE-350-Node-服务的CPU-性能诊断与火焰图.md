---
title: [NODE-350] Node 服务的 CPU 性能诊断与火焰图如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-350：Node 服务的 CPU 性能诊断与火焰图
**答**:
- 发现：CPU 使用率与 QPS 不成比例、P95 延迟涨、事件循环延迟（perf_hooks monitorEventLoopDelay P99 > 50ms）→ 有同步热点。
- 采集：--cpu-prof 启动（开发）、运行时 inspector Profiler.start/Stop（生产低风险短采样）、0x / clinic flame 一键火焰图。
- 火焰图解读：宽块 = 时间占比大；自顶向下找"平台块"（同步阻塞）；关注 JSON.parse/stringify 大对象、正则回溯（灾难性回溯是经典事故）、同步加密（bcrypt 同步版）、序列化循环。
- 修复模式：同步改异步/分片（大循环 yield）、正则优化（避免嵌套量词）、预计算与缓存、下沉 worker_threads（NODE-348）、大对象序列化换流式（NODE-011）。
- 预防：事件循环延迟指标进监控（服务健康红线）、同步重量级 API 禁用清单（lint 或 code review checklist）、关键路径压测 CPU 预算。
```javascript
const { monitorEventLoopDelay, PerformanceObserver } = require('perf_hooks');
const h = monitorEventLoopDelay({ resolution: 10 });
h.enable();
setInterval(() => {
  const p99 = h.percentile(99) / 1e6;                            // ms
  if (p99 > 50) { metrics.gauge('el.p99', p99); captureCpuProfile(); }  // 采样定位
  h.reset();
}, 5000);
```
