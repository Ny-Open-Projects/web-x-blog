---
title: [1124] 笔试手写：实现 useCachedMutation
date: 2026-11-22
categories: [状态管理新范式]
tags: [前端面试, 笔试题, Mutation]
type: 笔试题
---

## 1124：笔试手写：实现 useCachedMutation

**答**：实现 createCachedMutation(queryCache, invalidator)：mutate(key, payload) 先乐观写 queryCache.set(key, mergeFn(payload))（若 key 已有缓存），然后提交 submit(payload)；成功后 invalidator(keys) 精准失效关联查询（而非全量刷新）；失败回滚缓存到快照并返回 error。返回 { mutate, undo(opId) }。

```js
function createCachedMutation(queryCache, submit, invalidator) {
  const snapshots = new Map();
  return {
    async mutate(key, payload, mergeFn, relatedKeys = []) {
      const existed = queryCache.has(key);
      snapshots.set(key, existed ? structuredClone(queryCache.get(key)) : null); // 快照
      if (existed) queryCache.set(key, mergeFn(queryCache.get(key), payload)); // 乐观写
      try {
        const res = await submit(payload);
        invalidator(relatedKeys); // 精准失效关联（不全量刷新）
        snapshots.delete(key);
        return { ok: true, res };
      } catch (e) {
        // 回滚
        if (existed) queryCache.set(key, snapshots.get(key));
        else queryCache.delete(key);
        snapshots.delete(key);
        return { ok: false, error: String(e) };
      }
    },
  };
}
```

**评分点**：
- 乐观写前置 + 快照回滚（与 ZSM-098/122 同思想，聚焦缓存联动）
- invalidator 只失效 relatedKeys（失效粒度纪律）
- 回滚覆盖「原本无缓存」的分支（delete 而非 set null）
- 能讨论：与 TanStack onMutate 回调体系的对应关系
