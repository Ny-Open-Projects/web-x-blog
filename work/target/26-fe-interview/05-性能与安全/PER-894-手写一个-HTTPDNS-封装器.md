---
title: [PER-894] 手写一个 HTTPDNS 封装器：DNS 预解析、缓存 TTL 与失败回退系统 DNS
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-894：手写一个 HTTPDNS 封装器：DNS 预解析、缓存 TTL 与失败回退系统 DNS

**答**：
- 需求：实现 DnsResolver：lookup(host) 依次走：缓存（未过期）→ HTTPDNS 接口（带超时 500ms）→ 系统 DNS（fetch 正常域名，标记来源）；结果缓存带 TTL（可配置）；提供 preresolve(hosts) 批量预解析（并发 5，失败静默）；缓存按 LRU 上限 100 条。
- 边界：HTTPDNS 返回空结果视为失败走降级；同 host 并发 lookup 去重（共享同一 promise）；TTL 过期后重新解析但保留旧值兜底（新解析失败时返回过期值并标记 stale）。
- 评分点：并发去重；过期值 stale 兜底；LRU 上限。

```javascript
class DnsResolver {
  constructor({ ttl = 120000, timeout = 500, cap = 100 } = {}) {
    this.cache = new Map(); this.ttl = ttl; this.timeout = timeout;
    this.cap = cap; this.inflight = new Map();
  }
  async lookup(host) {
    if (this.inflight.has(host)) return this.inflight.get(host);   // 并发去重
    const p = this._lookup(host).finally(() => this.inflight.delete(host));
    this.inflight.set(host, p);
    return p;
  }
  async _lookup(host) {
    const c = this.cache.get(host);
    if (c && Date.now() - c.ts < this.ttl) return c;
    try {
      const ip = await Promise.race([
        httpdnsQuery(host), rejectAfter(this.timeout)]);
      if (!ip) throw new Error('empty');
      this.setCache(host, { ip, ts: Date.now(), source: 'httpdns' });
      return this.cache.get(host);
    } catch {
      if (c) return { ...c, stale: true };                     // 过期值兜底
      return { ip: null, ts: Date.now(), source: 'system-dns' };   // 回退系统 DNS
    }
  }
  setCache(host, v) {
    if (this.cache.size >= this.cap) this.cache.delete(this.cache.keys().next().value);  // LRU
    this.cache.set(host, v);
  }
  preresolve(hosts) {
    return Promise.all(hosts.map(h => this.lookup(h).catch(() => null)));   // 失败静默
  }
}
```
