---
title: [FRP-005] computed 的懒计算与脏标记是如何实现的？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-005：computed 的懒计算与脏标记是如何实现的？

**答**：
- computed 不是"依赖变就立即重算"，而是两段式：依赖变化时只把 `_dirty` 标记为 true 并通知**订阅了 computed 的 effect**，getter 本身不执行——这就是懒计算。
- 只有当渲染 effect 真正读取 `computed.value` 时，若 `_dirty` 为 true 才执行 getter 重算并缓存结果；否则直接返回缓存值。
- computed 内部是一个特殊的 effect：自己作为"订阅者"收集上游依赖，又作为"依赖"被下游订阅，形成依赖链。
- 这解释了为什么 computed 中访问多个响应式数据，只有被访问的才会被收集。

```javascript
// 简化实现，帮助理解 computed 的脏标记与懒计算
let activeEffect = null;
const targetMap = new WeakMap();

function track(t, k) {
  if (!activeEffect) return;
  let m = targetMap.get(t); if (!m) targetMap.set(t, (m = new Map()));
  let s = m.get(k); if (!s) m.set(k, (s = new Set())); s.add(activeEffect);
}
function trigger(t, k) {
  targetMap.get(t)?.get(k)?.forEach((e) => {
    // 关键区分：普通 effect 直接重跑；computed 的 runner 只"置脏"不重算
    e.scheduled ? e.scheduled() : e();
  });
}
function effect(fn) {
  const run = () => { activeEffect = run; fn(); activeEffect = null; };
  run();
  return run;
}

function computed(getter) {
  let value, dirty = true;                       // dirty：脏标记
  const runner = () => { activeEffect = runner; value = getter(); activeEffect = null; };
  // scheduler：上游依赖变化时 trigger 只调用它 —— 只置脏，getter 不执行
  runner.scheduled = () => { dirty = true; };

  return {
    get value() {
      if (dirty) { runner(); dirty = false; }    // 只有脏了才真正重算并缓存
      return value;
    },
  };
}

function reactiveLike(o) {
  return new Proxy(o, {
    get: (t, k) => (track(t, k), t[k]),
    set: (t, k, v) => (t[k] = v, trigger(t, k), true),
  });
}

// 验证懒计算：改 count 只置脏，读 sum.value 才重算
const state = reactiveLike({ count: 1 });
const sum = computed(() => { console.log('computed 执行'); return state.count * 10; });
effect(() => console.log('render:', sum.value));
// 输出：computed 执行 -> render: 10

state.count = 5;          // 只置脏：computed 不执行、effect 不重跑，无任何输出
console.log(sum.value);   // 读取才重算：computed 执行 -> 50
state.count = 6;          // 再置脏
console.log(sum.value);   // computed 执行 -> 60
console.log(sum.value, sum.value); // 脏标记为 false：不再重算，缓存直接返回 60
```
