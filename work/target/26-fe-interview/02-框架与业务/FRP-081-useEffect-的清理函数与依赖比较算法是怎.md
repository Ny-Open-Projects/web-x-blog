---
title: [FRP-081] useEffect 的清理函数与依赖比较算法是怎么实现的？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-081：useEffect 的清理函数与依赖比较算法是怎么实现的？

**答**：
- 依赖比较：`areHookInputsEqual(nextDeps, prevDeps)` 逐位 `is`（Object.is）比较，长度不等直接 false——NaN 相等、+0/-0 区分都由 `Object.is` 保证；`null`/`undefined` 依赖跳过比较。
- effect 节点结构：`{ tag, create, destroy, deps, next }`（函数组件的 effect 也串在 fiber.updateQueue 的环形链表上）；比较不等时先执行旧 effect 的 `destroy()`（上一次的清理），再执行新 `create()`，其返回值记为新的 destroy。
- 时序上 passive effect（useEffect）不在 commit 同步执行，而是**paint 之后**由 Scheduler 调度的 `flushPassiveEffects` 异步执行；unmount 时统一调用所有 destroy。
- 常见坑：依赖数组里漏引用类型 -> 浅比较恒等不触发；对象/数组依赖应使用 useMemo 化引用或 `useEffect(() => {}, [JSON.stringify(x)])` 变通。

```javascript
// 简化实现，帮助理解依赖比较与清理链
const is = (a, b) => (a === b ? (a !== 0 || 1 / a === 1 / b) : (a !== a && b !== b)); // Object.is
function areHookInputsEqual(next, prev) {
  if (prev === null || next === null || next.length !== prev.length) return false;
  for (let i = 0; i < next.length; i++) if (!is(next[i], prev[i])) return false;
  return true;
}

function createMyEffect(create, deps) {
  const effect = { create, deps: deps === undefined ? null : deps, destroy: null, tag: 'passive' };
  if (areHookInputsEqual(effect.deps, effect.prevDeps)) {
    // deps 相等（或传 null 之外全部相等）：跳过执行
    return 'skipped';
  }
  // 先跑上次清理，再跑新 effect
  if (effect.destroy) effect.destroy();
  effect.destroy = effect.create() || null; // create 返回值就是清理函数
  effect.prevDeps = effect.deps;
  return 'ran';
}

// 模拟三次渲染同一组件的 effect
const effectNode = { prevDeps: null, destroy: null };

// 第 1 次渲染：deps [1]
console.log(createMyEffect.call({ ...effectNode }, (() => { console.log('effect 1'); return () => console.log('cleanup 1'); }), [1]) || 'ran');
// 第 2 次渲染：deps [1] -> Object.is 相等跳过
// 第 3 次渲染：deps [2] -> 先 cleanup 1 再 effect 2
console.log(areHookInputsEqual([2], [1])); // false -> 需要重新执行
console.log(areHookInputsEqual([NaN], [NaN])); // true：Object.is 视 NaN 相等
console.log(areHookInputsEqual([{ a: 1 }], [{ a: 1 }])); // false：对象浅比较引用不同
```
