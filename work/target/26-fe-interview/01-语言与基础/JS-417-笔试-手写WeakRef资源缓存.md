---
title: [JS-417] 笔试：手写 WeakRef 资源缓存（GC 感知）
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 笔试题, 性能]
type: 笔试题
---

## JS-417：笔试：手写 WeakRef 资源缓存

**答**：实现 `GCResourceCache`：① 以对象为键缓存派生资源（如 DOM 元素 → 渲染结果），键回收后缓存条目自动失效；② 实现：WeakMap 直接可用，但要求「主动感知失效」（onEvict 回调通知清理外部资源如 GPU 纹理）——用 FinalizationRegistry 组合；③ get：键存活返回资源（不阻止键回收）；④ 说明为什么不能用 Map。写出实现与生命周期说明。

```javascript
class GCResourceCache {
  #map = new WeakMap();
  #refs = new Map();          // id -> WeakRef (用于枚举存活条目)
  constructor({ onEvict } = {}) {
    this.onEvict = onEvict;
    this.#fr = new FinalizationRegistry((id) => {
      this.#refs.delete(id);
      onEvict?.(id);          // 通知清理外部资源(GPU纹理等)
    });
  }
  #fr;
  #seq = 0;
  set(key, resource) {
    const id = key.__cacheId ??= `k${++this.#seq}`;
    if (!this.#refs.has(id)) this.#fr.register(key, id);
    this.#refs.set(id, new WeakRef(key));
    this.#map.set(key, resource);
  }
  get(key) { return this.#map.get(key); }             // 键被回收 → 自动消失
  aliveCount() {                                       // 枚举存活条目(诊断用)
    let n = 0;
    for (const [, ref] of this.#refs) if (ref.deref()) n++;
    return n;
  }
}
// 为什么不能用 Map: Map 强引用 key → DOM 元素永不回收 → 泄漏
// FinalizationRegistry: 回收时机不确定, 只做「尽力通知」, 不保证触发
```

**评分点**：
- WeakMap 为核心存储（键弱引用不阻止 GC）
- FinalizationRegistry 组合实现失效通知（外部资源清理）
- 清理回调时机不确定的认知（尽力而为语义）
- 能说清 Map 做键的泄漏原因

## 变体与延伸（补充）

**变体与延伸**：

1. FinalizationRegistry 的回调为什么不能当作可靠清理钩子？ → GC 时机由引擎决定，回调是尽力通知，页面关闭或长时间不触发 GC 都不会执行，关键资源仍需显式释放。
2. WeakRef.deref 之后对象会不会中途消失？ → 不会，deref 返回的是强引用，在该引用存活期间对象不会被回收，但下一轮 GC 后可能变 undefined，不能长期持有。
3. 为什么 #refs 用 Map 存 WeakRef 而不是 Set？ → 需要在 finalization 回调里按 id 删除对应条目并支持 aliveCount 枚举，Set 无法按 id 定位，也无法区分同键的多次注册。
