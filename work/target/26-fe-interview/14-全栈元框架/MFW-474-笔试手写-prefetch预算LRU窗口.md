---
title: [MFW-474] 笔试：手写 prefetch 预算 LRU 窗口管理器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-474：prefetch 预算 LRU 窗口管理器
**需求**：实现 `createPrefetchBudget({ bytes, entries })`：1) `request(href, size)`：按 RSC payload 估算字节数准入；超总预算时按 LRU 驱逐最久未"访问"（request 或 hover 触碰即刷新）的条目；2) 同 href 重复请求直接命中（命中即刷新 LRU 位）；3) 条目数上限 entries 同样生效，双约束先触发者生效；4) `stats()` 返回 { used, entries, evicted: n }——低端机（navigator.deviceMemory 低）可调小预算（构造参数体现）。

```javascript
export function createPrefetchBudget({ bytes = 2_000_000, entries = 50 } = {}) {
  const map = new Map() // href -> size（Map 迭代序即 LRU 序）
  let evicted = 0

  function touch(href, size) {
    if (map.has(href)) { const s = map.get(href); map.delete(href); map.set(href, s); return true }
    return admit(href, size)
  }

  function admit(href, size) {
    while (map.size >= entries) dropOldest('entries')
    while (used() + size > bytes && map.size) dropOldest('bytes')
    if (size > bytes) return false // 单条超预算直接拒
    map.set(href, size)
    return true
  }

  function dropOldest(reason) {
    const oldest = map.keys().next().value
    map.delete(oldest); evicted++
  }

  function used() { return [...map.values()].reduce((a, b) => a + b, 0) }

  return {
    request: touch,
    has: href => map.has(href),
    stats: () => ({ used: used(), entries: map.size, evicted }),
  }
}
```

**评分点**：
- Map 迭代序实现 LRU（get 后 delete+set 刷新位——JS 惯用解）
- 字节与条目双约束（只有条目数会漏 payload 巨大的页面）
- 单条超预算拒绝（一条 3MB payload 驱逐全部预取）
- evicted/used 可观测（预取策略要可调参验证）
