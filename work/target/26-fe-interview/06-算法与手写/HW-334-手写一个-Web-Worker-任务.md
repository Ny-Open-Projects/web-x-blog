---
title: [HW-334] 手写一个 Web Worker 任务引擎：池化、优先级与超时
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-334：手写一个 Web Worker 任务引擎：池化、优先级与超时

**答**：
- 需求：实现 WorkerPool：N 个 worker 常驻池；run(task, payload, {priority, timeoutMs}) 分派到空闲 worker（无空闲按优先级排队）；超时终止（terminate 该 worker 并重建，任务拒绝）；transferable 支持（大数组零拷贝转移）。
- 边界：超时 terminate 后池大小恢复（重建 worker）；任务结果回传结构化克隆（transfer 列表转移）；同 worker 串行（忙则复用其他）。
- 评分点：池化分派；超时 terminate+重建；transferable。

```javascript
class WorkerPool {
  constructor(workerSrc, size = 4) {
    this.size = size; this.workers = Array.from({ length: size }, () => this.spawn(workerSrc));
    this.q = []; this.busy = new Map();
  }
  spawn(src) { const w = new Worker(src); w.__idle = true; return w; }
  run(task, payload, { priority = 5, timeoutMs = 30000, transfer = [] } = {}) {
    return new Promise((res, rej) => this.q.push({ task, payload, priority, timeoutMs, transfer, res, rej, seq: this.q.length }))
      .finally(() => this.pump());
  }
  pump() {
    while (true) {
      const w = this.workers.find(x => x.__idle);
      if (!w) break;
      this.q.sort((a, b) => b.priority - a.priority || a.seq - b.seq);   // 优先级+序
      const job = this.q.shift();
      if (!job) break;
      w.__idle = false; this.busy.set(w, job);
      const timer = setTimeout(() => {                       // 超时 terminate+重建
        w.terminate();
        const i = this.workers.indexOf(w);
        this.workers[i] = this.spawn(w.__src);
        this.busy.delete(w);
        job.rej(new Error('worker-timeout'));
        this.pump();
      }, job.timeoutMs);
      w.onmessage = e => { clearTimeout(timer); w.__idle = true; this.busy.delete(w); job.res(e.data); this.pump(); };
      w.onerror = e => { clearTimeout(timer); w.__idle = true; this.busy.delete(w); job.rej(e); this.pump(); };
      w.postMessage({ task: job.task, payload: job.payload }, job.transfer);   // transferable 零拷贝
    }
  }
}
```
