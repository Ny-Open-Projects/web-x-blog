---
title: [TST-044] 笔试：手写并行测试 runner（Promise.allSettled + 并发上限）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-044：笔试：手写并行测试 runner（Promise.allSettled + 并发上限）
**答**：
- 需求：N 个异步测试文件用例并行执行，并发上限 W（模拟 worker 池），单个失败不中断整体，最终汇总 passed/failed/duration。
- 核心：worker 池模型——起 W 个 worker 循环从队列取用例，比 allSettled 一次性并发更可控；或用 allSettled + 手动分片。实现失败隔离与总耗时统计。
- 边界：队列耗尽时 worker 退出；统计并发度峰值；用例抛同步异常也要被 Promise 包装捕获。

```javascript
async function runParallel(tasks, concurrency = 4) {
  const queue = tasks.map((t, i) => ({ ...t, index: i }));
  const results = new Array(tasks.length);
  const start = Date.now();
  let maxInFlight = 0, inFlight = 0;

  async function worker() {
    while (queue.length) {
      const t = queue.shift();
      inFlight++; maxInFlight = Math.max(maxInFlight, inFlight);
      try {
        await Promise.resolve().then(t.fn);           // 同步异常也转 Promise 捕获
        results[t.index] = { name: t.name, ok: true };
      } catch (e) {
        results[t.index] = { name: t.name, ok: false, err: e.message };
      }
      inFlight--;
    }
  }

  await Promise.all(Array.from({ length: Math.min(concurrency, tasks.length) }, worker));
  return { results, ms: Date.now() - start, maxInFlight };
}

// ---- 用法 ----
const cases = Array.from({ length: 10 }, (_, i) => ({
  name: `case-${i}`,
  fn: () => new Promise((r) => setTimeout(r, 100)).then(() => {
    if (i === 3) throw new Error('boom');   // case-3 失败
  }),
}));
const { results, ms, maxInFlight } = await runParallel(cases, 4);
console.log(`耗时 ${ms}ms（串行需 ~1000ms），峰值并发 ${maxInFlight}`);
console.log(results.filter((r) => !r.ok)); // 仅 case-3
```
**评分点**：
- worker 池（固定 W 个消费者）而非一次性 Promise.all —— 并发上限可控。
- allSettled 思想：失败隔离，全部跑完再汇总。
- 同步异常 Promise 包装；总耗时与峰值并发统计。
- 能对应到 Vitest 的 pool/maxWorkers 配置。
