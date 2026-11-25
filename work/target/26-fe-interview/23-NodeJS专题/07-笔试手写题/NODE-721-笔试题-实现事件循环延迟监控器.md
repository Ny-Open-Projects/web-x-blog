---
title: [NODE-721] 笔试题——实现事件循环延迟监控器（分位统计 + 告警）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-721：手写事件循环延迟监控

**需求与边界**：
- 需求：事件循环延迟（ELD）监控——① monitorEventLoopDelay 采样 + 周期 reset；② 分位统计（P50/P99——每 10s 窗口）；③ 阈值告警（P99 > 100ms 持续 3 个窗口——SCN-OPS-276 去抖）；④ 与请求关联（告警时快照活跃 handle/最近慢请求）。
- 边界：① resolution 精度权衡（10ms——过细内存开销）；② enable 后 reset 语义（每个窗口独立）；③ 首个窗口无数据容忍。

**答**：
```javascript
import { monitorEventLoopDelay } from 'perf_hooks';
function eldMonitor({ windowMs = 10_000, thresholdMs = 100, deBounce = 3 } = {}) {
  const obs = monitorEventLoopDelay({ resolution: 10 });
  obs.enable();
  let breaches = 0;
  const timer = setInterval(() => {
    const p50 = obs.percentile(50) / 1e6, p99 = obs.percentile(99) / 1e6;   // ns→ms
    telemetry.push({ eldP50: p50, eldP99: p99, count: obs.count });   // 遥测
    breaches = p99 > thresholdMs ? breaches + 1 : 0;               // 去抖计数
    if (breaches >= deBounce) {
      alert({ type: 'ELD_HIGH', p99, snapshot: {                                     // 快照归因
        handles: process._getActiveHandles().length,
        requests: ringBuffer.last(10), heap: process.memoryUsage().heapUsed } });
      breaches = 0;                                    // 告警后重置（不连续轰炸）
    }
    obs.reset();                                       // 窗口独立
  }, windowMs);
  return { stop: () => { obs.disable(); clearInterval(timer); } };
}
```

**评分点**:
- monitorEventLoopDelay + 周期 reset（窗口独立——SCN-NODE-671 心电图）。
- 分位统计 + ns→ms 转换。
- 持续 3 窗口去抖（SCN-OPS-276 熔断疲劳防御）。
- 告警带归因快照（handle/请求/内存——定位方向）。
