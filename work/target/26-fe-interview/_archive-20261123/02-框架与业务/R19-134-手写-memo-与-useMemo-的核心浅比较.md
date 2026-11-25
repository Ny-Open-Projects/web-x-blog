---
title: [R19-134] 手写 memo 与 useMemo 的核心——浅比较是怎么实现的？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-134：手写 memo 与 useMemo 的核心——浅比较是怎么实现的？
**答**：
- `React.memo` 是组件级缓存：新 props 与旧 props 做一次**浅比较**，全等则直接复用上次渲染结果，跳过函数执行。
- `useMemo` 是 hook 级缓存：依赖浅比较通过就返回上次缓存值，不重算。
- 浅比较规则：第一层用 `Object.is` 比较；对象只比引用不递归——所以传内联对象/函数给 memo 组件会击穿缓存。
- 二者的共同内核就是 `shallowEqual`，这也是面试手写的高频拆分点。

```jsx
// shallowEqual.js —— memo 与 useMemo 共同的核心
export function shallowEqual(a, b) {
  if (Object.is(a, b)) return true;              // 引用相等直接通过

  if (typeof a !== 'object' || a === null ||
      typeof b !== 'object' || b === null) {
    return false;                                // 基本类型引用不同即不等
  }

  const keysA = Object.keys(a);
  const keysB = Object.keys(b);
  if (keysA.length !== keysB.length) return false;

  // 只比较第一层，且要求值本身 Object.is 相等（不递归）
  return keysA.every(key =>
    Object.prototype.hasOwnProperty.call(b, key) && Object.is(a[key], b[key])
  );
}

// memo.js —— 组件级缓存：props 浅比较通过则跳过渲染
import { shallowEqual } from './shallowEqual';

export function memo(Component, areEqual = shallowEqual) {
  let prevProps = null;
  let prevOutput = null;

  function Memoed(props) {
    if (prevOutput !== null && areEqual(prevProps, props)) {
      return prevOutput;                         // 命中缓存：复用上次输出
    }
    prevProps = props;
    prevOutput = Component(props);               // 未命中：真正执行
    return prevOutput;
  }
  return Memoed;
}

// useMemo.js —— hook 级缓存：依赖浅比较通过则返回上次值
export function useMemo(factory, deps) {
  const fiber = currentFiber;
  const index = hookIndex++;
  const hook = fiber.hooks[index] ?? (fiber.hooks[index] = { deps: null, value: undefined });

  if (hook.deps === null || deps.some((d, i) => !Object.is(d, hook.deps[i]))) {
    hook.value = factory();                      // 依赖变了才重算
    hook.deps = deps;
  }
  return hook.value;                             // 没变返回缓存值
}

// ---- 击穿演示：内联对象每次都是新引用 ----
const ExpensiveItem = memo(function ExpensiveItem({ user, onClick }) { /* ... */ });
// <ExpensiveItem user={{ id: 1 }} onClick={() => save(1)} />
// 上面写法每轮渲染 user、onClick 都是新引用，浅比较必失败，memo 形同虚设
// 正确做法：user 用 useMemo/稳定数据源，onClick 用 useCallback 或提到稳定层
```
