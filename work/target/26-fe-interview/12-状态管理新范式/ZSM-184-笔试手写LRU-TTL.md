---
title: [ZSM-184] 笔试：手写带 TTL 的 LRU 缓存（缓存层的容量与时效双控制）
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-184：手写带 TTL 的 LRU 缓存（缓存层的容量与时效双控制）
**需求**：实现 `TTLCache({ max, ttl })`：1) get 命中要把条目移到「最近使用」端；2) set 超过 max 时淘汰最久未用条目；3) 每个条目独立 TTL，过期视为未命中并删除（惰性过期）；4) 提供 peek（读但不影响 LRU 顺序）与 keys()；5) 全部操作 O(1)。不要求用现成 LinkedMap 类，可用 Map 的插入序性质实现。

```javascript
export class TTLCache {
  constructor({ max = 100, ttl = 60_000 } = {}) {
    this.max = max; this.ttl = ttl
    this.map = new Map()              // Map 保持插入序：队尾是最新
  }

  get(key) {
    const item = this.map.get(key)
    if (!item) return undefined
    if (Date.now() > item.expire) {   // 惰性过期：访问时才发现
      this.map.delete(key)
      return undefined
    }
    this.map.delete(key)              // 重插到队尾 = 最近使用
    this.map.set(key, item)
    return item.value
  }

  set(key, value, ttl = this.ttl) {
    if (this.map.has(key)) this.map.delete(key)
    this.map.set(key, { value, expire: Date.now() + ttl })
    if (this.map.size > this.max) {   // 超容淘汰队首（最久未用）
      const oldest = this.map.keys().next().value
      this.map.delete(oldest)
    }
  }

  peek(key) {                         // 读但不改 LRU 顺序
    const item = this.map.get(key)
    if (!item || Date.now() > item.expire) return undefined
    return item.value
  }

  keys() {
    const now = Date.now()
    return [...this.map].filter(([, i]) => i.expire > now).map(([k]) => k)
  }
}

// 评分点：
// 1. Map 插入序模拟 LRU：get 删除重插，set 淘汰队首
// 2. 惰性过期：读时校验 expire，不需要定时器
// 3. set 已存在 key 先删再插保证最新位置
// 4. peek 不影响使用顺序的语义差异
// 5. 全部 O(1)（Map 的 get/set/delete/迭代首元素均 O(1)）
```
