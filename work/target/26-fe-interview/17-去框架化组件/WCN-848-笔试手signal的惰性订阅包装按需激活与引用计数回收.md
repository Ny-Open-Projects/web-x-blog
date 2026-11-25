---
title: [WCN-848] 笔试：手写 signal 的「惰性订阅」包装（按需激活 + 引用计数回收）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-848：笔试：手写 signal 的「惰性订阅」包装（按需激活 + 引用计数回收）

**题目**：实现 `lazyComputed(factory)`，`factory` 是一个「创建订阅并返回 { signal, dispose } 的工厂」。要求：① 惰性——只有在第一次被 `get()` 或 `subscribe()` 时才调用 factory 真正建立订阅；② 引用计数——每当有订阅者加入 +1，退订 −1，计数归零时调用 dispose 释放上游订阅并重置为「未激活」（下次再 get 会重建）；③ `get()` 返回值；④ 未激活时 get 触发激活但自己不算常驻订阅（即 get 后计数仍为 0，便于「读一次就用」的场景）；⑤ 提供 `isActive()`。边界：factory 抛错要重置状态不残留；重复 dispose 幂等。

**答**：

```javascript
function lazyComputed(factory) {
  let active = false, instance = null, refCount = 0;
  function ensureActive() {
    if (active) return;
    instance = factory();                       // 真正建立上游订阅
    active = true;
  }
  function release() {
    if (refCount > 0) return;
    instance?.dispose?.();                      // 归零释放上游
    instance = null; active = false;
  }
  return {
    get() {
      try { ensureActive(); } catch (e) { active = false; instance = null; throw e; } // 失败重置
      return instance.signal.get();
    },
    subscribe(fn) {
      ensureActive();
      refCount++;
      const un = instance.signal.subscribe(fn);
      let done = false;
      return () => {                            // 幂等退订
        if (done) return; done = true;
        un?.(); if (--refCount === 0) release();
      };
    },
    isActive: () => active,
  };
}

// 上游工厂：每次激活新建一个 signal 并模拟订阅
const src = { v: 1, subs: new Set(), set(n) { this.v = n; this.subs.forEach(f => f()); } };
const lazy = lazyComputed(() => ({
  signal: { get: () => src.v * 2, subscribe: f => { src.subs.add(f); return () => src.subs.delete(f); } },
  dispose: () => src.subs.clear(),
}));
console.log(lazy.isActive()); // false，尚未激活
console.log(lazy.get());      // 2，触发激活但 refCount 仍 0
const un = lazy.subscribe(() => {}); console.log(lazy.isActive()); // true
un(); console.log(lazy.isActive()); // false，引用计数归零已回收
```

**评分点**：
- 真正的订阅只在首次 get/subscribe 时建立（惰性核心）。
- 引用计数 + 归零 dispose + 再次激活重建（生命周期完整）。
- factory 抛错重置状态、退订幂等（边界与健壮性）。
- get 不增加常驻计数，区分「读一次」与「持续订阅」（语义精准）。
