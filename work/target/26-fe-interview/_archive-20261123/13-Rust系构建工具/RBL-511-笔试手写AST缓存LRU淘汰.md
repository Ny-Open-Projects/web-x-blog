---
title: [RBL-511] 笔试：手写 AST 缓存 LRU 淘汰（内存预算约束）
date: 2026-11-21
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-511：手写 AST 缓存 LRU 淘汰（内存预算约束）
**需求**：按 RBL-510 的增量期缓存——实现 `createAstCache({ maxBytes })`：1) `put(id, ast, sizeBytes)`：入缓存（LRU 序），**超预算淘汰最久未用**直到预算内；2) `get(id)`：命中移到队首；3) 淘汰的模块下次访问要重 parse（调用方 callback 通知）；4) `stats()`：命中率/淘汰数/当前字节；5) 附用例：预算驱逐与重 parse 通知。

```javascript
function createAstCache({ maxBytes = 100, onEvict } = {}) {
  const cache = new Map()   // id -> { ast, size }（Map 迭代序 = LRU 序）
  let used = 0
  let hits = 0, misses = 0, evictions = 0

  function evictUntil(need) {
    while (used + need > maxBytes && cache.size) {
      const oldest = cache.keys().next().value       // 队首 = 最久未用
      const { size } = cache.get(oldest)
      cache.delete(oldest)
      used -= size
      evictions++
      onEvict?.(oldest)                              // 淘汰通知：下次访问重 parse
    }
  }

  function put(id, ast, sizeBytes) {
    if (sizeBytes > maxBytes) return false           // 单个超预算：不入缓存
    evictUntil(sizeBytes)
    cache.set(id, { ast, size: sizeBytes })
    used += sizeBytes
    return true
  }

  function get(id) {
    if (!cache.has(id)) { misses++; return null }
    const v = cache.get(id)
    cache.delete(id); cache.set(id, v)               // 移到队首
    hits++
    return v.ast
  }

  return {
    put, get,
    stats: () => ({ size: cache.size, used, maxBytes, hits, misses, evictions,
      hitRate: hits + misses ? +(hits / (hits + misses)).toFixed(2) : 0 }),
  }
}

// 用例
const evicted = []
const cache = createAstCache({ maxBytes: 100, onEvict: (id) => evicted.push(id) })
cache.put('m1', { ast: 1 }, 30)
cache.put('m2', { ast: 2 }, 30)
cache.get('m1')                                    // m1 移到队首（m2 变最旧）
cache.put('m3', { ast: 3 }, 50)                    // 需 50：驱逐 m2（30）
console.log(cache.get('m2'))                       // null（已淘汰）
console.log(evicted)                               // ['m2']
console.log(cache.get('m1'))                       // { ast: 1 }：仍命中
cache.put('m4', { ast: 4 }, 150)                   // 单个超预算：拒绝
console.log(cache.stats())
// { size: 2, used: 80, maxBytes: 100, hits: 2, misses: 1, evictions: 1, hitRate: 0.67 }
```
**评分点**：
- Map 迭代序实现 LRU（delete+set 移队首）
- 预算驱逐循环（used + need > maxBytes）
- 单个超预算拒绝（不入缓存不驱逐）
- onEvict 通知（重 parse 回调）+ 命中率统计
