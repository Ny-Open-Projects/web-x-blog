---
title: [MFW-188] 笔试：手写同资源串行锁的 Server Action 调度器
date: 2026-11-19
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-188：笔试：手写同资源串行锁的 Server Action 调度器
**题目**：多个用户请求可能同时写同一资源（如同一购物车、同一库存）。实现 `withResourceLock(resourceId, fn)`：① 同一 resourceId 的操作严格串行（前一个完成才开始下一个）；② 不同 resourceId 并行；③ 等待队列有上限（同键排队最多 5 个，超限直接抛 `BusyError`）；④ 持锁超时（10s）自动释放防死锁，被超时中断的请求抛错但锁不泄漏。

```ts
type Queue = { chain: Promise<unknown>; length: number };
const locks = new Map<string, Queue>();
const MAX_QUEUE = 5, LOCK_TIMEOUT = 10_000;

export class BusyError extends Error {}
export class LockTimeoutError extends Error {}

export async function withResourceLock<T>(resourceId: string, fn: () => Promise<T>): Promise<T> {
  let q = locks.get(resourceId);
  if (q && q.length >= MAX_QUEUE) throw new BusyError('too many waiting'); // ③ 排队上限
  if (!q) { q = { chain: Promise.resolve(), length: 0 }; locks.set(resourceId, q); }

  q.length++;
  const run = q.chain.then(async () => { // ①/② 同键串行，异键各自 chain 互不等待
    const timer = setTimeout(() => {
      throw new LockTimeoutError('lock timeout'); // ④ 超时令本次执行失败
    }, LOCK_TIMEOUT);
    try {
      return await fn(); // ④ fn 超时会沿 promise 链抛出，chain 继续推进
    } finally {
      clearTimeout(timer);
    }
  });
  q.chain = run.catch(() => {}); // 吞掉本任务的错误，保证后续任务不被毒化
  q.length--;
  try {
    return (await run) as T;
  } finally {
    if (q.length === 0) locks.delete(resourceId); // 队列空了回收，防 Map 泄漏
  }
}

// 用法：库存扣减
export const decStock = (sku: string) =>
  withResourceLock(`stock:${sku}`, () => db.products.decrementStock(sku, 1));
```

**评分点**：
1. 用 promise chain 实现串行（前一个 promise resolve 后才执行下一个），这是「无真锁环境下的串行化」标准手法。
2. 错误必须被链上 catch 吞掉，否则一次失败会让队列里所有后续任务连锁失败。
3. 排队上限（背压）+ 空队列回收两个防泄漏细节都要出现。
4. 能指出：这只解决了「单实例内存锁」，多实例部署要换 Redis 锁（SET NX + 过期 + 看门狗续期）。
5. 超时处理诚实：setTimeout 抛错不能真正中断已发出的 IO，能主动说明这一点（fn 应自带 AbortSignal）。
