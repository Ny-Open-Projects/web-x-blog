---
title: [995] 笔试手写：实现短窗口请求合并（micro-batching）
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, 成本延迟, 合并]
type: 笔试题
---

## 995：笔试手写：实现短窗口请求合并（micro-batching）

**答**：实现 createBatcher(fn, { maxWait=50, maxSize=8 })：多个并发调用 fn(item) 时，50ms 窗口内到达的合并为一次 fn(batch) 批量执行（fn 返回数组按序对应），结果分发给各调用方；窗口满 maxSize 立即执行；fn 失败则本批所有调用 reject 同一错误。

```js
function createBatcher(fn, { maxWait = 50, maxSize = 8 } = {}) {
  let queue = [], timer = null, running = false;
  async function flush() {
    timer = null;
    if (running || !queue.length) return;
    running = true;
    const batch = queue; queue = [];
    try {
      const rs = await fn(batch.map(b => b.item));       // 批量执行一次
      batch.forEach((b, i) => b.resolve(rs[i]));         // 按序分发
    } catch (e) {
      batch.forEach(b => b.reject(e));                   // 整批同错
    } finally { running = false; if (queue.length) flush(); }
  }
  return item => new Promise((resolve, reject) => {
    queue.push({ item, resolve, reject });
    if (queue.length >= maxSize) return flush();         // 满批立即执行
    timer ??= setTimeout(flush, maxWait);                // 首个请求开窗口
  });
}
const batchEmbed = createBatcher(items => embedAll(items));
const [a, b] = await Promise.all([batchEmbed('x'), batchEmbed('y')]); // 合并为一次调用
```

**评分点**：
- 窗口逻辑：首个请求开定时器、满批提前 flush、flush 中新请求进下一轮
- 结果按序对应分发（数组下标对齐），错误整批传播
- running 锁防止 fn 执行期间重入（防重复批量）
- 能讨论参数权衡：maxWait 越大吞吐越好但延迟越高，50ms 是交互场景经验值；maxSize 受供应商批量接口上限约束

