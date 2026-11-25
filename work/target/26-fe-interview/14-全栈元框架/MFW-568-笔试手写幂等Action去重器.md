---
title: [MFW-568] 笔试：手写幂等 Action 去重器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-568：笔试：手写幂等 Action 去重器

**答**：实现 `withIdempotency(fn, { store, ttlMs })`。store 注入（Map 模拟 Redis：`get(key) / set(key, value, ttl)`）。fn: `(args) => Promise<result>`。规则：1) 首次调用：执行 fn，结果存 store（含 in-flight 标记——并发同 key：第二个调用等待首个的 Promise（单飞 RBL-738）而非重复执行）；2) 完成后：结果缓存 ttlMs（重放返回缓存值 + replayed: true）；3) fn 抛错：错误不缓存（重试允许）——in-flight 清除；4) 返回包装函数 `wrapped(args, idemKey)`。边界：同 key 并发 3 个调用只执行 1 次；TTL 过期后重放 = 重新执行。

```javascript
function withIdempotency(fn, { store = new Map(), ttlMs = 60000, now = Date.now } = {}) {
  return async (args, idemKey) => {
    if (!idemKey) return fn(args);                       // 无键不幂等（透传）
    const key = `idem:${idemKey}`;
    const existing = store.get(key);
    if (existing) {
      if (existing.promise) return existing.promise;     // in-flight：共享 Promise（单飞）
      if (now() - existing.doneAt < ttlMs)
        return { ...existing.result, replayed: true };   // TTL 内重放
      store.delete(key);                                 // 过期重执行
    }
    const promise = (async () => {
      try {
        const result = await fn(args);
        store.set(key, { result, doneAt: now() });       // 完成缓存
        return result;
      } catch (e) {
        store.delete(key);                               // 错误不缓存
        throw e;
      } finally {
        // in-flight 标记由 promise 本身承载：完成后 store 替换为结果态
      }
    })();
    store.set(key, { promise });
    return promise;
  };
}

// 自测
const store = new Map(); let calls = 0;
const placeOrder = withIdempotency(async (args) => {
  calls++;
  await sleep(20);
  return { orderId: 'o-' + calls, sku: args.sku };
}, { store, ttlMs: 100 });

// 并发同 key：单飞
const r1 = placeOrder({ sku: 'A' }, 'idem-1');
const r2 = placeOrder({ sku: 'A' }, 'idem-1');
const r3 = placeOrder({ sku: 'A' }, 'idem-1');
const [a, b, c] = await Promise.all([r1, r2, r3]);
console.log(calls === 1);                                // 只执行一次
console.log(a.orderId === b.orderId && b.orderId === c.orderId);

// TTL 内重放
const r4 = await placeOrder({ sku: 'A' }, 'idem-1');
console.log(r4.replayed === true && r4.orderId === a.orderId);

// 不同 key 独立执行
await placeOrder({ sku: 'B' }, 'idem-2');
console.log(calls === 2);

// 错误不缓存（可重试）
const failing = withIdempotency(async () => { throw new Error('db'); }, { store });
let e1, e2;
try { await failing({}, 'idem-3'); } catch (e) { e1 = e; }
try { await failing({}, 'idem-3'); } catch (e) { e2 = e; }
console.log(e1.message === 'db' && e2.message === 'db'); // 两次都真执行（可重试）
```

**评分点**：
- 并发单飞（in-flight Promise 共享——不只是结果缓存，执行中也合并）
- TTL 重放语义（replayed 标记——调用方可区分）；错误不缓存（可重试性 RBL-856）
- 无键透传（幂等是可选契约）；边界全覆盖
- 能说清「Action 静默重放 × 非幂等 = 资损——幂等键是 Action 架构的必答题」属于加分
