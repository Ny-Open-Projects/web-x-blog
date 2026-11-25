---
title: [R19-423] 笔试：手写 React Query 核心缓存
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 数据流]
type: 笔试题
---

## R19-423：笔试：手写 React Query 核心

**答**：实现最小 QueryClient：① 缓存 Map<queryKey, { data, error, status, dataUpdatedAt }>；② fetchQuery：去重（同 key 在途共享 promise）、TTL 过期重取、成功/失败状态机；③ useQuery hook：挂载即取（stale 触发）、窗口聚焦重取（focus 事件 + staleTime）、竞态守卫；④ invalidateQueries(key)：标记 stale 并触发活跃观察者重取；⑤ GC：无观察者的缓存条目 5 分钟后清理。写出实现。

```javascript
class QueryClient {
  #cache = new Map();
  constructor({ staleTime = 30_000, gcTime = 5 * 60_000 } = {}) { Object.assign(this, { staleTime, gcTime }); }
  #entry(key) {
    const k = JSON.stringify(key);
    if (!this.#cache.has(k)) this.#cache.set(k, { status: 'idle', data: null, error: null, dataUpdatedAt: 0, promise: null, subs: new Set(), gc: null });
    return this.#cache.get(k);
  }
  async fetchQuery(key, fn) {
    const e = this.#entry(key);
    const fresh = Date.now() - e.dataUpdatedAt < this.staleTime;
    if (e.status === 'success' && fresh) return e.data;      // 新鲜直接返回
    if (e.promise) return e.promise;                          // 在途去重
    e.status = 'pending';
    e.promise = fn().then((data) => {
      e.data = data; e.status = 'success'; e.dataUpdatedAt = Date.now(); e.promise = null;
      e.subs.forEach(cb => cb());
      return data;
    }).catch((err) => {
      e.error = err; e.status = 'error'; e.promise = null;
      e.subs.forEach(cb => cb());
      throw err;
    });
    return e.promise;
  }
  invalidateQueries(key) {
    const e = this.#entry(key);
    e.dataUpdatedAt = 0;                                      // 标记 stale
    if (e.subs.size) this.fetchQuery(key, e.fetcher);         // 活跃观察者重取
    else this.#scheduleGC(key);
  }
  #scheduleGC(key) {
    clearTimeout(this.#entry(key).gc);
    this.#entry(key).gc = setTimeout(() => {
      if (!this.#entry(key).subs.size) this.#cache.delete(JSON.stringify(key));
    }, this.gcTime);
  }
}
function useQuery(key, fn, client) {
  const e = client.#entry(key);
  const [, force] = useReducer(c => c + 1, 0);
  useEffect(() => {
    e.subs.add(force);
    e.fetcher = fn;
    client.fetchQuery(key, fn);
    const onFocus = () => { if (Date.now() - e.dataUpdatedAt > client.staleTime) client.fetchQuery(key, fn); };
    window.addEventListener('focus', onFocus);
    return () => { e.subs.delete(force); window.removeEventListener('focus', onFocus); client.#scheduleGC(key); };
  }, [JSON.stringify(key)]);
  return { data: e.data, error: e.error, status: e.status };
}
```

**评分点**：
- 在途去重（promise 共享）与 TTL 新鲜度判定
- invalidate 的「标记 stale + 活跃观察者重取」语义
- 窗口聚焦重取与卸载 GC 调度
- 订阅者集合驱动组件更新
