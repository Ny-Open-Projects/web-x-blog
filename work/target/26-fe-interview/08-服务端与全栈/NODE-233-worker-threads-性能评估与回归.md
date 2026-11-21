---
title: [NODE-233] worker_threads 性能评估与回归？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-233：worker_threads 性能评估与回归？
**答**：
- 评估指标：任务 P95（含排队）、主线程事件循环阻塞时长（eventLoopUtilization 前后对比）、内存（worker 基座成本）。
- 收益验证：改造前主线程被 CPU 任务阻塞（其他请求 P95 恶化），改造后主线程 P95 恢复、worker 任务 P95 可控——两个指标都要看。
- 回归陷阱：池太小 → 排队 P95 恶化；池太大 → CPU 争抢（每线程 time slice 下降）——池大小压测扫描（2/4/8 档）。
- 监控接入：pool 队列长度、活跃 worker 数、任务耗时直方图进 metrics（NODE-36x trace 关联任务 id）。

```javascript
// 评估脚本
const before = eventLoopUtilization();
const t0 = performance.now();
await pool.run(task);
const elu = eventLoopUtilization(before).utilization;   // 主线程被占用的比例
perf.histogram('cpu-task', { ms: performance.now() - t0, elu });
// 池大小扫描（压测）
for (const size of [2, 4, 8]) {
  pool.setOptions({ maxThreads: size });
  const r = await autocannon({ url, connections: 50, duration: 30 });
  console.log(size, r.latency.p95, r.errors);
}
// 阻塞检测：改造前 main thread elu ≈ 1.0（阻塞），改造后 < 0.5
```
