---
title: [PER-731] 手写一个多级缓存管理器：内存 Map -> IndexedDB -> 网络，带 TTL、容量上限与命中率统计
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-731：手写一个多级缓存管理器：内存 Map -> IndexedDB -> 网络，带 TTL、容量上限与命中率统计

**答**：
- 读路径：内存命中直返 -> IDB 命中回填内存 -> 未命中走网络并写两级；写路径双写；淘汰：内存按容量 LRU，IDB 按 TTL 过期清理（定期扫描）。
- 要点：value 存 IDB 前记录 `{data, ts, etag}` 支持条件请求（304 透传省流量）；命中率分桶上报（读路径各层占比）；内存层容量按设备档（低端 100 条）。
- 边界：IDB 不可用（隐私模式）降级内存单级；序列化成本（大对象 clone）抽样统计；并发读同一 key 要 inflight 合并。
- 评分点：条件请求与层间回填。

```javascript

class TieredCache {
  constructor(idbStore, { memMax = 100, ttlMs = 300000 } = {}) {
    this.mem = new Map(); this.idb = idbStore; this.memMax = memMax;
    this.ttl = ttlMs; this.stats = { mem: 0, idb: 0, net: 0 };
    this.inflight = new Map();
  }
  async get(key, fetcher) {
    const m = this.mem.get(key);
    if (m && Date.now() - m.ts < this.ttl) { this.stats.mem++; return m.data; }
    const cached = await this.idb.get(key).catch(() => null);
    if (cached && Date.now() - cached.ts < this.ttl) {
      this.stats.idb++;
      this.putMem(key, cached);                                 // 回填内存层
      return cached.data;
    }
    if (this.inflight.has(key)) return this.inflight.get(key);  // 并发合并
    const p = (async () => {
      const data = await fetcher(cached?.etag);
      this.set(key, data);
      this.stats.net++;
      return data;
    })();
    this.inflight.set(key, p);
    try { return await p; } finally { this.inflight.delete(key); }
  }
  set(key, data) {
    this.putMem(key, { data, ts: Date.now() });
    this.idb.put(key, { data, ts: Date.now() }).catch(() => {}); // IDB 失败不影响
  }
  putMem(key, val) {
    this.mem.set(key, val);
    if (this.mem.size > this.memMax) {                          // LRU 淘汰
      const oldest = [...this.mem.entries()].sort((a, b) => a[1].ts - b[1].ts)[0];
      this.mem.delete(oldest[0]);
    }
  }
}
```
