---
title: [NODE-635] V8 垃圾回收（分代与并发标记）对服务延迟的影响怎么调？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-635：V8 GC 对服务延迟怎么调？
**答**：
- 分代模型：新生代（Scavenger——半空间复制，快但频繁，对象熬过 2 次晋升老生代）+ 老生代（Mark-Compact——三色标记并发进行，major GC 停顿较长）。
- 延迟影响：新生代 GC 每次 ~1ms（频率高）；老生代 major GC 并发标记但仍有停顿段——P99 抖动的常见来源；大堆（>1.5GB）放大停顿。
- 调优手段：--max-old-space-size 合理上限（按容器内存留余量）；--max-semi-space-size 增大新生代（降低 GC 频率换单次耗时）；对象池化高频小对象；避免大对象短命分配（大 buffer 进外部内存/复用）。
- 观测：performance.measureMemory()、v8.getHeapStatistics()、GC 事件（--trace-gc / Perfetto）关联请求延迟——GC 停顿与 P99 毛刺对齐验证。
- 追问钩子：为什么「堆外内存」（Buffer）不受 V8 GC 管但也要管——Buffer 分配在 Node 的 C++ 层（外部内存），堆统计看不到，泄漏表现为 RSS 涨但 heapUsed 平稳；未释放的大 Buffer（连接缓冲池）是「堆健康但进程 OOM」的经典案例——观测必须同时看 heapUsed 与 rss。

```javascript
// GC 观测与调优
node --trace-gc --max-old-space-size=2048 --max-semi-space-size=32 server.js
setInterval(() => {
  const h = v8.getHeapStatistics();
  telemetry.push({ heap: h.used_heap_size, external: h.external_memory,
    rss: process.memoryUsage().rss });               // 三指标同看（SCN-BLD-253 同源）
}, 10_000);
```
