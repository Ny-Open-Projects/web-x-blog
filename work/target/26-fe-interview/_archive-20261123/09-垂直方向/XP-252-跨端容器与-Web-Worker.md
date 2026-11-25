---
title: [XP-252] 跨端容器与 Web Worker：CPU 密集任务下沉（笔试）
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 笔试题, 27]
type: 笔试题
---

## XP-252：跨端容器与 Web Worker：CPU 密集任务下沉（笔试）

**答**：
- 题目：容器内 CPU 密集任务（数据解析/加密）下沉 Worker——容器环境 Worker 支持（JS 线程池）与消息传递。
- 思路：容器内 Worker 池（HW-334 复用）——创建 N 个 JS 线程（独立上下文）；任务队列 + 优先级；结果回传（结构化克隆）。
- 评分点：线程池创建；任务调度；数据传输。

```javascript
class ContainerWorkerPool {
  constructor(size = 2) {                                       // 容器内线程池
    this.workers = Array.from({ length: size }, () => this.createWorker());
    this.q = []; this.busy = new Set();
  }
  createWorker() {                                              // 创建 JS 线程
    const worker = new ContainerWorker('worker.js');             // 容器 Worker API
    worker.onmessage = (e) => { this.busy.delete(worker); this.pump(); };
    return worker;
  }
  run(task, payload) {                                          // 任务下发
    return new Promise((res) => { this.q.push({ task, payload, res }); this.pump(); });
  }
  pump() {                                                       // 调度
    while (this.q.length) {
      const idle = this.workers.find(w => !this.busy.has(w));
      if (!idle) break;
      const job = this.q.shift(); this.busy.add(idle);
      idle.postMessage(job);                                      // 异步执行
    }
  }
}
// 收益：JSON 解析 50MB 数据主线程 800ms → Worker 300ms（主线程不阻塞）
```
