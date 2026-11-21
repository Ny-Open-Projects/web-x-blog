---
title: [FRP-191] 手写 zustand mini：create + selector + 浅比较如何做到精准订阅？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-191：手写 zustand mini：create + selector + 浅比较如何做到精准订阅？

**答**：
- zustand 的 store 就是 `getState/setState/subscribe` 三件套（vanilla）；React 绑定用 **useSyncExternalStore**：subscribe 订阅、getSnapshot 返回"选择器结果"。
- 精准订阅的机制：selector 决定快照值——useSyncExternalStore 对快照做 `Object.is` 比较，selector 结果不变就**不重渲**。
- selector 返回**新对象**时会破坏比较（每次都是新引用）——zustand 的 `useShallow`/默认浅比较补丁就是为此：对选择器输出做浅比较后再决定。
- set 的合并语义：`set(partial)` 浅合并到 state；替换整个 state 用 `set(newState, true)`（replace）。

```javascript
// 简化实现，帮助理解 zustand mini
import { useSyncExternalStore } from 'react';

function createVanillaStore(createState) {
  let state;
  const listeners = new Set();

  const store = {
    getState: () => state,
    setState(partial, replace) {
      const next = typeof partial === 'function' ? partial(state) : partial;
      if (!Object.is(next, state)) {
        state = replace ? next : { ...state, ...next };   // 默认浅合并
        listeners.forEach(fn => fn());                     // 全量通知，过滤交给 selector
      }
    },
    subscribe(fn) { listeners.add(fn); return () => listeners.delete(fn); },
  };
  state = createState(store.setState, store.getState);
  return store;
}

function create(createState) {
  const store = createVanillaStore(createState);

  function useStore(selector = (s) => s, equalityFn = Object.is) {
    // getSnapshot 的返回值 = selector(state) —— React 用它做 Object.is 比较
    return useSyncExternalStore(
      store.subscribe,
      () => selector(store.getState()),
      () => selector(store.getInitialState?.() ?? store.getState()),
    );
  }

  // useShallow：selector 返回新对象时的浅比较包装
  useStore.withShallow = (selector) => {
    let prev;
    return () => {
      const next = selector(store.getState());
      if (shallow(prev, next)) return prev;   // 浅相等：返回旧引用 -> React 不重渲
      prev = next;
      return next;
    };
  };

  return Object.assign(useStore, { getState: store.getState, setState: store.setState, subscribe: store.subscribe });
}

function shallow(a, b) {
  if (Object.is(a, b)) return true;
  if (typeof a !== 'object' || typeof b !== 'object' || !a || !b) return false;
  const ka = Object.keys(a), kb = Object.keys(b);
  return ka.length === kb.length && ka.every(k => Object.is(a[k], b[k]));
}

// 用法：
// const useBearStore = create((set) => ({
//   bears: 0, fish: 100,
//   addBear: () => set(s => ({ bears: s.bears + 1 })),
// }));
// 精准订阅：只有 bears 变化的 set 会让该组件重渲
// const bears = useBearStore((s) => s.bears);
// fish 变化 -> selector 结果 bears 不变 -> Object.is 相等 -> 不重渲
// 陷阱：useBearStore((s) => ({ a: s.a, b: s.b })) 每次返回新对象 -> 永远重渲 -> 用 withShallow
```
