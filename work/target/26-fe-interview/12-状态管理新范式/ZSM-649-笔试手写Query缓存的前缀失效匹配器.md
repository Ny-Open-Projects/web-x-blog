---
title: [ZSM-649] 笔试：手写 Query 缓存的前缀失效匹配器（含 hashKey 等价性）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-649：手写 Query 缓存的前缀失效匹配器（含 hashKey 等价性）
**答**：实现 `createCacheMatcher()`：1) `hashKey(key)`：对象键排序序列化（与 TanStack 语义一致：`{a,b}` 与 `{b,a}` 同 hash）；2) `matchPrefix(cachedKeys, prefix)`：前缀匹配——prefix 是数组，cachedKey 数组前 N 位与 prefix 相等即命中（支持对象元素的深度等价）；3) `matchPredicate(cache, predicate)`：函数过滤（按 data 内容判定）；4) `invalidate(cache, filters)`：返回命中条目并标脏；5) 附用例：验证键序无关命中与嵌套对象前缀匹配。

```javascript
// hashKey：对象键排序（等价性）
function hashKey(key) {
  return JSON.stringify(key, (_, val) =>
    val && typeof val === 'object' && !Array.isArray(val)
      ? Object.keys(val).sort().reduce((acc, k) => ((acc[k] = val[k]), acc), {})
      : val
  )
}

// 深度相等（用于对象元素比较）
function deepEqual(a, b) {
  return JSON.stringify(sortish(a)) === JSON.stringify(sortish(b))
}
function sortish(v) {
  if (Array.isArray(v)) return v.map(sortish)
  if (v && typeof v === 'object') {
    return Object.keys(v).sort().reduce((acc, k) => ((acc[k] = sortish(v[k])), acc), {})
  }
  return v
}

// 前缀匹配
function matchPrefix(cachedKeys, prefix) {
  return cachedKeys.filter((cached) => {
    if (prefix.length > cached.length) return false
    for (let i = 0; i < prefix.length; i++) {
      const p = prefix[i], c = cached[i]
      if (p !== undefined && !deepEqual(p, c)) return false   // 逐位等价
    }
    return true
  })
}

// predicate 过滤 + invalidate
function invalidate(cache, { queryKey, predicate } = {}) {
  const invalidated = []
  for (const [key, entry] of cache) {
    const byKey = queryKey ? matchPrefix([key], queryKey).length > 0 : true
    const byPred = predicate ? predicate({ key, data: entry.data }) : true
    if (byKey && byPred) {
      entry.isInvalidated = true
      invalidated.push(key)
    }
  }
  return invalidated
}

// 用例
const cache = new Map()
cache.set(['todos', 'list', { page: 1 }], { data: [1], isInvalidated: false })
cache.set(['todos', 'list', { page: 2 }], { data: [2], isInvalidated: false })
cache.set(['todos', 'detail', 7], { data: {}, isInvalidated: false })
cache.set(['users', 'list'], { data: [], isInvalidated: false })

// 键序无关：{ page: 1 } 与 { ... } 等价命中
console.log(matchPrefix([...cache.keys()], ['todos', 'list', { page: 1 }]))
// [['todos','list',{page:1}]]
console.log(matchPrefix([...cache.keys()], ['todos']))          // 3 条 todos
console.log(invalidate(cache, { queryKey: ['todos', 'list'] })) // 2 条命中并标脏
console.log(invalidate(cache, { predicate: ({ data }) => Array.isArray(data) && data.length === 0 }))
// ['users','list']
```
**评分点**：
- hashKey 对象键排序（键序无关的缓存等价性）
- 前缀匹配逐位深度等价（对象元素也能匹配）
- predicate 与 queryKey 过滤组合（AND 语义）
- invalidate 标脏返回命中清单（可观测）
