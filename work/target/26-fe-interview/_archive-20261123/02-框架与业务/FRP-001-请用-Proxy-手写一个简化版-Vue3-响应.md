---
title: [FRP-001] 请用 Proxy 手写一个简化版 Vue3 响应式（track/trigger/effect）？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-001：请用 Proxy 手写一个简化版 Vue3 响应式（track/trigger/effect）？

**答**：
- 核心三件套：`effect` 注册副作用、`track` 在**读**属性时收集当前 effect、`trigger` 在**写**属性时重新执行收集到的 effect。
- 数据结构：`targetMap: WeakMap<target, Map<key, Set<effect>>>`，三层结构分别对应"哪个对象、哪个属性、哪些 effect"。
- `reactive` 用 Proxy 拦截 get/set，get 里调 track、set 里调 trigger，改动即可自动重跑依赖它的 effect。
- 源码在此基础上增加：嵌套 effect 栈、effect 嵌套调度、cleanup 清理等。

```javascript
// 简化实现，帮助理解 Vue3 响应式核心
let activeEffect = null;
const targetMap = new WeakMap(); // target -> key -> Set<effect>

function track(target, key) {
  if (!activeEffect) return; // 不在 effect 中读取，无需收集
  let depsMap = targetMap.get(target);
  if (!depsMap) targetMap.set(target, (depsMap = new Map()));
  let dep = depsMap.get(key);
  if (!dep) depsMap.set(key, (dep = new Set()));
  dep.add(activeEffect);
}

function trigger(target, key) {
  const depsMap = targetMap.get(target);
  depsMap?.get(key)?.forEach((effect) => effect()); // 重新执行所有依赖该属性的 effect
}

function effect(fn) {
  const run = () => {
    activeEffect = run; // 执行前挂到全局，track 时收集它
    fn();
    activeEffect = null;
  };
  run();
  return run;
}

function reactive(obj) {
  return new Proxy(obj, {
    get(target, key) {
      track(target, key);
      return Reflect.get(target, key);
    },
    set(target, key, value) {
      Reflect.set(target, key, value);
      trigger(target, key);
      return true;
    },
  });
}

// 验证：修改 state.count 会自动重新执行 effect
const state = reactive({ count: 0 });
effect(() => console.log('count is', state.count)); // count is 0
state.count = 1;                                    // count is 1
```
