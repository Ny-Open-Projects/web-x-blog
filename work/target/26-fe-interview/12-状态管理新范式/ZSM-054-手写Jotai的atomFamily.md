---
title: [ZSM-054] 笔试：手写 Jotai 的 atomFamily（带缓存与 TTL 清理）
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-054：手写 Jotai 的 atomFamily（带缓存与 TTL 清理）

**答**：
- 实现 `atomFamily(param => atom(...))`：同参数返回同一 atom（缓存复用），不同参数各自独立。
- 支持 `family.remove(param)` 释放实例，防长列表累积内存。
- 进阶：给缓存加 TTL（如 5 分钟未访问自动清理），避免手动 remove 遗漏。

```javascript
export function atomFamily(initialize, ttl = 5 * 60_000) {
  const cache = new Map() // param → { atom, lastUsed }
  const get = param => {
    const key = typeof param === 'object' ? JSON.stringify(param) : param // 引用不稳定时序列化
    let entry = cache.get(key)
    if (!entry) {
      entry = { atom: initialize(param), lastUsed: Date.now() }
      cache.set(key, entry)
    } else {
      entry.lastUsed = Date.now() // 触碰刷新 TTL
    }
    return entry.atom
  }
  get.remove = param => {
    const key = typeof param === 'object' ? JSON.stringify(param) : param
    cache.delete(key)
  }
  // TTL 清扫：低频定时器 + 时间戳惰性判断
  get.sweep = () => {
    const now = Date.now()
    for (const [k, e] of cache) if (now - e.lastUsed > ttl) cache.delete(k)
  }
  setInterval(() => get.sweep(), 60_000)
  return get
}

// 用法：每个会话一个未读数 atom
const unreadFamily = atomFamily(id => atom(0))
const unreadOf = id => unreadFamily(id)
```

**评分点**：
- 同参复用、异参隔离；对象参数做了稳定 key 处理（JSON.stringify 或 WeakMap 双轨）。
- remove/sweep 提供释放通道，能说出内存泄漏场景。
- TTL 用「lastUsed 时间戳 + 惰性/定时清扫」，而非每访问都扫描。
- 能指出：缓存 atom 本身无订阅者才可安全清理（答出加满分）。
