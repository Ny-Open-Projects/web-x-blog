---
title: [ZSM-479] 笔试：手写基于 WeakRef 的资源态缓存
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-479：手写基于 WeakRef 的资源态缓存
**需求**：实现 `createWeakCache(loader)`：1) `get(key)`：命中（WeakRef 存活）直接返回；未命中/已被 GC 调 loader 重建；2) `cleanup()`：遍历清除 deref() === undefined 的条目（GC 后墓碑清理）；3) 定期 cleanup（interval 可配）+ stop 清理；4) 大资源（图片位图/WebGL 纹理）场景说明为什么 WeakRef 合适（GC 压力由引擎管理，不用手动 LRU）；5) `size()` 返回存活条目数（清理后统计）。

```javascript
export function createWeakCache(loader, { cleanupIntervalMs = 60_000 } = {}) {
  const cache = new Map()      // key → WeakRef
  const inFlight = new Map()   // key → Promise（防并发重复加载）
  let timer = null

  function cleanup() {
    let alive = 0
    for (const [k, ref] of cache) {
      if (ref.deref() === undefined) cache.delete(k)          // GC 墓碑清理
      else alive++
    }
    return alive
  }

  timer = setInterval(() => cleanup(), cleanupIntervalMs)

  async function get(key) {
    const ref = cache.get(key)
    const hit = ref?.deref()
    if (hit) return hit
    if (inFlight.has(key)) return inFlight.get(key)          // 并发去重
    const p = loader(key).then((v) => {
      cache.set(key, new WeakRef(v))
      inFlight.delete(key)
      return v
    }).catch((e) => { inFlight.delete(key); throw e })
    inFlight.set(key, p)
    return p
  }

  return {
    get,
    cleanup,
    size: () => cleanup(),
    stop: () => clearInterval(timer),
  }
}
```
**评分点**：
- WeakRef 命中判定（deref() 判活）+ GC 后重建语义
- cleanup 墓碑清理（Map 里的死 WeakRef 本身也是泄漏点——常被忽略）
- inFlight 并发去重（loader 重复加载防护）
- 适用边界说明（大资源弱缓存 vs 必须持久的小状态不适用——Weak 语义无保证）
