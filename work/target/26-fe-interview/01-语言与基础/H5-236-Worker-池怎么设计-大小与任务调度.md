---
title: [H5-236] Worker 池怎么设计：大小与任务调度
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, Worker]
type: 面试题
---

## H5-236：Worker 池怎么设计：大小与任务调度

**答**：
- 池大小：默认 `navigator.hardwareConcurrency - 1`（给主线程留一核），上限一般 4~8；移动端保守
- 调度策略：FIFO 简单够用；长任务 + 短任务混合时建议双队列（防长任务阻塞短任务）；可按任务类型固定 worker（亲和性减少上下文切换）
- 生命周期：常驻（重复任务复用，省启动成本）vs 按需创建销毁（省内存）；图片处理类建议常驻
- 错误处理：worker.onerror 整个线程级错误要重建 worker；任务级异常走 message 回传
- 面试话术：池的本质是「把 Worker 的创建成本与任务排队解耦」，讲出 3 个设计维度（大小/调度/生命周期）即完整

```javascript
class WorkerPool {
  #workers; #queue = []; #idle = [];
  constructor(size = Math.min(navigator.hardwareConcurrency - 1, 6)) {
    this.#workers = Array.from({ length: size }, () => this.#spawn());
  }
  #spawn() {
    const w = new Worker('task.js');
    w.onmessage = (e) => { const { resolve } = w._task; resolve(e.data); w._task = null; this.#idle.push(w); this.#drain(); };
    return w;
  }
  run(data, transfer) {
    return new Promise((resolve, reject) => {
      this.#queue.push({ data, transfer, resolve, reject });
      this.#drain();
    });
  }
  #drain() {
    const w = this.#idle.pop();
    if (w && this.#queue.length) {
      const t = this.#queue.shift(); w._task = t;
      w.postMessage(t.data, t.transfer || []);
    }
  }
}
```
