---
title: [MFW-402] 笔试：手写请求级 DataCache 读路径（L1→L2→L3 串行）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-402：三级读路径
**需求**：实现 `createDomainReader({ mem, ttlMs = 30_000 })`：1) L1 请求内 Map（AsyncLocalStorage store——同请求同 key 单飞）；2) L2 进程内 LRU（跨请求，TTL 内复用；容量 500）；3) L3 fetcher；4) 读到 L2/L3 回填上层；5) negCache：L3 null/错误 30s（穿透防护——RBL-426 同款）；6) invalidate(domain) 清 L2 对应前缀+L1 全清。

```javascript
import { AsyncLocalStorage } from 'node:async_local_storage'
const als = new AsyncLocalStorage()      // store: Map

function withReq(fn) { const m = new Map(); return als.run(m, fn) }

export function createDomainReader(source, { l2 = lruFactory(500), negMs = 30_000 } = {}) {
  const neg = new Map()
  return {
    read: (key, fetcher) => withReq(async () => {
      const l1 = als.getStore()
      if (!l1.has(key)) {
        const l2hit = l2.get(key)
        if (l2hit !== undefined) { l1.set(key, l2hit); return l2hit }
        if (Date.now() - (neg.get(key)?.t ?? -9e9) < negMs) return null       // 负缓存
        try { const v = await fetcher()
          l1.set(key, v); l2.set(key, v); return v
        } catch (e) { neg.set(key, { t: Date.now() }); throw e }
      }
      return l1.get(key)
    }),
    invalidate: (prefix) => { l2.clearPrefix(prefix); als.destroy?.() /* 新请求即净 */ },
    // 单飞已内建：同请求并发同 key 共享同一 L3 Promise（Map 存 Promise 本身）
  }
}
```
**评分点**：
- L1 存 Promise 而非值（同请求并发同 key 天然单飞——不重复打 L3）
- L2 TTL+容量双约束；回填只向更近层（不跨层污染）
- 负缓存短 TTL（新数据创建后生效延迟可控）
- invalidate 分层清（L2 前缀 + 请求级随生命周期自然净）
