---
title: [DP-214] 源码识别：Vue KeepAlive 与组合式组件的源码模式？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-214：源码识别：Vue KeepAlive 与组合式组件的源码模式？
**答**：
- 享元+对象池：KeepAlive 的缓存 Map（key → vnode/实例）把组件实例作为"共享单元"复用（DP-159 讲过思想，这里是源码位），max + LRU 淘汰（keys 数组尾部淘汰头部）。
- 状态模式：组件的 activated/deactivated 钩子由 KeepAlive 在切换时手动触发——实例状态在"激活/失活"两态间转移而不销毁。
- 组合模式：Transition 包 KeepAlive 包 RouterView 的嵌套——每层组件通过 render 函数的子节点递归（组件树的组合模式），KeepAlive 返回缓存的 vnode 而非新建。
- 识别要点：能指出缓存 key 的生成规则（组件 name/key）与 include/exclude 过滤（白名单策略）。

```javascript
// Vue KeepAlive 源码级简化
const KeepAlive = {
  setup(props, { slots }) {
    const cache = new Map();                 // key → vnode
    const keys = new Set();                  // LRU 顺序
    return () => {
      const vnode = slots.default();
      const key = vnode.key ?? vnode.type;
      let cached = cache.get(key);
      if (cached) {
        vnode.el = cached.el; vnode.component = cached.component;   // 享元：复用实例
        vnode.shapeFlag |= ShapeFlags.COMPONENT_SHOULD_KEEP_ALIVE;
      } else {
        keys.add(key); cache.set(key, vnode);
        if (props.max && keys.size > props.max) pruneCacheEntry(keys.values().next().value);  // LRU 淘汰
      }
      vnode.shapeFlag |= ShapeFlags.COMPONENT_KEPT_ALIVE;
      return props.include && !matches(props.include, key) ? vnode : vnode;   // include/exclude 策略
    };
  },
};
// activated/deactivated：patch 时判断 keptAlive → 不走 mount 而是 instance.a/da()（状态模式的手动转移）
```
