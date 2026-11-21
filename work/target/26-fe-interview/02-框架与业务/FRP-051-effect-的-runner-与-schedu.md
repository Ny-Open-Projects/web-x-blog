---
title: [FRP-051] effect 的 runner 与 scheduler 完整时序是怎样的？trigger 后到底发生了什么？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-051：effect 的 runner 与 scheduler 完整时序是怎样的？trigger 后到底发生了什么？

**答**：
- `effect(fn)` 返回的函数就是 **runner**（源码叫 `effectFn`/`ReactiveEffect.run`），它身上挂着 `.deps`（依赖集合数组）、`.options`（含 scheduler）等元信息。
- 完整时序：runner 执行 → cleanup 旧依赖 → activeEffect 指向自己 → fn 执行（内部 track 收集）→ 恢复上一个 activeEffect → 返回 fn 结果（所以 `effect(() => v)` 的返回值能拿到）。
- `trigger` 时如果 effect 配置了 **scheduler**，不直接执行 runner，而是把 runner 交给 scheduler（这就是 computed 惰性、watch 回调、组件更新入队 `queueJob` 的实现基础）。
- 一句话：runner 是"怎么执行"，scheduler 决定"什么时候、以什么方式执行"。

```javascript
// 简化实现，帮助理解 runner 与 scheduler 的完整时序
let activeEffect = null;
const targetMap = new WeakMap();

function track(target, key) {
  if (!activeEffect) return;
  let depsMap = targetMap.get(target);
  if (!depsMap) targetMap.set(target, (depsMap = new Map()));
  let dep = depsMap.get(key);
  if (!dep) depsMap.set(key, (dep = new Set()));
  if (!dep.has(activeEffect)) {
    dep.add(activeEffect);
    activeEffect.deps.push(dep); // 反向记录，供 cleanup 使用
  }
}

function trigger(target, key) {
  const dep = targetMap.get(target)?.get(key);
  if (!dep) return;
  [...dep].forEach((eff) => {
    // 有 scheduler 就把执行权交出去（watch/queueJob 的来源），否则直接重跑 runner
    eff.options?.scheduler ? eff.options.scheduler(eff) : eff();
  });
}

function effect(fn, options = {}) {
  const runner = () => {
    activeEffect = runner;
    const res = fn(); // 执行期间读响应式数据 → track 收集 runner
    activeEffect = null;
    return res;
  };
  runner.deps = [];
  runner.options = options;
  if (!options.lazy) runner(); // 默认立即执行一次完成首次收集
  return runner;
}

// 验证 scheduler：修改数据触发的是调度器而不是直接重跑
const state = reactive({ count: 0 }); // 假设 reactive/track/trigger 已按上文实现
effect(() => console.log('render with', state.count), {
  scheduler(eff) { console.log('scheduled! not rerun directly'); queueMicrotask(eff); },
});
state.count = 1; // 输出 scheduled! not rerun directly，随后微任务输出 render with 1
```
