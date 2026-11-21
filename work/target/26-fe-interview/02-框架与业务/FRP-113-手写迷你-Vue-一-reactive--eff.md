---
title: [FRP-113] 手写迷你 Vue（一）：reactive + effect + computed 响应式核心？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-113：手写迷你 Vue（一）：reactive + effect + computed 响应式核心？

**答**：
- 三个核心模块的组合：`reactive`（Proxy + track/trigger）、`effect`（runner + 栈 + cleanup）、`computed`（lazy effect + 缓存 + 依赖为脏时重算）。
- computed 实现：内部 effect 设 `lazy: true` 不立即执行；读取 `.value` 时若 `dirty` 才执行求值；求值期间收集的依赖触发时只做 `dirty = true` 并通知订阅 computed 的 effect（scheduler 不直接重算——这正是 FRP-051 scheduler 的应用）。
- 细节点：effect 栈保证嵌套、cleanup 保证分支切换、ref 用 getter/setter 转发（FRP-054）。

```javascript
// 简化实现，帮助理解：60 行内的迷你响应式核心
let activeEffect = null, effectStack = [];
const targetMap = new WeakMap();

function reactive(obj) {
  return new Proxy(obj, {
    get(t, k) {
      track(t, k);
      const v = Reflect.get(t, k);
      return typeof v === 'object' && v ? reactive(v) : v; // 惰性深层代理
    },
    set(t, k, v) { Reflect.set(t, k, v); trigger(t, k); return true; },
  });
}
function track(t, k) {
  if (!activeEffect) return;
  let m = targetMap.get(t); if (!m) targetMap.set(t, (m = new Map()));
  let d = m.get(k); if (!d) m.set(k, (d = new Set()));
  if (!d.has(activeEffect)) { d.add(activeEffect); activeEffect.deps.push(d); }
}
function trigger(t, k) {
  const d = targetMap.get(t)?.get(k); if (!d) return;
  [...d].forEach((e) => e.computed ? e.scheduler?.() : (e.scheduler ? e.scheduler(e) : e()));
}
function effect(fn, opts = {}) {
  const e = () => {
    e.deps.forEach((d) => d.delete(e)); e.deps = [];      // cleanup
    effectStack.push(e); activeEffect = e;
    try { return fn(); } finally {
      effectStack.pop(); activeEffect = effectStack[effectStack.length - 1] || null;
    }
  };
  e.deps = []; e.computed = opts.computed; e.scheduler = opts.scheduler;
  if (!opts.lazy) e();
  return e;
}
function computed(getter) {
  let value, dirty = true;
  const runner = effect(getter, { lazy: true, computed: true, scheduler: () => { dirty = true; triggerValue(obj, 'value'); } });
  const obj = {
    get value() {
      if (dirty) { value = runner(); dirty = false; }      // 惰性 + 缓存
      if (activeEffect && !activeEffect.computed) trackValue(obj, 'value', activeEffect); // 链式收集
      return value;
    },
  };
  return obj;
}
const valueDeps = new WeakMap();
function trackValue(obj, key, eff) {
  let m = valueDeps.get(obj); if (!m) valueDeps.set(obj, (m = new Map()));
  let s = m.get(key); if (!s) m.set(key, (s = new Set()));
  s.add(eff); eff.deps.push(s);
}
function triggerValue(obj, key) {
  valueDeps.get(obj)?.get(key)?.forEach((eff) => eff()); // 通知订阅该 computed 的读取方 effect 重跑
}
// 更新链：sum 依赖的 count 变 -> computed 标脏 -> 读取方 effect 重跑
const state = reactive({ count: 1 });
const sum = computed(() => state.count * 10);
effect(() => console.log('sum =', sum.value)); // sum = 10
state.count = 3;                               // sum = 30
```
