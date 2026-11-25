---
title: [WCN-834] Signal 的「惰性订阅 / 按需激活」如何设计以支撑超大应用？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-834：Signal 的「惰性订阅 / 按需激活」如何设计以支撑超大应用？

**答**：
- 结论先行：超大应用里不是所有 computed/effect 都该常驻——惰性策略是「没人订阅就不算、没人看就不建订阅」，用引用计数与可见性驱动，把计算与内存成本压到实际需要的范围。
- computed 天然惰性：主流实现是 pull-based + 脏标记，只有被读取时才重算——这本身就是惰性，要避免「为了提前算而主动订阅所有 computed」的反模式。
- effect 按需激活：用 `effect.when(condition)` 或基于 IntersectionObserver 的「进入视口才激活」，离开视口时 dispose 订阅；长列表尤其有效（只订阅可见项）。
- 引用计数管理：对共享 computed 维护 subscriber 计数，归零时释放对上游的订阅（降级为纯 pull），再有人订阅时重建——避免「订阅泄漏导致上游无法回收」。
- 边界：惰性意味着「第一次读可能触发一次计算级联」，要避免在渲染关键路径上集中激活大量 computed 造成卡顿；可配合优先级调度分批激活。
- 追问钩子：面试官会问「惰性和缓存eviction怎么配合」——答：引用计数归零可触发缓存失效回收，结合 LRU 上限控制内存；这是超大应用信号图治理的核心。

```javascript
// 惰性 computed：无订阅者时不主动缓存，靠脏标记按需重算
function lazyComputed(fn) {
  let dirty = true, value, subs = 0;
  const c = {
    get() {
      if (dirty) { value = fn(); dirty = false; }   // 只在被读时算
      return value;
    },
    subscribe() { subs++; return () => { if (--subs === 0) dirty = true; }; }, // 无人订阅→标记失效
    markDirty() { dirty = true; },
  };
  return c;
}
const src = { v: 1, subs: new Set(), set(n) { this.v = n; this.subs.forEach(f => f()); } };
const c = lazyComputed(() => src.v * 2);
console.log(c.get()); // 2，首次计算
src.set(3);           // c 被标脏但还没算
console.log(c.get()); // 6，读取时才重算
```
