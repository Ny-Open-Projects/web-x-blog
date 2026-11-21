---
title: [DP-283] 笔试题：手写 LRU + TTL 缓存？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-283：笔试题：手写 LRU + TTL 缓存？
**题目**：实现 Cache 类：1) LRU 淘汰（get/put 访问刷新）；2) 条目带 TTL，过期惰性删除（get 时检查）+ 定期清扫；3) 命中率统计；4) maxLen 容量控制。
**评分点**：
- Map 迭代顺序利用正确（Map 保持插入序 → 重新 set 即移到尾部）。
- TTL 惰性检查与容量淘汰分离清晰。
- 命中率统计（hits/misses）线程安全无需考虑（JS 单线程）。
- 过期条目也占容量（put 时跳过过期条目清理）。
```javascript
class LRUCache {
  #map = new Map();
  constructor(private maxLen = 100, private ttl = 60_000) { this.hits = 0; this.misses = 0;
    this.sweeper = setInterval(() => this.sweep(), this.ttl); }
  get(key) {
    const item = this.#map.get(key);
    if (!item) { this.misses++; return undefined; }
    if (Date.now() - item.ts > this.ttl) { this.#map.delete(key); this.misses++; return undefined; }  // 2) 惰性过期
    this.#map.delete(key); this.#map.set(key, item);       // 1) LRU 刷新
    this.hits++;
    return item.value;
  }
  put(key, value) {
    for (const [k, it] of this.#map)                        // 清理过期腾出容量
      if (Date.now() - it.ts > this.ttl) this.#map.delete(k);
    if (this.#map.has(key)) this.#map.delete(key);
    else if (this.#map.size >= this.maxLen) this.#map.delete(this.#map.keys().next().value);  // 4) 淘汰最旧
    this.#map.set(key, { value, ts: Date.now() });
  }
  sweep() { for (const [k, it] of this.#map) if (Date.now() - it.ts > this.ttl) this.#map.delete(k); }
  hitRate() { const t = this.hits + this.misses; return t ? this.hits / t : 0; }
}
```
