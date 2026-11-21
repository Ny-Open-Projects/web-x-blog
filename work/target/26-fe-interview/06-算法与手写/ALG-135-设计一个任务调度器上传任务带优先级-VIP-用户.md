---
title: [ALG-135] 设计一个任务调度器：上传任务带优先级（VIP 用户优先），并发上限 3，任务完成后自动补位，add 返回 Promise 拿结果？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-135：设计一个任务调度器：上传任务带优先级（VIP 用户优先），并发上限 3，任务完成后自动补位，add 返回 Promise 拿结果？
**答**：经典"队列 + 并发计数 + 补位"：add 把任务包上 resolve/reject 进队列并按优先级排序（生产用最小堆 O(log n)，示例用 sort O(n log n)）；每次入队或任务完成时尝试从队首取任务执行，直到占满并发额度；finally 里 `active--` 并递归 `_next` 补位。add 返回 Promise，业务侧 `await` 拿结果。

```javascript
class Scheduler {
  constructor(concurrency = 3) {
    this.concurrency = concurrency;
    this.active = 0;
    this.queue = [];
  }
  add(task, priority = 0) {            // task: () => Promise
    return new Promise((resolve, reject) => {
      this.queue.push({ task, priority, resolve, reject });
      // 生产环境用最小堆插入 O(log n)；示例用排序表达优先级语义
      this.queue.sort((a, b) => b.priority - a.priority);
      this._next();
    });
  }
  _next() {
    while (this.active < this.concurrency && this.queue.length) {
      const { task, resolve, reject } = this.queue.shift(); // 队首优先级最高
      this.active++;
      task().then(resolve, reject).finally(() => {
        this.active--;
        this._next();                  // 完成即补位
      });
    }
  }
}
// scheduler.add(() => uploadChunk(file), 10) // VIP 高优先级
```
