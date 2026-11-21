---
title: [PER-270] 笔试题：手写 Worker 大对象任务的内存回压队列（在途上限 + transfer + 完成回收）
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-270：手写 Worker 大对象任务的内存回压队列（在途上限 + transfer + 完成回收）

**题目**：实现 `WorkerPool(n, workerUrl)`：① n 个 worker 轮询分发；② 每个任务传 ArrayBuffer 用 transfer 零拷贝；③ 回压控制：在途任务总数不超过 n × 2，超限任务排队等待；④ 任务返回 Promise（按 id 匹配消息）；⑤ worker 出错时任务 reject 并继续调度后续任务。

**答**：回压是关键——无上限 postMessage 会把大 buffer 全 clone/堆积在队列里，内存与 worker 都打爆。用"id 匹配 Promise + 在途计数"实现背压。

```javascript
class WorkerPool {
  constructor(n, workerUrl) {
    this.free = Array.from({ length: n }, () => {
      const w = new Worker(workerUrl);
      w.onmessage = (e) => this.#settle(e.data.id, null, e.data.result, w);
      w.onerror = (e) => this.#settle(this.#errId(w), e.message ?? 'worker error', null, w);
      return { w, idle: true };
    });
    this.queue = []; this.pending = 0; this.maxPending = n * 2;
    this.jobs = new Map(); this.nextId = 0;
  }
  #settle(id, err, result, w) {
    const job = this.jobs.get(id); this.jobs.delete(id);
    this.pending--; this.#markIdle(w);
    err ? job?.reject(new Error(err)) : job?.resolve(result);
    this.#dispatch();
  }
  #markIdle(w) { const it = this.free.find(x => x.w === w); if (it) it.idle = true; }
  #errId(w) { /* worker 全错时 reject 其在途任务：遍历找归属（简化：用 nextId 记录） */
    for (const [id, j] of this.jobs) if (j.worker === w) return id; return -1; }
  run(buffer) {
    return new Promise((resolve, reject) => {
      if (this.pending >= this.maxPending) this.queue.push({ buffer, resolve, reject });
      else this.#start(buffer, resolve, reject);
    });
  }
  #start(buffer, resolve, reject) {
    const id = ++this.nextId;
    const slot = this.free.find(x => x.idle) ?? this.free[0];
    slot.idle = false; this.pending++;
    this.jobs.set(id, { resolve, reject, worker: slot.w });
    slot.w.postMessage({ id, buffer }, [buffer]);     // transfer 所有权，零拷贝
  }
  #dispatch() {
    while (this.pending < this.maxPending && this.queue.length) {
      const { buffer, resolve, reject } = this.queue.shift();
      this.#start(buffer, resolve, reject);
    }
  }
}
```

**评分点**：
- transfer 列表 `[buffer]` 使用正确，并能说明所有权转移语义。
- 回压：pending 上限 + queue 排队，上限与 worker 数相关（n×2）。
- Promise 按 id 匹配（Map 结算），支持并发不串扰。
- 错误路径：worker 出错 reject 对应任务并恢复调度（不死锁队列）。
