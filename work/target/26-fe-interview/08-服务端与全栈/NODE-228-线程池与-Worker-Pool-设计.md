---
title: [NODE-228] 线程池与 Worker Pool 设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-228：线程池与 Worker Pool 设计？
**答**：
- 池化必要性：Worker 创建成本高（新 V8 实例 ~几十 ms）——池化复用（piscina 的设计思想）。
- 池大小：CPU 密集 = 核数（或 -1）；I/O 混合可略超；过大会调度抖动+内存乘倍。
- 池要素：任务队列（FIFO+优先级）、并发上限、超时回收（僵尸 worker 强杀）、忙时拒绝/排队策略。
- 实现：piscina 开箱即用；手写要点是"任务 Promise 化 + result 关联（id 映射）+ 错误传播"。

```javascript
import Piscina from 'piscina';
const pool = new Piscina({
  filename: './workers/image-worker.js',
  maxThreads: Math.min(os.cpus().length, 8),
  maxQueue: 1000,                              // 池要素：队列上限（拒绝策略）
  idleTimeout: 30000,
});
const result = await pool.run({ buf }, { transfer: [buf.buffer], signal: AbortSignal.timeout(10_000) });
// 手写池核心（简化）：
class WorkerPool {
  #idle = []; #queue = []; #busy = new Map();
  acquire(task) {
    const w = this.#idle.pop() ?? new Worker('./worker.js');
    return new Promise((res, rej) => {
      w.postMessage({ id: task.id, data: task.data });
      this.#busy.set(task.id, { w, res, rej });
      w.on('message', m => { if (m.id === task.id) { this.#release(w); res(m.result); } });
    });
  }
  #release(w) { if (this.#idle.length < this.max) this.#idle.push(w); else w.terminate(); }
}
```
