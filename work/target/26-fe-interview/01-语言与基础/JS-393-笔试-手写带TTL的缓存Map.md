---
title: [JS-393] 笔试：手写带 TTL 的缓存 Map（惰性过期 + 容量上限）
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 笔试题, 性能]
type: 笔试题
---

## JS-393：笔试：手写带 TTL 的缓存 Map

**答**：实现 `TTLMap({ ttl, max })`：① get：命中且未过期返回值，过期删除返回 undefined（惰性过期，不用定时器）；② set：超容量时先清理过期项，仍超则淘汰最旧；③ sweep()：主动清理（低频调用防内存驻留）；④ set 相同 key 刷新过期时间；⑤ 支持 maxAgePerKey 覆盖全局 ttl。写出实现。

```javascript
class TTLMap {
  #m = new Map();     // key -> { v, expireAt }
  constructor({ ttl = 60_000, max = 500 } = {}) {
    this.ttl = ttl; this.max = max;
  }
  get(key) {
    const e = this.#m.get(key);
    if (!e) return undefined;
    if (Date.now() > e.expireAt) { this.#m.delete(key); return undefined; } // 惰性过期
    return e.v;
  }
  set(key, value, maxAge) {
    const ttl = maxAge ?? this.ttl;
    // 淘汰: 先清过期, 再按插入序删最旧
    if (this.#m.size >= this.max && !this.#m.has(key)) {
      const now = Date.now();
      for (const [k, e] of this.#m) {
        if (now > e.expireAt) this.#m.delete(k);
        if (this.#m.size < this.max) break;
      }
      while (this.#m.size >= this.max)
        this.#m.delete(this.#m.keys().next().value);
    }
    this.#m.set(key, { v: value, expireAt: Date.now() + ttl });  // 重写 = 刷新 TTL
  }
  sweep() {
    const now = Date.now();
    for (const [k, e] of this.#m) if (now > e.expireAt) this.#m.delete(k);
  }
  get size() { return this.#m.size; }
}
// 定期 sweep 防止「过期但从未 get」的项驻留
setInterval(() => cache.sweep(), 60_000);
```

**评分点**：
- 惰性过期（get 时检查）+ 主动 sweep 的双层设计
- 淘汰顺序：先过期项后最旧项（Map 插入序）
- set 重写刷新过期时间（易漏）
- 容量检查排除「更新已有 key」的场景
