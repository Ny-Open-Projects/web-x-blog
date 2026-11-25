---
title: [V3-406] 笔试：手写 keep-alive 核心（LRU 缓存 + include/exclude）
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-406：笔试：手写 keep-alive 核心（LRU 缓存 + include/exclude）
**答**：用 Map 实现组件实例 LRU 缓存：`keepAliveCache(max)` 提供 get(key, factory) 与 prune；命中时移到「最新」；超容量淘汰最旧（先销毁实例再删）；支持 include 列表过滤。

```javascript
function keepAliveCache(max = 10) {
  const cache = new Map() // Map 迭代序 = 插入序，最新在最后
  return {
    get(key, factory) {
      if (cache.has(key)) {
        const inst = cache.get(key)
        cache.delete(key); cache.set(key, inst) // 刷新为最新
        return inst
      }
      const inst = factory()
      cache.set(key, inst)
      this.prune()
      return inst
    },
    prune() {
      while (cache.size > max) {
        const oldestKey = cache.keys().next().value
        const oldest = cache.get(oldestKey)
        oldest.unmount?.() // 先销毁，防止副作用残留
        cache.delete(oldestKey)
      }
    },
    clear() { cache.forEach(i => i.unmount?.()); cache.clear() },
    has: (k) => cache.has(k),
    size: () => cache.size
  }
}
```
**评分点**：
- Map 利用插入序实现 LRU（delete+set 刷新最新）。
- 淘汰时先 unmount 再删除（防副作用/内存泄漏）。
- prune 用 while 处理 max 突降场景。
- include 过滤可在 get 前判断（说出即可）。
