---
title: [DP-159] KeepAlive 的组件缓存为什么是"享元 + 备忘录"？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-159：KeepAlive 的组件缓存为什么是"享元 + 备忘录"？（高频）
**答**：
- 享元：切走的组件不销毁，实例与 DOM 被放入缓存池按 key 复用（共享同一实例，DP-038 思想从 DOM 复用升级为组件实例复用）。
- 备忘录：切走时组件状态（表单输入、滚动位置）被原样封存，切回时恢复——即快照语义。
- 工程化细节：LRU 上限防内存泄漏（超出即逐出最久未用并真正卸载）、include/exclude 匹配、activated/deactivated 钩子= 备忘录恢复/封存的时机。

```javascript
// 极简 KeepAlive：LRU 缓存 + 快照恢复（原理示意）
function createKeepAlive({ max = 10 } = {}) {
  const cache = new Map();                                    // key → { vnode, dom, state }
  return {
    mount(key, createInstance) {
      if (cache.has(key)) {
        const hit = cache.get(key);
        cache.delete(key); cache.set(key, hit);               // LRU 触碰：移到最新
        return hit;                                           // 享元命中：复用实例与 DOM
      }
      const fresh = createInstance();                         // 未命中：真实创建
      cache.set(key, fresh);
      if (cache.size > max) {                                 // 逐出最久未用（防内存膨胀）
        const oldestKey = cache.keys().next().value;
        const evicted = cache.get(oldestKey);
        evicted.destroy?.();                                  // 逐出 = 真正卸载
        cache.delete(oldestKey);
      }
      return fresh;
    },
    deactivate(key) {                                         // 切走：封存状态（备忘录出口）
      const entry = cache.get(key);
      if (entry) entry.state = entry.snapshot?.() ?? null;    // 保存滚动位置/表单值
    },
    activate(key) {                                           // 切回：恢复状态
      const entry = cache.get(key);
      entry?.restore?.(entry.state);
    },
  };
}
// Vue 内建 <KeepAlive> 等价行为：
// <KeepAlive :include="['OrderList']" :max="10">
//   <component :is="currentComp" />
// </KeepAlive>  —— activated/deactivated 钩子里做恢复/封存的业务补充
const keepAlive = createKeepAlive({ max: 10 });
const entry = keepAlive.mount('order-list', () => createOrderListInstance());
keepAlive.deactivate('order-list');                           // 切走
keepAlive.activate('order-list');                             // 切回：输入与滚动都在
```

---

## 二十、反模式与陷阱
