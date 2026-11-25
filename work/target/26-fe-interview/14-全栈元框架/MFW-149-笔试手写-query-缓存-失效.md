---
title: [MFW-149] 笔试：手写一个带失效的 Query 缓存层（TanStack Query 核心简化）
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-149：笔试：手写一个带失效的 Query 缓存层（TanStack Query 核心简化）
**答**：实现 `QueryClient` 的核心：① `fetchQuery(key, fn, { staleTime })`：缓存命中且未过期直接返回；② 过期（stale）后重新执行 fn，期间并发调用**共享同一 pending**（不重复请求）；③ `invalidateQuery(prefix)`：按 key 前缀失效（下次 fetch 强制重跑）；④ 同 key 不同参数序列化判等；⑤ staleTime=0 表示总是 stale。

```ts
type QueryKey = readonly unknown[];

function hashKey(key: QueryKey): string {
  return JSON.stringify(key, (_k, v) => (typeof v === 'object' && v !== null
    ? Object.keys(v as object).sort().reduce((acc: Record<string, unknown>, k) => {
        acc[k] = (v as Record<string, unknown>)[k]; return acc;
      }, {}) // 对象 key 排序，保证 {a:1,b:2} 与 {b:2,a:1} 同 key
    : v));
}

interface Entry {
  data: unknown;
  fetchedAt: number;
  promise?: Promise<unknown>;
  invalidated?: boolean;
}

export class QueryClient {
  private cache = new Map<string, Entry>();

  constructor(private staleTime = 30_000) {}

  isStale(entry: Entry, staleTime: number): boolean {
    if (entry.invalidated) return true;               // 手动失效强制 stale
    return Date.now() - entry.fetchedAt > staleTime;   // 0 => 总是 stale
  }

  async fetchQuery<T>(
    key: QueryKey,
    fn: () => Promise<T>,
    opts: { staleTime?: number } = {},
  ): Promise<T> {
    const hash = hashKey(key);
    const st = opts.staleTime ?? this.staleTime;
    const entry = this.cache.get(hash);

    // 1. 新鲜数据直接返回
    if (entry && entry.promise === undefined && !this.isStale(entry, st)) {
      return entry.data as T;
    }

    // 2. in-flight 共享：并发调用拿到同一个 pending
    if (entry?.promise) return entry.promise as Promise<T>;

    // 3. 执行取数：记录 promise 供并发去重
    const promise = fn()
      .then((data) => {
        this.cache.set(hash, { data, fetchedAt: Date.now() }); // 成功：写入缓存清 promise
        return data;
      })
      .catch((err) => {
        // 失败：清掉 pending 让下次重试，但保留旧数据（stale-while-error）
        const old = this.cache.get(hash);
        if (old) this.cache.set(hash, { ...old, promise: undefined });
        else this.cache.delete(hash);
        throw err;
      });

    if (entry) this.cache.set(hash, { ...entry, promise }); else this.cache.set(hash, { data: undefined, fetchedAt: 0, promise });
    return promise as Promise<T>;
  }

  // 4. 前缀失效：['products'] 失效 ['products', 'p1'] 等
  invalidate(prefix: QueryKey): void {
    const p = hashKey(prefix);
    for (const [hash, entry] of this.cache) {
      if (hash.startsWith(p.slice(0, -1))) { // 前缀匹配（去掉 JSON 尾 ']'）
        entry.invalidated = true;
      }
    }
  }

  getQueryData<T>(key: QueryKey): T | undefined {
    return this.cache.get(hashKey(key))?.data as T | undefined;
  }
}
```

**评分点**：
1. staleTime 语义正确：0 总是 stale，过期判断用 fetchedAt 差值。
2. 并发去重：pending Promise 共享，成功/失败都要清理 promise 字段。
3. 失败保留旧数据（stale-while-error 思想），下次可重试。
4. invalidate 是前缀匹配并标记 invalidated 而非删除（保留旧值展示）。
5. hashKey 对对象参数做 key 排序判等——参数顺序不影响缓存命中。
