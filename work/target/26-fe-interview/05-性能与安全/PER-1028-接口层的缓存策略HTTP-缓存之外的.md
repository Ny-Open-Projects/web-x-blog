---
title: [PER-1028] 接口层的缓存策略：HTTP 缓存之外的客户端缓存设计
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1028：接口层的缓存策略：HTTP 缓存之外的客户端缓存设计

**答**：
- HTTP 缓存（Cache-Control/ETag）适合静态性强接口；业务级缓存（内存/IndexedDB）适合"新鲜度可控"的数据（列表/配置）。
- 设计要素：TTL 与 stale 策略（过期先返回旧值再后台刷新）、失效机制（写操作后主动失效相关键）、容量与淘汰（LRU）。
- 一致性问题：多标签页共享缓存需同步（storage 事件/BroadcastChannel）；写后读必须读服务端绕过缓存。
- 深水：缓存键设计含业务语义（用户 ID/租户），防串数据。

```javascript
class APICache {
  constructor(ttl = 60_000) { this.ttl = ttl; this.map = new Map(); }
  async get(key, fetcher, { force = false } = {}) {
    const hit = this.map.get(key);
    if (!force && hit && Date.now() - hit.t < this.ttl) return hit.v;
    if (hit) backgroundRefresh(key, fetcher, this);   // SWR：旧值先回
    const v = await fetcher();
    this.map.set(key, { v, t: Date.now() });
    return v;
  }
  invalidate(prefix) {                                 // 写后失效
    for (const k of [...this.map.keys()])
      if (k.startsWith(prefix)) this.map.delete(k);
  }
}
function backgroundRefresh(key, fetcher, cache) {
  fetcher().then(v => cache.map.set(key, { v, t: Date.now() })).catch(() => {});
}
```
