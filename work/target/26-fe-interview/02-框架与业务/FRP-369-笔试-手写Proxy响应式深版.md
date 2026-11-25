---
title: [FRP-369] 笔试：手写 Proxy 响应式深版（数组/Map/Set 支持）
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## FRP-369：笔试：手写 Proxy 响应式深版

**答**：扩展 reactive 支持集合类型：① 数组：push/splice 等变异方法触发更新（length 依赖追踪）；② Map/Set：get/set/has/delete/add 的拦截（方法劫持——Map 不是普通属性访问）；③ 遍历依赖：forEach/keys/values 依赖「ITERATE_KEY」（集合结构变化触发）；④ 嵌套对象惰性代理；⑤ readonly 浅层选项。写出 Map 的拦截实现与关键点。

```javascript
const rawMap = new WeakMap();   // raw → reactive
const depMap = new WeakMap();   // raw → Map<key, Set<effect>>

function track(target, key) {
  if (!active) return;
  const deps = depMap.get(target) ?? depMap.set(target, new Map()).get(target);
  const set = deps.get(key) ?? deps.set(key, new Set()).get(key);
  set.add(active);
}
function trigger(target, key) {
  const deps = depMap.get(target)?.get(key);
  deps?.forEach((e) => { if (e !== active) e.run(); });
}

function reactive(obj) {
  const existing = rawMap.get(obj);
  if (existing) return existing;
  const proxy = new Proxy(obj, {
    get(t, key, receiver) {
      if (key === '__isReactive') return true;
      if (t instanceof Map) return mapHandlers(t, key, receiver);   // Map 分流
      track(t, key);
      const v = Reflect.get(t, key, receiver);
      return (typeof v === 'object' && v !== null) ? reactive(v) : v;  // 惰性嵌套
    },
    set(t, key, nv) {
      const old = t[key];
      const r = Reflect.set(t, key, nv);
      if (!Object.is(old, nv)) { trigger(t, key); trigger(t, ITERATE_KEY); }
      return r;
    },
  });
  rawMap.set(obj, proxy);
  return proxy;
}

function mapHandlers(t, key) {
  const methods = {
    get: (k) => { track(t, k); return t.get(k); },
    set: (k, v) => { const had = t.has(k); t.set(k, v); trigger(t, k); if (!had) trigger(t, ITERATE_KEY); return t; },
    delete: (k) => { const had = t.has(k); t.delete(k); if (had) { trigger(t, k); trigger(t, ITERATE_KEY); } },
    has: (k) => { track(t, k); return t.has(k); },
  };
  return methods[key] ?? Reflect.get(t, key);
}
// 关键: Map 的 get('x') 不是属性访问 → 必须劫持方法; 结构变化(size/遍历)触发 ITERATE_KEY
```

**评分点**：
- 集合方法劫持（Map.get 不是属性访问的核心认知）
- ITERATE_KEY（结构变化的依赖键）
- 惰性嵌套代理与缓存（rawMap 防重复包装）
- 数组 length 与索引的联动追踪说明
