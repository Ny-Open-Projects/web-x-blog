---
title: [NODE-724] 笔试题——实现 worker 任务池（调度 + 超时 + 池化复用）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-724：手写 worker 池

**需求与边界**：
- 需求：worker_threads 池（SCN-NODE-634）——① 固定 worker 复用（每任务 postMessage——不新建）；② 任务超时（超时 kill 该 worker + 重建——卡死任务不影响池）；③ 队列（池满排队——上限后拒绝）；④ 优雅关闭（排空任务后 terminate）。

**答**：
```javascript
import { Worker } from 'worker_threads';
class WorkerPool {
  constructor({ size = 4, taskTimeout = 10_000 } = {}) {
    this.size = size; this.timeout = taskTimeout;
    this.idle = []; this.queue = []; this.workers = new Set();
  }
  run(task) {
    return new Promise((resolve, reject) => {
      const item = { task, resolve, reject };
      const w = this.idle.pop();
      w ? this.exec(w, item) : this.queue.length < 1000 ? this.queue.push(item)
        : reject(new Error('POOL_FULL'));              // 队列上限（SCN-NODE-641 快速失败）
    });
  }
  exec(worker, item) {
    const timer = setTimeout(() => {                   // 超时：kill + 重建（卡死隔离）
      worker.terminate();
      item.reject(new Error('TASK_TIMEOUT'));
      this.spawn();                                    // 替换死 worker
    }, this.timeout);
    worker.once('message', (result) => { clearTimeout(timer);
      this.idle.push(worker); item.resolve(result); this.next(); });
    worker.postMessage(item.task);
  }
  spawn() {
    const w = new Worker('./task.js'); this.workers.add(w); this.idle.push(w);
    w.on('message', ...);                              // 复用绑定
    return w;
  }
  async drain() {                                      // 优雅关闭（SCN-NODE-638）
    await Promise.all([...this.workers].map(w => new Promise(res => {
      w.on('exit', res); w.postMessage({ type: 'DRAIN' });
    })));
  }
}
```

**评分点**:
- 复用池化（idle 栈 pop——不新建 worker）。
- 超时 kill + 重建（卡死任务隔离——SCN-NODE-634）。
- 队列上限快速失败（SCN-NODE-639 池耗尽策略）。
- 优雅关闭 drain（SCN-NODE-638 语义）。
