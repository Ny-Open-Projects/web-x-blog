---
title: [NODE-349] Node 服务的内存泄漏排查方法如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-349：Node 服务的内存泄漏排查
**答**:
- 发现：RSS 持续爬升（压测前后对比 + 灰度单实例观测）、GC 后老年代不回落（heapUsed 趋势）、Node 18+ 可用 performance.measureUserAgentSpecificMemory 定期采样。
- 采集：堆快照对比法（heapdump / inspector——泄漏前 snap A、跑 N 次可疑操作后 snap B，比较增量对象与 retainer 链）；生产在线采样用 inspector 命令（ARC-309），避免全量 dump 卡服务。
- 常见根因清单：全局 Map/数组只增不减（缓存无上限）、事件监听器未移除（MaxListenersExceededWarning 是信号）、闭包持有大请求对象（日志闭包捕获 res）、定时器未清、Promise 未处理的悬挂引用、外部库内部缓存。
- 工具链：--inspect + Chrome DevTools Memory 面板、clinic heapprofiler（分配火焰图找分配热点）、memwatch-next 类 GC 监控。
- 预防：缓存必带上限与 TTL（ARC-445 原则移植）、监听器配对、大对象不进长生命周期作用域；CI 压测内存回归（固定请求量后 RSS 增长阈值）。
```javascript
// 在线堆快照（inspector）
const inspector = require('inspector');
const session = new inspector.Session();
session.connect();
function heapSnapshot() {
  return new Promise(res => {
    session.post('HeapProfiler.takeHeapSnapshot', null, (e, r) => {
      // 流式写到文件（分 chunk），避免整段驻内存
      res(r);
    });
  });
}
// 流程：snap A → 复现操作 → snap B → DevTools 比较 (Comparison View) 找 retainer
```
