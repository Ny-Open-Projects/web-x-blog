---
title: [FRP-006] watch 的实现思路是什么？deep 和 immediate 如何支持？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-006：watch 的实现思路是什么？deep 和 immediate 如何支持？

**答**：
- watch 本质：用 effect 包一层 getter 来收集依赖，依赖变化时不重跑 effect，而是走 **scheduler 调度**——执行用户回调并传入新旧值。
- 收集前先 `traverse`（递归遍历）source：深层属性被"读一遍"才能触发各自的 track，这就是 `deep: true` 的实现原理。
- `immediate: true` 是创建后直接手动跑一次回调；`flush: 'post'`（默认 'pre'）决定回调排在组件更新前还是后。
- 回调里的 `onCleanup` 注册清理函数，处理竞态（旧请求回来覆盖新结果）。

```javascript
// 简化实现，帮助理解 watch 核心
let activeEffect = null;
const targetMap = new WeakMap();
function track(t, k) {
  if (!activeEffect) return;
  let m = targetMap.get(t); if (!m) targetMap.set(t, (m = new Map()));
  let s = m.get(k); if (!s) m.set(k, (s = new Set())); s.add(activeEffect);
}
function trigger(t, k) { targetMap.get(t)?.get(k)?.forEach((e) => e.scheduled?.()); }
function traverse(value, seen = new Set()) {
  if (typeof value !== 'object' || value === null || seen.has(value)) return value;
  seen.add(value);
  for (const key in value) traverse(value[key], seen); // 深层读一遍触发 track
  return value;
}

function watch(source, cb, { deep = false, immediate = false } = {}) {
  let oldValue, cleanup;
  const onCleanup = (fn) => (cleanup = fn);
  const job = () => {
    cleanup?.();                                        // 先清理上轮注册的副作用
    const newValue = effectRunner();
    cb(newValue, oldValue, onCleanup);                  // 走 scheduler：执行用户回调
    oldValue = newValue;
  };
  const getter = typeof source === 'function' ? source : () => deep ? traverse(source) : source;
  const effectRunner = () => { activeEffect = { scheduled: job }; oldValue = getter(); activeEffect = null; return oldValue; };

  if (immediate) cb(getter(), undefined, onCleanup);
  effectRunner(); // 首次执行收集依赖
}

// 用法验证（配合 FRP-001 的 reactive）
const state = { count: 0 };
const r = new Proxy(state, { get: (t, k) => (track(t, k), t[k]), set: (t, k, v) => (t[k] = v, trigger(t, k), true) });
watch(() => r.count, (n, o) => console.log('watch:', o, '->', n));
r.count = 1; // watch: 0 -> 1
```
