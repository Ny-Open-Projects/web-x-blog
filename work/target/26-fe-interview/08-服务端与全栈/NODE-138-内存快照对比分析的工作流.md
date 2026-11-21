---
title: [NODE-138] 内存快照对比分析的工作流？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-138：内存快照对比分析的工作流？
**答**：
- 场景区分：内存"涨而不掉"才是泄漏（GC 后不回落）；RSS 高但 heapUsed 低可能是 Buffer/外部内存。
- **三快照法**：① 稳定流量下拍基线 → ② 复现操作 N 次（如调用可疑接口 1000 次）→ ③ 再拍 1~2 次；DevTools Comparison 视图按 Δ Size 排序。
- 分析路径：增长最大的 constructor → Retainers 引用链 → 找到"谁持有不放"：全局缓存没淘汰、监听器没 off、闭包持大对象、定时器引用上下文。
- 采集姿势：`v8.writeHeapSnapshot()` 信号触发（注意快照本身会 STW 数秒，先摘流量）；与 NODE-082 的 heapdump 排查互补。

```javascript
const v8 = require('v8');
const { setInterval: every } = require('timers');

// 信号触发三快照采集（生产先摘流量再拍，快照会 STW）
every(0, () => {}); // 占位避免误触
process.on('SIGUSR2', () => {
  const file = v8.writeHeapSnapshot(`/tmp/heap-${Date.now()}.heapsnapshot`);
  console.log('snapshot written:', file);
});

// 快照前的辅助观测：GC 后不回落才是真泄漏
setInterval(() => {
  const m = process.memoryUsage();
  metrics.gauge('heap_used_mb', m.heapUsed / 1024 / 1024);
  metrics.gauge('rss_mb', m.rss / 1024 / 1024);
  metrics.gauge('external_mb', m.external / 1024 / 1024); // Buffer 走这里
}, 10_000).unref();
// DevTools → Memory → Load 三份快照 → Comparison → 看 Delta 与 Retainers
```
