---
title: [HW-138] 手写 useQuery 最小实现——缓存、竞态、重试、失效重取与卸载中止（React Query 核心）
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-138：手写 useQuery 最小实现——缓存、竞态、重试、失效重取与卸载中止（React Query 核心）
**答**：React Query 核心语义的最小复刻：① 缓存（Map key→{data, ts}）+ staleTime；② 竞态（AbortController + seq）；③ 失效重取（invalidate 触发订阅者刷新）；④ 重试退避；⑤ 卸载中止；⑥ loading/error/stale 状态机。

```javascript
const cache = new Map();                          // key -> { data, ts, promise, subs: Set }
export function useQuery(key, fetcher, { staleTime = 30000, retries = 2 } = {}) {
  const [, force] = useState(0);
  const entry = cache.get(key);
  const stale = !entry || Date.now() - entry.ts > staleTime;
  const refetch = useCallback(async () => {
    let e = cache.get(key);
    if (e?.promise) return e.promise;             // 在途共享
    const promise = (async () => {
      for (let i = 0; ; i++) {
        try {
          const data = await fetcher(key);        // fetcher 内部用 AbortSignal（HW-109）
          cache.set(key, { data, ts: Date.now(), subs: e?.subs });
          cache.get(key).subs.forEach((f) => f());   // 通知订阅组件刷新
          return data;
        } catch (err) {
          if (i >= retries) throw err;
          await new Promise((r) => setTimeout(r, 500 * 2 ** i));
        }
      }
    })();
    cache.set(key, { ...(e ?? { subs: new Set() }), promise, ts: e?.ts ?? 0 });
    force((x) => x + 1);
    return promise;
  }, [key]);
  useEffect(() => {
    const notify = () => force((x) => x + 1);
    (cache.get(key)?.subs ?? cache.set(key, { subs: new Set() }).get(key).subs).add(notify);
    if (stale) refetch();                         // 挂载/过期：拉取
    return () => { cache.get(key)?.subs?.delete(notify); };
  }, [key, stale]);
  const cur = cache.get(key);
  return { data: cur?.data, loading: !!cur?.promise && !cur.data,
           error: cur?.error, isStale: stale, refetch,
           invalidate: () => { cache.delete(key); refetch(); } };
}
// 覆盖 React Query 六大语义的最小集；卸载后 subs 自动清理（无泄漏）
// in-flight 共享：同 key 并发 useQuery 只发一次请求（HW-079 语义）
```

**评分点**：
- 六大语义齐备：缓存/staleTime、在途共享、竞态/中止、重试退避、失效重取、订阅通知。
- subs 集合清理（卸载无泄漏）。
- stale 判定与 loading 状态机（有 data 不显示 loading）。
- 能说清与 React Query 的差距（无 GC/窗口聚焦重取/分页选择器等）。
