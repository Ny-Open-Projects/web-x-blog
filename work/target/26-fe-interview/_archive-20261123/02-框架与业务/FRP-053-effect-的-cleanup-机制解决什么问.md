---
title: [FRP-053] effect 的 cleanup 机制解决什么问题？手写"分支切换"的脏依赖清理。
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-053：effect 的 cleanup 机制解决什么问题？手写"分支切换"的脏依赖清理。

**答**：
- 问题场景：`effect(() => state.ok ? state.a : state.b)`，当 ok 从 true 变 false 后，effect 依赖的应是 b，但旧的 a 依赖**还留在 dep 集合里**（脏依赖），改 a 仍会误触发重跑。
- 解决：每次 runner 执行前，先把自己从**上次收集过的所有 dep 集合**中移除，再重新收集——这样只保留本次执行真正读到的依赖。
- 实现要点：effect 身上存 `deps: []`（反向记录所有收集它的 dep 集合），track 时把 effect 加入 dep 的同时也把 dep 塞进 `effect.deps`；cleanup 就是遍历 `effect.deps` 执行 `dep.delete(effect)`。
- Vue3 源码对应 `ReactiveEffect.run` 里的 `cleanupEffect(this)`，以及 track 时的 `activeEffect.deps.push(dep)`。

```javascript
// 简化实现，帮助理解 cleanup 解决分支切换脏依赖
let activeEffect = null;
const targetMap = new WeakMap();

function cleanup(effectFn) {
  for (const dep of effectFn.deps) dep.delete(effectFn); // 从所有旧集合中摘除自己
  effectFn.deps.length = 0;
}

function track(target, key) {
  if (!activeEffect) return;
  let depsMap = targetMap.get(target);
  if (!depsMap) targetMap.set(target, (depsMap = new Map()));
  let dep = depsMap.get(key);
  if (!dep) depsMap.set(key, (dep = new Set()));
  dep.add(activeEffect);
  activeEffect.deps.push(dep); // 双向记录：effect 也记住哪些 dep 收集了它
}

function effect(fn) {
  const effectFn = () => {
    cleanup(effectFn); // 关键：执行前清掉上次的依赖
    activeEffect = effectFn;
    fn();
    activeEffect = null;
  };
  effectFn.deps = [];
  effectFn();
  return effectFn;
}

const state = reactive({ ok: true, a: 'A', b: 'B' }); // get->track set->trigger 已实现
let runCount = 0;
effect(() => {
  runCount++;
  console.log(state.ok ? state.a : state.b);
});
state.ok = false;   // 重跑：读 b
state.a = 'A2';     // 不应重跑！a 已被 cleanup 掉，只有脏依赖实现会误触发
console.log('runCount =', runCount); // 期望 2（无 cleanup 会是 3）
```
