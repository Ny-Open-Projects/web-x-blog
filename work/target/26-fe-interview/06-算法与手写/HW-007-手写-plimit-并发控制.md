---
title: [HW-007] 手写 p-limit 并发控制
date: 2026-11-17
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-007：手写 p-limit 并发控制

**答**：
- 评分点：维护「当前执行中数量 active」+「等待队列 queue」两个核心状态；新任务进来时若未满并发数直接执行，否则入队；每个任务结束后 `active--` 并从队列取下一个（调度时机必须在 finally，成功失败都要调度）；返回的 Promise 与原任务一一对应（resolve/reject 要绑定到具体任务，不能错位）；能说出并发数必须为正整数。

```javascript
// ===== 5 分钟速写版 =====
function pLimit(concurrency) {
  let active = 0;
  const queue = [];
  const next = () => {
    active--;
    if (queue.length) queue.shift()();
  };
  const run = (fn, resolve, reject) => {
    active++;
    fn().then(resolve, reject).finally(next); // 成败都要释放槽位
  };
  return fn => new Promise((resolve, reject) => {
    if (active < concurrency) run(fn, resolve, reject);
    else queue.push(() => run(fn, resolve, reject));
  });
}
// 用法：
// const limit = pLimit(3);
// urls.forEach(u => limit(() => fetch(u)));

// ===== 标准完整版（含边界处理）=====
function pLimitPro(concurrency) {
  if (!Number.isInteger(concurrency) || concurrency < 1) {
    throw new TypeError('concurrency must be a positive integer');
  }
  let active = 0;
  const queue = [];
  const dequeue = () => {
    while (active < concurrency && queue.length) {
      const { fn, resolve, reject } = queue.shift();
      active++;
      fn().then(resolve, reject).catch(() => {}).finally(() => {
        active--;
        dequeue(); // 链式补位，保证一次释放能拉起多个等待任务
      });
    }
  };
  const limit = fn => new Promise((resolve, reject) => {
    if (typeof fn !== 'function') return reject(new TypeError('fn must be a function'));
    queue.push({ fn, resolve, reject });
    dequeue();
  });
  // 附加能力：暴露当前状态，便于监控与测试
  limit.activeCount = () => active;
  limit.pendingCount = () => queue.length;
  limit.clearQueue = () => { queue.length = 0; }; // 场景切换时丢弃未执行任务
  return limit;
}
// 批量场景：分页采集 100 个接口，限制并发 5
// const limit = pLimitPro(5);
// await Promise.all(ids.map(id => limit(() => fetchDetail(id))));
```

---
