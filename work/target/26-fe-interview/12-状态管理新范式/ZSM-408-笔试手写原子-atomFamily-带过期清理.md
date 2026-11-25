---
title: [ZSM-408] 笔试：手写 atomFamily（参数化 atom + LRU 清理）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-408：手写 atomFamily（参数化 atom + LRU 清理）
**答**：实现 `createAtomFamily(factory, { max = 100 })`：1) `get(param)` 返回该参数的 atom 实例（同参数复用）；2) LRU 淘汰：超过 max 时清除最久未访问的 atom（连同其状态）；3) `remove(param)` 主动清除；4) 访问（get）刷新 LRU 顺序；5) 正在被订阅的 atom 不淘汰（有活引用保护）。

```javascript
export function createAtomFamily(factory, { max = 100 } = {}) {
  const cache = new Map()   // param → { atom, subs: number }

  function get(param) {
    let entry = cache.get(param)
    if (entry) { cache.delete(param); cache.set(param, entry) }   // 访问刷新 LRU
    else {
      if (cache.size >= max) {
        for (const [p, e] of cache) {                             // Map 保序：最旧在前
          if (e.subs > 0) continue                                // 活引用保护
          cache.delete(p); break
        }
      }
      entry = { atom: factory(param), subs: 0 }
      cache.set(param, entry)
    }
    return entry.atom
  }

  function track(param, on) {                                     // 订阅计数（活引用）
    const e = cache.get(param)
    if (e) e.subs += on ? 1 : -1
  }

  return {
    get, remove: (param) => cache.get(param)?.subs === 0 && cache.delete(param),
    withTracking: (param) => { const a = get(param); track(param, true)
      return [a, () => track(param, false)] },
  }
}
```
**评分点**：
- LRU 用 Map 插入序实现（delete+set 刷新），淘汰从最旧端开始
- 活引用保护：被订阅（subs>0）的 atom 跳过淘汰（否则订阅悬空）
- 同参数 get 复用同一实例（家族语义核心）
- remove 对活跃 atom 拒绝删除；subs 计数对称（订阅/退订配对）
