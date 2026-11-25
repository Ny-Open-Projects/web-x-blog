---
title: [DP-339] 笔试题：手写 WeakRef 缓存（自动回收）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-339：笔试题：手写 WeakRef 缓存（自动回收）？
**答**：实现 WeakCache：1) 大对象缓存（WeakRef 持有，GC 可回收）；2) get 时 ref.deref() 判活；3) FinalizationRegistry 清理键记录；4) 与普通 Map 缓存的适用边界。
**评分点**：
- deref 判活与重建策略。
- Registry 回调清理键表。
- 适用边界说清（只在"重算比持有便宜"时用）。
- 不缓存必要数据（GC 随时收走）。
```javascript
class WeakCache {
  #refs = new Map();
  #registry = new FinalizationRegistry((key) => this.#refs.delete(key));   // 3)
  get(key, factory) {
    const ref = this.#refs.get(key);
    const val = ref?.deref();                              // 2) 判活
    if (val) return val;
    const fresh = factory(key);
    this.#refs.set(key, new WeakRef(fresh));
    this.#registry.register(fresh, key);
    return fresh;
  }
}
// 适用：反序列化的大 JSON/编译产物缓存 —— GC 回收后可重算。
// 不适用：会话状态/权限快照（丢失即错误）——用强引用 Map + LRU。
```
