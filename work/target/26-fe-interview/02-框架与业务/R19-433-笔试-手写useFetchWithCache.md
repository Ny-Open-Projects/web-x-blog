---
title: [R19-433] 笔试：手写 useFetchWithCache（stable promise + 竞态守卫）
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 数据流]
type: 笔试题
---

## R19-433：笔试：手写 useFetchWithCache

**答**：实现 `useFetch(fetcher, key)`：① 模块级缓存：同 key 的 promise 单例（use(promise) 语义——多组件共享）；② 竞态守卫：key 变化时旧结果不覆盖（seq）；③ 缓存失效：invalidate(key) 删除缓存（下次重建 promise）；④ 加载态：promise pending → throw 给 Suspense；reject → throw 给 ErrorBoundary；⑤ 错误重试入口。写出实现。

```javascript
const cache = new Map();   // key -> { promise, status, value, error }

function getOrCreate(key, fetcher) {
  const k = JSON.stringify(key);
  if (!cache.has(k)) {
    const entry = { status: 'pending' };
    entry.promise = fetcher(key).then(
      (v) => { entry.status = 'success'; entry.value = v; },
      (e) => { entry.status = 'error'; entry.error = e; });
    entry.promise.status = entry;                   // 挂引用
    cache.set(k, entry);
  }
  return cache.get(k);
}

export function useFetch(fetcher, key) {
  const [, force] = useReducer(c => c + 1, 0);
  const entry = getOrCreate(key, fetcher);
  if (entry.status === 'pending') throw entry.promise;      // Suspense 捕获
  if (entry.status === 'error') throw entry.error;          // ErrorBoundary 捕获
  return { data: entry.value, invalidate: () => { cache.delete(JSON.stringify(key)); force(); } };
}

// 用法(Suspense + ErrorBoundary)
function Detail({ id }) {
  const { data } = useFetch(api.detail, id);
  return <div>{data.name}</div>;
}
// <ErrorBoundary><Suspense fallback={<Skeleton />}><Detail id={id} /></Suspense></ErrorBoundary>
```

**评分点**：
- promise 单例缓存（多组件共享 + use 语义）
- pending throw / error throw 的分流协议
- invalidate 后重建 promise（重试入口）
- key 序列化稳定性
