---
title: [NODE-671] Node 服务的性能剖析（clinic/heapdump）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-671：性能剖析怎么做？
**答**：
- 工具矩阵：clinic doctor（整体健康诊断——事件循环延迟/GC/外部资源）、clinic flame（CPU 热点火焰图）、heapdump（堆快照——内存泄漏，SCN-BLD-327 同构）、0x（火焰图轻量版）。
- 诊断路径：延迟问题 → clinic doctor 看事件循环延迟占比 → CPU 型（火焰图找热点函数）/IO 型（下游耗时）/GC 型（GC 停顿对齐）——三型分类先于细节。
- 生产剖析约束：剖析有开销（CPU 采样/heap 快照 STW）——低流量时段/单实例摘流剖析（readiness 摘流——SCN-NODE-664 探针联动），禁止全实例同时剖析。
- 持续观测：常驻轻量指标（事件循环延迟百分位/活跃 handle 数/GC 频率——perf_hooks.monitorEventLoopDelay）替代重型剖析。
- 追问钩子：为什么「事件循环延迟」是 Node 性能诊断的第一指标——所有慢的最终表现都是事件循环被阻塞（CPU 密集/同步 IO/GC）；monitorEventLoopDelay 的 P99 延迟直接量化「阻塞严重度」，其分布形态（毛刺 vs 持续高）区分故障类型——它是 Node 服务的心电图。

```javascript
import { monitorEventLoopDelay, performance } from 'perf_hooks';
const obs = monitorEventLoopDelay({ resolution: 10 });
obs.enable();
setInterval(() => {
  telemetry.push({ eldP99: obs.percentile(99) / 1e6,   // ms
    handles: process._getActiveHandles?.().length });
  obs.reset();
}, 10_000);
// 生产剖析：单实例摘流
kubectl exec pod -- kill -USR2 1                     // heapdump 信号（仅摘流实例）
```
