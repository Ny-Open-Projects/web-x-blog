---
title: [DP-084] Zustand/Jotai 这类现代状态库是什么模式组合？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-084：Zustand/Jotai 这类现代状态库是什么模式组合？
**答**：
- Zustand = **模块单例**（create 出全局唯一 store）+ **观察者**（selector 订阅 + 粒度通知）+ **外观**（`store.setState` 一个入口）。
- Jotai = **原子化**（atom 是最小状态单元，原子间组合成依赖图）+ 观察者（派生 atom 自动重算）。
- 对比 redux：去掉了"集中 reducer + dispatch 命令"，改为"直接 setState + selector 订阅"——命令模式弱化，观察者保留。
- 面试落点：能说出"selector 级订阅避免全树重渲染"（对应 reselect 记忆化思想，见 DP-078）。

```javascript
// Zustand 风格的 mini 实现：单例 store + selector 订阅
function createStore(initial) {
  let state = initial;                        // 闭包私有：唯一状态
  const listeners = new Set();                // selector 级订阅
  const store = {
    getState: () => state,
    setState(patch) {
      const prev = state;
      state = typeof patch === 'function' ? patch(state) : { ...state, ...patch };
      listeners.forEach(({ selector, fn }) => {
        if (selector(prev) !== selector(state)) fn(state); // 只通知结果变化的订阅者（细粒度）
      });
    },
    subscribe(selector, fn) { listeners.add({ selector, fn }); return () => listeners.delete(fn); },
  };
  return store;
}
// 使用：模块级单例（ESM 保证全局唯一）
const useBearStore = createStore({ bears: 0, users: [] });
useBearStore.subscribe((s) => s.bears, (s) => console.log('BearView 重渲染', s.bears));
useBearStore.subscribe((s) => s.users.length, (s) => console.log('UserView 重渲染', s.users.length));
useBearStore.setState((s) => ({ bears: s.bears + 1 })); // 只触发 BearView
// BearView 重渲染 1 —— users 相关订阅未被通知（性能关键）

// Jotai 风格：原子 + 派生（依赖图自动重算）
function atom(initialValue) { return { init: initialValue, deps: [] }; }
function derivedAtom(read, ...deps) { return { read, deps }; } // 派生原子声明依赖
const countAtom = atom(0);
const doubleAtom = derivedAtom(
  (get) => get(countAtom) * 2, // get 即依赖收集（代理/观察者）
  countAtom
);
const store2 = new Map(); // 简化的原子值存储
store2.set(countAtom, 5);
const get = (a) => (a.read ? a.read(get) : store2.get(a));
console.log(get(doubleAtom)); // 10 —— 依赖图驱动派生
```
