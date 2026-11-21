---
title: [FRP-007] effect 的 cleanup 机制解决什么问题？onCleanup 怎么实现？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-007：effect 的 cleanup 机制解决什么问题？onCleanup 怎么实现？

**答**：
- 问题一（分支切换）：`effect(() => show ? a.value : b.value)`，从 a 分支切到 b 后，a 不再被读取，但依赖表里还留着该 effect——a 变化会触发一次无意义的重跑。
- 问题二（竞态）：watch 回调里的异步请求，旧请求后返回会覆盖新数据。
- 解法：每次 effect 执行前先 cleanup——把自己从**上一轮收集的所有依赖集合**中移除，再重新收集本轮依赖。
- 用户侧 `onCleanup(fn)` 注册的是清理回调（取消请求等），同样在每轮开始与 effect 停止时执行。

```javascript
// 简化实现，帮助理解 cleanup
let activeEffect = null;

function effect(fn) {
  const runner = () => {
    // cleanup：先从上一轮的所有依赖集合中移除自己
    runner.deps.forEach((depSet) => depSet.delete(runner));
    runner.deps.length = 0;

    activeEffect = runner;
    const ret = fn(runner); // 把 onCleanup 交给用户注册
    activeEffect = null;
    return ret;
  };
  runner.deps = [];   // 记录本轮收集到的所有依赖集合引用
  runner.onCleanup = (fn) => (runner.cleanupFn = fn);
  runner.cleanupFn = null;
  return runner;
}

// track 时要把 dep 集合也记到 effect 上（配合上面的 deps）
function trackWithCleanup(target, key, getDep) {
  if (!activeEffect) return;
  const dep = getDep(target, key);
  dep.add(activeEffect);
  activeEffect.deps.push(dep); // effect 记住自己在哪些集合里，执行前可被移除
  activeEffect.cleanupFn?.(); activeEffect.cleanupFn = null; // 执行用户清理
  if (activeEffect.cleanup) { activeEffect.cleanup(); activeEffect.cleanup = null; }
  activeEffect.cleanup = () => activeEffect.cleanupFn?.();
}

// 验证：切换 show 后，a 的变化不再触发 effect
// effect((onCleanup) => {
//   onCleanup(() => request.abort());  // 每轮先取消旧请求，解决竞态
//   show.value ? console.log(a.value) : console.log(b.value);
// });
```
