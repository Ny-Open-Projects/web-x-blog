---
title: [ZSM-180] 笔试：手写 queryKey 前缀匹配失效引擎（invalidateQueries 核心）
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-180：手写 queryKey 前缀匹配失效引擎（invalidateQueries 核心）
**需求**：实现 `invalidate(cacheKey, partialKey)`：1) partialKey 是 cacheKey 的前缀即视为命中（数组逐位相等；partialKey 中允许 `{}` 通配任意值，如 `['goods', {}, 'detail']`）；2) 命中的查询标记 stale 并按 options 重新调度请求；3) 精确匹配时（partialKey 与 key 完全等长且逐位相等）只失效该条；4) 返回命中列表。要求实现匹配函数 `matchKey(key, partial)` 可独立单测。

```javascript
function matchKey(key, partial) {
  if (partial.length > key.length) return false
  for (let i = 0; i < partial.length; i++) {
    const p = partial[i], k = key[i]
    if (p !== null && typeof p === 'object' &&
        Object.keys(p).length === 0) continue            // {} 通配符
    if (!deepEqual(p, k)) return false
  }
  return true
}

function deepEqual(a, b) {
  if (a === b) return true
  if (typeof a !== 'object' || typeof b !== 'object' || !a || !b) return false
  const ka = Object.keys(a), kb = Object.keys(b)
  if (ka.length !== kb.length) return false
  return ka.every(k => deepEqual(a[k], b[k]))
}

function invalidate(cache, partial) {
  const hits = cache.filter(q => matchKey(q.key, partial))
  hits.forEach(q => {
    q.stale = true                                       // 标记过期
    if (q.observers > 0) scheduleRefetch(q)              // 活跃观察者才重取
    else q.gcTimer = setTimeout(() => remove(cache, q), q.gcTime)  // 不活跃走 GC
  })
  return hits.map(q => q.key)
}

// const cache = [
//   { key: ['goods', 'list', { page: 1 }], observers: 1 },
//   { key: ['goods', 'detail', '1'], observers: 0 },
// ]
// invalidate(cache, ['goods'])        // 全域失效
// invalidate(cache, ['goods', {}])    // 第二位任意：两条全中
// invalidate(cache, ['goods', 'detail']) // 只中详情

// 评分点：
// 1. 前缀匹配语义：partial 是 key 的逐位前缀
// 2. {} 通配位支持（对象空字面量约定）
// 3. deepEqual 处理 key 中的对象参数（顺序无关比较）
// 4. stale 标记与「活跃才重取、不活跃走 GC」的行为分层
// 5. partial 比 key 长时不误判命中
```
