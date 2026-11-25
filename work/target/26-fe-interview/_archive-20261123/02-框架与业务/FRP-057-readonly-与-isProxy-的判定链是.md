---
title: [FRP-057] readonly 与 isProxy 的判定链是怎样的？浅层与深层只读如何实现？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-057：readonly 与 isProxy 的判定链是怎样的？浅层与深层只读如何实现？

**答**：
- 判定链依靠 **ReactiveFlags 特殊 key**：代理的 get 拦截器里对 `key === ReactiveFlags.IS_REACTIVE / IS_READONLY / RAW` 直接返回布尔或原始对象，不做常规取值——因为 Proxy 无法从代理对象外部"看出"它是代理，只能靠约定 key 自查。
- `isReactive(v)`：访问 `v[ReactiveFlags.IS_REACTIVE]`，是深层响应式代理（或其嵌套值）为 true；`isReadonly` 同理；`isProxy(v) = isReactive(v) || isReadonly(v)`。
- `toRaw(v)` 借 `ReactiveFlags.RAW` 从代理还原原始对象（源码里对应 `proxy[ReactiveFlags.RAW]`，由 Proxy 的 get 特判返回 target）。
- readonly 用**另一套 handler**：get 不 track（只读不会变，没必要收集），set/deleteProperty 直接**开发环境警告并返回 true**；`readonlyMap` 独立缓存，与 reactiveMap 分开。

```javascript
// 简化实现，帮助理解 ReactiveFlags 判定链与 readonly
const ReactiveFlags = {
  IS_REACTIVE: '__v_isReactive',
  IS_READONLY: '__v_isReadonly',
  RAW: '__v_raw',
};

function createHandler(isReadonly) {
  return {
    get(target, key, receiver) {
      // 判定链核心：约定 key 优先短路
      if (key === ReactiveFlags.IS_REACTIVE) return !isReadonly;
      if (key === ReactiveFlags.IS_READONLY) return isReadonly;
      if (key === ReactiveFlags.RAW) return target;
      const res = Reflect.get(target, key, receiver);
      if (!isReadonly) track(target, key);      // 只读对象不收集依赖
      return isObject(res) ? (isReadonly ? readonly(res) : reactive(res)) : res;
    },
    set(target, key, value) {
      if (isReadonly) {
        console.warn(`Cannot set ${String(key)}: target is readonly`);
        return true; // 静默失败，保持与源码一致
      }
      Reflect.set(target, key, value);
      trigger(target, key);
      return true;
    },
  };
}

const reactiveMap = new WeakMap(), readonlyMap = new WeakMap();
function shared(obj, map, isReadonly) {
  if (map.has(obj)) return map.get(obj);
  const proxy = new Proxy(obj, createHandler(isReadonly));
  map.set(obj, proxy);
  return proxy;
}
const reactive2 = (o) => shared(o, reactiveMap, false);
const readonly2 = (o) => shared(o, readonlyMap, true);
const isReactive2 = (v) => !!(v && v[ReactiveFlags.IS_REACTIVE]);
const isReadonly2 = (v) => !!(v && v[ReactiveFlags.IS_READONLY]);
const isProxy = (v) => isReactive2(v) || isReadonly2(v);
const toRaw = (v) => v?.[ReactiveFlags.RAW] ?? v;

const ro = readonly2({ a: 1 });
ro.a = 2;                       // 警告且不生效
console.log(isProxy(ro), isProxy(reactive2({})), isProxy({})); // true true false
console.log(isReactive2(ro), isReadonly2(ro));                  // false true
console.log(toRaw(ro) === ro);  // false，toRaw 还原了原始对象
```

## 九、Vue 编译器原理
