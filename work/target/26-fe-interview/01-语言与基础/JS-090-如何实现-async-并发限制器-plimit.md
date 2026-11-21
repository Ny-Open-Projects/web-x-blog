---
title: [JS-090] 如何实现 async 并发限制器（p-limit）？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-090：如何实现 async 并发限制器（p-limit）？

**答**：
- 核心状态：活跃数 activeCount、等待队列 queue、并发上限 concurrency。
- 提交任务：未达上限立即执行并 activeCount++；否则入队等待。
- 任务结算：无论成败都 activeCount-- 并从队首取下一个任务，保证槽位不泄漏。
- 返回值语义：limit(fn) 返回的 Promise 就是该任务本身的 Promise，可直接进 Promise.all。

```mermaid
flowchart TD
    A[调用 limit 提交任务] --> B{活跃数小于并发上限}
    B -->|是| C[立即执行 活跃数加一]
    B -->|否| D[任务执行器进入等待队列]
    C --> E[任务结算 成功或失败]
    E --> F[活跃数减一]
    F --> G{等待队列非空}
    G -->|是| H[取出队首立即执行]
    G -->|否| I[池进入空闲]
    H --> E
```

```javascript
function pLimit(concurrency) {
  if (!Number.isInteger(concurrency) || concurrency < 1) {
    throw new TypeError('concurrency 必须是正整数');
  }
  let activeCount = 0;
  const queue = [];

  const next = () => {
    activeCount -= 1;
    if (queue.length > 0) queue.shift()();
  };

  const run = (fn, resolve, reject) => {
    activeCount += 1;
    fn().then(resolve, reject).then(next); // 结算后释放槽位
  };

  return function limit(fn) {
    return new Promise((resolve, reject) => {
      const start = () => run(fn, resolve, reject);
      if (activeCount < concurrency) start();
      else queue.push(start);
    });
  };
}

const limit = pLimit(2);
const task = (id) => () =>
  new Promise((r) => setTimeout(() => {
    console.log('done', id);
    r(id);
  }, 100));

(async () => {
  const results = await Promise.all([1, 2, 3, 4, 5].map((i) => limit(task(i))));
  console.log('all', results); // done 输出永远两个一组
})();
```
