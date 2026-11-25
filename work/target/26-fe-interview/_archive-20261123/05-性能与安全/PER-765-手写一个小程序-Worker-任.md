---
title: [PER-765] 手写一个小程序 Worker 任务调度器：Worker 池、任务队列与大数据传输的分片策略
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-765：手写一个小程序 Worker 任务调度器：Worker 池、任务队列与大数据传输的分片策略

**答**：
- 实现：Worker 池（2 个实例），任务队列 FIFO，任务带 transferable 标记（ArrayBuffer 直接 transfer 不拷贝）；大数据任务自动分片（按 1MB 切，Worker 端聚合结果）。
- 要点：任务超时与失败重试（Worker 可能崩）；池实例崩溃自动重建；任务优先级（用户交互触发的任务插队）。
- 边界：分片聚合要保证顺序（带 seq）；Worker 不可用（低版本基础库）降级主线程分片。
- 评分点：transferable 与降级路径。

```javascript

class WorkerScheduler {
  constructor(workerFactory, { poolSize = 2 } = {}) {
    this.pool = Array.from({ length: poolSize }, workerFactory);
    this.queue = []; this.busy = new Set();
    this.fallbackAvailable = true;
  }
  run(task) {                                                   // {payload, transfer, fn(降级用), priority}
    return new Promise((resolve, reject) => {
      task.resolve = resolve; task.reject = reject;
      if (task.priority === 'high') this.queue.unshift(task);
      else this.queue.push(task);
      this.pump();
    });
  }
  pump() {
    const free = this.pool.find(w => !this.busy.has(w));
    if (!free || !this.queue.length) return;
    const task = this.queue.shift();
    this.busy.add(free);
    const timer = setTimeout(() => this.onFail(free, task, 'timeout'), 10000);
    free.onmessage = ({ data }) => {
      clearTimeout(timer);
      this.busy.delete(free);
      task.resolve(data);
      this.pump();
    };
    try {
      free.postMessage(task.payload, task.transfer ?? []);      // transferable 零拷贝
    } catch { this.fallback(task); }                            // Worker 不可用降级
  }
  onFail(w, task, reason) {
    this.busy.delete(w);
    this.rebuild(w);                                            // Worker 崩溃重建
    if (task.retried) return this.fallback(task);
    task.retried = true;
    this.queue.unshift(task);
    this.pump();
  }
  fallback(task) {                                              // 主线程分片降级
    chunkedRun(task.fn, task.payload).then(task.resolve, task.reject);
  }
}
```
