---
title: [NODE-082] Node 内存调优怎么做（heap 限制与 heapdump 排查泄漏）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-082：Node 内存调优怎么做（heap 限制与 heapdump 排查泄漏）？
**答**：
- 两个 heap 概念区分：`--max-old-space-size`（老生代上限，64 位默认约 2-4GB，容器里必须显式设置并**小于容器内存限制**，否则 OOMKilled）；`Buffer`/`ArrayBuffer` 在堆外（`external`/`arrayBuffers`），流处理失控常表现为 rss 涨而 heapUsed 不涨。
- 泄漏排查路径：监控发现 rss/heapUsed 持续上涨不回落 → `heapdump`/`--heapsnapshot-signal=SIGUSR2` 抓堆快照 → Chrome DevTools Memory 面板做两次快照对比（Comparison 视图看增量对象与 Retained Size）→ 定位持有链（常见：全局 Map 缓存无上限、事件监听器未移除、闭包持有大对象、定时器未清理）。
- 快速手段：`process.memoryUsage()` 定时打日志；`v8.getHeapStatistics()`；生产常驻 `--max-old-space-size=容器内存的75%` + `max_memory_restart`。

```javascript
// 1. 启动参数（Docker/K8s 场景）
// node --max-old-space-size=384 main.js   # 容器 limit 512m，heap 只占 75%
// node --heapsnapshot-signal=SIGUSR2 main.js  # kill -USR2 <pid> 触发快照，无需额外依赖

// 2. 内存水位监控 + 自动抓快照
const v8 = require('node:v8');
setInterval(() => {
  const mem = process.memoryUsage();
  const heapLimit = v8.getHeapStatistics().heap_size_limit;
  const ratio = mem.heapUsed / heapLimit;
  metrics.gauge('node_heap_used_bytes', mem.heapUsed);
  metrics.gauge('node_rss_bytes', mem.rss);
  metrics.gauge('node_external_bytes', mem.external);   // 堆外：Buffer 泄漏看这里
  if (ratio > 0.85) {
    log.error({ event: 'heap_critical', ratio, heapUsed: mem.heapUsed });
    v8.writeHeapSnapshot(`/tmp/heap-${Date.now()}.heapsnapshot`); // 自动留证
  }
}, 30000).unref();

// 3. 经典泄漏案例：无上限缓存
const cache = new Map();
app.use(async (ctx) => {
  cache.set(ctx.url, bigObject);   // BUG：只进不出，QPS 高时必然 OOM
  // 修复：LRU + 容量上限
  // const lru = new LRU({ max: 1000, ttl: 60000 }); lru.set(ctx.url, bigObject);
});

// 4. 事件监听器泄漏：MaxListenersExceededWarning 就是前兆
// emitter.on('data', handler) 在每次请求都注册却从不 off → 修复：命名函数 + once//removeListener
```

```bash
# 排查流程命令行
kill -USR2 $(pgrep -f bff-server)             # 触发堆快照
ls -lh /tmp/heap-*.heapsnapshot
# Chrome DevTools → Memory → Load 快照 → Selection: Comparison
# 关注 Shallow Size 与 Retained Size 排序、Constructor 中的 Map/Array/闭包
clinic heapprofiler -- node main.js           # 或 clinic 自动定位增长源
```
