---
title: [DP-211] 源码识别：Zustand 源码中的观察者与原子订阅？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-211：源码识别：Zustand 源码中的观察者与原子订阅？
**答**：
- 极简观察者：createStore 就是 `{ getState, setState, subscribe }`——listeners Set，setState 后通知；比 Redux 少了 reducer/命令层（setState 直接是命令）。
- 原子订阅（selector 模式）：useStore(selector) 用 useSyncExternalStore 包一层，subscribe 传 selector 缓存值，只有 selector 结果变化才重渲染——观察者的"过滤版通知"。
- immer/middleware 是装饰：applyMiddleware 同款 compose，devtools/persist 包装 setState。
- 识别要点：对比 Redux 说清差异——Zustand 把"命令解释（reducer）"下放到业务里，核心只剩观察者 + 备忘录（selector 缓存）。

```javascript
// Zustand 核心（源码级简化）
function createStore(createState) {
  let state;
  const listeners = new Set();
  const setState = (partial, replace) => {
    const next = typeof partial === 'function' ? partial(state) : partial;
    if (next !== state) {                                   // 引用不等才通知
      state = replace ? next : { ...state, ...next };
      listeners.forEach(l => l(state));
    }
  };
  const subscribe = (l) => { listeners.add(l); return () => listeners.delete(l); };
  state = createState(setState, () => state);
  return { setState, getState: () => state, subscribe };
}
// React 绑定：原子订阅
function useStore(api, selector) {
  return useSyncExternalStore(
    api.subscribe,                          // 整体订阅
    () => selector(api.getState()),         // 读取切片
    () => selector(api.getInitialState()),
  );
}
// setState(s => ({ count: s.count + 1 })) —— 命令直接是函数，无 action type
```
