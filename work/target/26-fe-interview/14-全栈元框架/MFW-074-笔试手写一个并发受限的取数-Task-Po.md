---
title: [MFW-074] 笔试：手写一个并发受限的取数任务池（Promise Pool）
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-074：笔试：手写一个并发受限的取数任务池（Promise Pool）
**答**：SSR 页面要并发拉 100 个推荐接口，直接 Promise.all 会打爆下游。实现 `promisePool(tasks, limit)`：① 任意时刻最多 limit 个任务在跑；② 全部完成后按原顺序返回结果数组；③ 单个任务失败不影响其他任务（结果对应位置为 rejected 原因）；④ 全部失败时整体尽快返回。

```ts
type Settled<T> = { status: 'fulfilled'; value: T } | { status: 'rejected'; reason: unknown };

async function promisePool<T>(
  tasks: Array<() => Promise<T>>,
  limit: number,
): Promise<Array<Settled<T>>> {
  const results: Array<Settled<T>> = new Array(tasks.length);
  let next = 0; // 下一个待领取任务的下标（任务队列游标）

  // 每个worker：循环领任务，直到队列领空
  async function worker(): Promise<void> {
    while (next < tasks.length) {
      const index = next++;
      try {
        results[index] = { status: 'fulfilled', value: await tasks[index]() };
      } catch (reason) {
        results[index] = { status: 'rejected', reason };
      }
    }
  }

  // 并发上限 = min(limit, 任务数)；零任务直接返回
  const workerCount = Math.min(Math.max(1, limit), tasks.length);
  await Promise.all(Array.from({ length: workerCount }, () => worker()));
  return results;
}

// 用法：拉 100 个推荐，最多同时 8 个在途
const settled = await promisePool(
  productIds.map((id) => () => fetchReco(id)),
  8,
);
const okItems = settled.filter((s) => s.status === 'fulfilled').map((s) => s.value);
```

**评分点**：
1. worker 池模型（固定 N 个 worker 循环领任务），而不是幼稚的「每 limit 个一批等完再下一批」——批间会互相拖慢；说出这一点是区分度核心。
2. 共享游标 `next++` 领任务，结果按下标回填保证原顺序。
3. try/catch 吞单点失败，返回 settled 结构不中断整池。
4. 边界处理：limit<=0 钳制为 1、任务数为 0/小于 limit 时的行为正确。
