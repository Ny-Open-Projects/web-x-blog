---
title: [JS-348] Worker 池大小与任务粒度设计
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## JS-348：Worker 池大小与任务粒度设计

**答**：
- 池大小：hardwareConcurrency 为上限，但移动端要打折（核心数≠可用算力，别的 App 在抢）——实践取 min(4, hardwareConcurrency - 1)；Worker 本身占内存（每实例 V8 堆），低端机 2~4 个封顶
- 任务粒度：单任务计算时长 >> 消息往返成本（毫秒级）才值得下放；太碎的任务（<10ms）调度开销反噬收益——批量化（一次传一批）
- 数据传输成本：结构化克隆大对象很贵（兆级对象拷贝秒级感知）——优先 transferable（ArrayBuffer）或 SAB 共享；能传指针不传数据
- 动态伸缩：任务队列深度驱动 Worker 按需创建（上限封顶），空闲超时 terminate 释放内存——与服务器连接池同构
- 失败处理：Worker 崩溃（onerror）后重建实例并重放任务；毒任务（反复崩溃的输入）标记隔离——池的健壮性来自这层

```javascript
class WorkerPool {
  constructor(url, max = Math.min(4, (navigator.hardwareConcurrency || 2) - 1)) {
    this.url = url; this.max = max; this.pool = []; this.queue = [];
  }
  async run(msg, transfer = []) {
    if (!this.pool.length && this.pool.length + this.queue.length < this.max)
      this.pool.push(this._spawn());
    const w = this.pool.find(w => !w.busy) || await new Promise(r => this.queue.push(r));
    if (!w) return this.run(msg, transfer);
    w.busy = true;
    return new Promise((resolve, reject) => {
      w.onmessage = ({ data }) => { w.busy = false; resolve(data); this._free(w); };
      w.onerror = (e) => { w.busy = false; reject(e); this._rebuild(w); };
      w.postMessage(msg, transfer);
    });
  }
  _free(w) { const n = this.queue.shift(); if (n) n(w); }
  _rebuild(w) { this.pool = this.pool.filter(x => x !== w); w.terminate(); this.pool.push(this._spawn()); }
  _spawn() { const w = new Worker(this.url); w.busy = false; return w; }
}
```
