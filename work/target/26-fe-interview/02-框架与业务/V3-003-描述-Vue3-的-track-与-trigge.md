---
title: [V3-003] 描述 Vue3 的 track 与 trigger 机制（附示意代码）。
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-003：描述 Vue3 的 track 与 trigger 机制（附示意代码）。
**答**：
- 依赖收集的单位是 effect（组件渲染函数、computed、watch 回调都是 effect）。
- track 发生在 get 拦截：把"当前正在运行的 activeEffect"记入 `targetMap -> depsMap -> deps` 三层结构。
- trigger 发生在 set 拦截：按 target + key 找到 effect 集合，交给调度器执行。
- 结构上是 WeakMap 嵌套 Map 嵌套 Set，WeakMap 以原始对象为 key 便于垃圾回收。

```javascript
// 依赖收集与派发更新的简化模型
let activeEffect = null;
const targetMap = new WeakMap();

function track(target, key) {
  if (!activeEffect) return; // 没有正在运行的 effect 则不收集
  let depsMap = targetMap.get(target);
  if (!depsMap) targetMap.set(target, (depsMap = new Map()));
  let deps = depsMap.get(key);
  if (!deps) depsMap.set(key, (deps = new Set()));
  deps.add(activeEffect); // 属性 -> effect 集合
}

function trigger(target, key) {
  const depsMap = targetMap.get(target);
  if (!depsMap) return;
  const effects = depsMap.get(key);
  effects && effects.forEach((effect) => effect());
}

function effect(fn) {
  activeEffect = fn;
  fn(); // 首次执行触发 get，完成依赖收集
  activeEffect = null;
}

const state = { count: 0 };
effect(() => console.log("count is", state.count)); // 输出 count is 0
```
