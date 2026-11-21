---
title: [PER-267] WeakRef 与 FinalizationRegistry 有什么用？在缓存与泄漏监控里怎么落地？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-267：WeakRef 与 FinalizationRegistry 有什么用？在缓存与泄漏监控里怎么落地？

**答**：
- WeakRef 弱引用对象，不阻止 GC；`deref()` 对象活着返回引用、被回收返回 undefined。典型用途：外部大对象的观察者索引（如检测 detached DOM）、框架内部追踪实例。
- FinalizationRegistry 在对象被 GC 后收到回调（回调里拿 registry 传的 token 而不是对象本身），可做：资源释放监控（泄漏计数）、原生资源（Worker/WASM 句柄）的事后清理。
- 铁律：不能用它们"复活"或管理业务对象生命周期——GC 时机不可控；业务缓存要限容量请用 LRU，不要拿 WeakMap/WeakRef 当"自动清理的缓存"（键不可枚举、时机不确定）。
- 落地示例：图片对象池用 WeakRef 存可复用实例 + registry 统计回收率（回收率高说明池没起作用，反向证明缓存策略失效）。

```javascript
const poolStats = { created: 0, collected: 0 };
const registry = new FinalizationRegistry((id) => {
  poolStats.collected++;
  console.debug(`[pool] 对象 ${id} 被 GC，回收率 ${poolStats.collected / poolStats.created}`);
});

class ItemPool {
  #items = new Map();       // id -> WeakRef
  acquire(id) {
    const ref = this.#items.get(id)?.deref?.();
    if (ref) return ref;                        // 命中池
    poolStats.created++;
    const item = createHeavyItem(id);
    registry.register(item, id);                // 对象被回收时通知
    this.#items.set(id, new WeakRef(item));
    return item;
  }
  release(id) { /* 归还逻辑：从活跃列表移除，池里的 WeakRef 不阻止 GC */ }
}
// 判读：collected/created 接近 1 => 池几乎没复用到（获取-归还节奏有问题）
```
