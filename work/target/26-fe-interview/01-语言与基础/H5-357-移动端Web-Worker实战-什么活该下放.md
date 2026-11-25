---
title: [H5-357] 移动端 Web Worker 实战：什么活该下放
date: 2026-11-21
categories: [HTML5]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## H5-357：移动端 Web Worker 实战：什么活该下放

**答**：
- 下放标准：单次 > 50ms 的纯计算（大 JSON 解析、加密、图片处理、数据聚合）才值得 Worker——小任务通信开销反而亏（移动端 IPC 不便宜）
- 移动端 Worker 特有考量：Worker 数量受内存约束（低端机 2~4 个），用池化复用而不是按任务创建；Worker 冷启动（脚本加载+wasm 实例化）要预热
- 数据传输设计：大 ArrayBuffer 用 transferable 零拷贝；高频小消息合并批传；结构化克隆大对象很贵（兆级要秒考虑分片）
- Worker 内能力：可 fetch/IndexedDB/WebSocket（与主线程同源隔离），图片解码 createImageBitmap 也可下放；不可用 DOM
- 典型架构：单 Worker 串行队列（简单任务）+ 池并行（CPU 密集）+ 主线程只做 UI——移动端页面 INP 主要靠这个架构救

```javascript
// worker-pool.js
class WorkerPool {
  constructor(n) {
    this.idle = Array.from({ length: n }, () => new Worker('compute.js'));
    this.queue = [];
  }
  exec(payload, transfer = []) {
    return new Promise((resolve, reject) => {
      const w = this.idle.pop();
      if (w) return this._run(w, payload, transfer, resolve, reject);
      this.queue.push({ payload, transfer, resolve, reject });
    });
  }
  _run(w, payload, transfer, resolve, reject) {
    const onmsg = ({ data }) => {
      w.removeEventListener('message', onmsg);
      data.ok ? resolve(data.result) : reject(data.error);
      const next = this.queue.shift();
      next ? this._run(w, next.payload, next.transfer, next.resolve, next.reject) : this.idle.push(w);
    };
    w.addEventListener('message', onmsg);
    w.postMessage(payload, transfer);
  }
}
```
