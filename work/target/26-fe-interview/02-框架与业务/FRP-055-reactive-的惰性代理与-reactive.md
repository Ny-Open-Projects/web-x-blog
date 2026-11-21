---
title: [FRP-055] reactive 的惰性代理与 reactiveMap 缓存是怎么实现的？为什么嵌套对象不一开始就代理？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-055：reactive 的惰性代理与 reactiveMap 缓存是怎么实现的？为什么嵌套对象不一开始就代理？

**答**：
- `reactive(obj)` 只对**最外层**建 Proxy，深层对象在 **get 拦截器里读取时才包一层 reactive**（`res = reactive(res)`），这就是惰性（懒）代理——初始化成本 O(1)，且没读到的分支永远不花代理开销。
- 缓存：`reactiveMap: WeakMap<raw, proxy>`，同一原始对象多次 `reactive()` 返回**同一个代理**，避免重复建 Proxy，也保证 `reactive(p) === p`、两个代理间操作一致。
- 入口先查 `reactiveMap`，已代理直接返回；get 时若值是对象也先查缓存再新建。Vue3 源码里 `baseHandlers` + `reactiveMap/shallowReactiveMap/readonlyMap` 分表存储（`getTargetType` 区分 COMMON/Map/Set）。
- 惰性代理还规避了 Proxy 无法代理"未来才存在的属性"的问题：新对象读到了才被追踪。

```javascript
// 简化实现，帮助理解惰性代理与 reactiveMap 缓存
const reactiveMap = new WeakMap(); // raw -> proxy 缓存，WeakMap 随对象 GC

function reactive(obj) {
  // 已有代理直接返回，保证 reactive(reactive(x)) === reactive(x)
  if (reactiveMap.has(obj)) return reactiveMap.get(obj);
  const proxy = new Proxy(obj, {
    get(target, key, receiver) {
      const res = Reflect.get(target, key, receiver);
      track(target, key);
      // 惰性核心：仅当读到的值是对象时才递归 reactive，且先查缓存
      return isObject(res) ? reactive(res) : res;
    },
    set(target, key, value, receiver) {
      Reflect.set(target, key, value, receiver);
      trigger(target, key);
      return true;
    },
  });
  reactiveMap.set(obj, proxy);
  return proxy;
}

// 验证缓存：两次 reactive 同一对象得到同一代理；深层对象读到才代理
const raw = { nested: { deep: 1 } };
const p1 = reactive(raw), p2 = reactive(raw);
console.log(p1 === p2); // true

let deepReads = 0;
effect(() => { deepReads++; JSON.stringify(p1.nested); }); // 读取时才建 nested 的代理
console.log('代理后代理数应为 2 raw+nested, map size =', reactiveMap.size); // 2
p1.nested.deep = 99; // set 落在 nested 的代理上，触发收集了 nested 的 effect
```
