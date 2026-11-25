---
title: [1217] 笔试手写：实现离线队列的重放与幂等去重
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, TanStack Query]
type: 笔试题
---

## 1217：笔试手写：实现离线队列的重放与幂等去重

**答**：实现 OfflineQueue：enqueue(op)（op = { idemKey, fn }，fn 返回 promise）；flush(networkOk)——网络恢复时按序重放；同 idemKey 的 op 只执行一次（去重表持久化语义——本实现内存 Set 模拟）；失败的 op 保留队首重试；返回 { succeeded, failed, skipped }。

```js
class OfflineQueue {
  constructor() { this.q = []; this.done = new Set(); }
  enqueue(op) { this.q.push(op); }
  async flush(networkOk = true) {
    const res = { succeeded: [], failed: [], skipped: [] };
    if (!networkOk) return res;
    const remain = [];
    for (const op of this.q) {
      if (this.done.has(op.idemKey)) { res.skipped.push(op.idemKey); continue; }
      try {
        await op.fn();
        this.done.add(op.idemKey);
        res.succeeded.push(op.idemKey);
      } catch {
        remain.push(op);                     // 失败保留队首语义（按序重试）
        res.failed.push(op.idemKey);
      }
    }
    this.q = remain;
    return res;
  }
}
const q = new OfflineQueue();
const calls = [];
q.enqueue({ idemKey: 'k1', fn: async () => calls.push('k1') });
q.enqueue({ idemKey: 'k1', fn: async () => calls.push('k1-dup') });  // 重复
q.enqueue({ idemKey: 'k2', fn: async () => { throw new Error('x'); } });
console.log(await q.flush(true), calls);   // skipped k1-dup；failed k2；calls ['k1']
```

**评分点**：
- idemKey 去重（at-least-once 语义的客户端补偿）
- 失败保留重放（remain 重组队列——按序语义）
- skipped 与 failed 分列（可观测）
- 能讨论：done 表的持久化（刷新后仍去重）、服务端幂等与客户端去重的双层防线

