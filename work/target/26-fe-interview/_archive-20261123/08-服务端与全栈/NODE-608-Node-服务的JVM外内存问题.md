---
title: [NODE-608] Node 服务的堆外内存（Buffer/native 泄漏）排查如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面题, 20]
type: 面试题
---

## NODE-608：堆外内存排查
**答**:
- 问题特征：RSS 远大于 heapUsed（heap 正常但进程内存涨）——堆外：Buffer 分配/native addon/线程栈。
- 常见根因：Buffer 未释放（大 Buffer 引用滞留——数组/闭包持有；Buffer 池 8KB 分配策略——小 buffer 累积在池里不还 OS）、native 模块泄漏（C++ addon 内存——addon 自身 bug）、流缓冲堆积（backpressure 忽略——数据堆积 NODE-010）、worker 泄漏（worker 不销毁——线程栈/内存）。
- 排查手段：RSS vs heapUsed 分离监控（差值趋势——堆外增长识别）、Buffer 使用统计（process.memoryUsage().arrayBuffers——Node 18+）、native 泄漏工具（valgrind/massif 对 addon、`node --heapsnapshot` 看不到的用 ASAN 重编 addon）、fd/线程数监控（lsof/线程数——句柄与 worker 泄漏）。
- 防护：Buffer 池化复用（大 buffer 复用——减少分配压力）、流必处理背压、addon 评审（native 依赖最少化——引入评审）、容器 limit 对齐（--max-old-space-size + RSS 预算——NODE-374）。
```javascript
// 堆外监控
setInterval(() => {
  const m = process.memoryUsage();
  const external = m.rss - m.heapUsed;                          // 堆外近似
  metrics.gauge('mem.external', external);
  metrics.gauge('mem.arrayBuffers', m.arrayBuffers ?? 0);       // Buffer 明细
  if (external > base * 2) snapshotForProfiling();              // 采样定位
}, 30e3);
```
