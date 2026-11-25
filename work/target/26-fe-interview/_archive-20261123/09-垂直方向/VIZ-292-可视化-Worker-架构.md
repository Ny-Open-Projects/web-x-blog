---
title: [VIZ-292] 可视化 Worker 架构：数据计算下沉与 SharedArrayBuffer
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-292：可视化 Worker 架构：数据计算下沉与 SharedArrayBuffer

**答**：
- 重计算下沉 Worker：数据解析/聚合/降采样在 Worker，主线程只渲染；SharedArrayBuffer（需 COOP/COEP）零拷贝共享大数据。
- 传输优化：postMessage 大数组用 transferable（ArrayBuffer transfer 零拷贝）。
- 架构：Worker 池（计算并行）+ 主线程渲染，消息协议（请求 id/数据窗口）。

```javascript
// worker.js
self.onmessage = (e) => {
  const { id, op, data } = e.data;
  const result = op === 'm4' ? m4Aggregate(data, e.data.pixelWidth)
    : op === 'lttb' ? lttb(data, e.data.target);
  self.postMessage({ id, result }, [result.buffer]);      // transferable 零拷贝
};
// main.js
class ComputeWorkerPool {
  constructor(size = 4) { this.workers = [...Array(size)].map(() => new Worker('viz-worker.js'));
    this.pending = new Map(); this.nextId = 0; }
  compute(op, data, extra) {
    const id = this.nextId++;
    return new Promise(res => {
      this.pending.set(id, res);
      this.workers[id % this.workers.length].postMessage({ id, op, data, ...extra },
        [data.buffer]);                                     // 转移所有权
    });
  }
}
```
