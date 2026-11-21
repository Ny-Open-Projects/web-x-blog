---
title: [PER-268] 全局缓存（Map/数组）只进不出导致的内存泄漏，如何用容量上限与 TTL 治理？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-268：全局缓存（Map/数组）只进不出导致的内存泄漏，如何用容量上限与 TTL 治理？

**答**：
- 泄漏形态：`const cache = new Map()` + set 无限增；埋点去重集合、路由缓存、接口缓存都中过招。长驻 SPA 一个页面挂一天，缓存堆积几百 MB。
- 双闸门：容量上限（LRU 淘汰最久未用）+ TTL（过期清理）。容量挡"堆积量"，TTL 挡"陈旧数据"（业务正确性问题同时解决）。惰性删除优先——读时检查过期并顺带清理过期项，避免全量扫描。
- 清理策略选型：读多写多用 LRU（O(1) 双向链表）；写多读少可用 FIFO + 定期批量扫描 TTL；键含 DOM/大对象的考虑 WeakMap（key 可枚举问题要接受）。
- 验收：内存面板反复访问 > 上限数量的键，堆水位应稳定在缓存容量附近；命中率指标同步看（淘汰太狠会伤命中率，容量设太小）。

```javascript
class TTLCache extends Map {                  // Map 保插入序 = 近似 LRU 语义
  constructor(max = 500, ttl = 5 * 60_000) { super(); this.max = max; this.ttl = ttl; }
  get(k) {
    const v = super.get(k);
    if (!v) return undefined;
    if (Date.now() > v.exp) { super.delete(k); return undefined; }   // 惰性过期
    super.delete(k); super.set(k, v);        // 重插 = 提到"最近使用"位
    return v.val;
  }
  set(k, val) {
    if (super.size >= this.max) {
      const oldest = super.keys().next().value;   // Map 保序，第一个即最旧
      super.delete(oldest);
    }
    super.set(k, { val, exp: Date.now() + this.ttl });
  }
}
// 反例对照：const cache = new Map(); cache.set(k, bigData) —— 无上限，长驻页面必然泄漏
```
