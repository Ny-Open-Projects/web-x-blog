---
title: [HW-086] 手写常驻异步 Worker 队列——单 worker 串行消费 + 背压上限 + 优雅关闭
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：常驻消费循环：任务来了入队，worker 循环取任务执行直到队列空（不销毁，避免每次重建开销）。背压：队列超上限时 push 返回等待 Promise（生产者被限流）。优雅关闭：close() 停止接收新任务，等当前任务做完。

```javascript
class AsyncWorker {
  constructor(handler, { maxQueue = 1000 } = {}) {
    Object.assign(this, { handler, maxQueue });
    this.queue = []; this.running = false; this.closed = false;
    this.queueFull = null;
  }
  push(job) {
    if (this.closed) return Promise.reject(new Error('closed'));
    if (this.queue.length >= this.maxQueue) {          // 背压：等待腾位
      if (!this.queueFull) this.queueFull = new Promise((r) => (this.queueFullResolve = r));
      return this.queueFull.then(() => this.push(job));
    }
    return new Promise((resolve, reject) => {
      this.queue.push({ job, resolve, reject });
      this.#drain();
    });
  }
  async #drain() {
    if (this.running) return;
    this.running = true;
    while (this.queue.length) {
      const { job, resolve, reject } = this.queue.shift();
      try { resolve(await this.handler(job)); }
      catch (e) { reject(e); }
      if (this.queue.length < this.maxQueue && this.queueFullResolve) {  // 腾位唤醒生产者
        const r = this.queueFullResolve; this.queueFull = null; this.queueFullResolve = null; r();
      }
    }
    this.running = false;
  }
  async close() {                                     // 优雅关闭：不再接新任务
    this.closed = true;
    while (this.running || this.queue.length) await new Promise((r) => setTimeout(r, 50));
  }
}
// 用法：埋点消费 worker
const w = new AsyncWorker(async (ev) => { await send(ev); }, { maxQueue: 500 });
w.push({ type: 'click', ts: Date.now() });
```

**评分点**：
- 单 worker 循环消费（running 防重入），队列空不销毁 worker。
- 背压：队列满时生产者 Promise 挂起，腾位时单次唤醒（queueFull 状态复位）。
- 优雅关闭语义：closed 拒绝新任务、等待在途完成。
- handler 异常 reject 对应任务不炸整个循环。
