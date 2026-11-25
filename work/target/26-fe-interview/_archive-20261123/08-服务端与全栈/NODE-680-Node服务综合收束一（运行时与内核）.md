---
title: [NODE-680] Node 服务综合收束一：运行时与内核方法论？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-680：运行时收束
**答**：
- 内核主线：libuv 阶段与微任务插入点/worker 选型三分法/GC 三指标观测/Stream 背压链路完整性（NODE-633/634/635/636）。
- 进程主线：cluster 状态外置/优雅关闭三步/崩溃风暴限流/黑盒记录仪（NODE-637/638/648）。
- 性能主线：事件循环延迟心电图/heap 快照对比泄漏定位/线程池共享竞争/剖析摘流纪律（NODE-671/672/673）。
- 面试答法：Node 运行时的三个健康问——「事件循环延迟 P99 多少」（阻塞度）、「GC 后基线回落吗」（泄漏）、「崩溃后多久恢复」（自愈）——三问覆盖运行时健康度。

```javascript
const nodeRuntime = {
  kernel: ['libuv-phases', 'worker-3way', 'gc-3metrics', 'backpressure-chain'],
  process: ['cluster-stateless', 'graceful-3steps', 'crash-storm-limit', 'blackbox-recorder'],
  perf: ['eld-p99', 'heap-diff', 'threadpool-contention', 'profile-on-drained'],
};
```
