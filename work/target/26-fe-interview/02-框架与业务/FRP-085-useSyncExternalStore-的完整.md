---
title: [FRP-085] useSyncExternalStore 的完整实现是怎样的？为什么外部 store 需要它而不能用 useEffect 订阅？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-085：useSyncExternalStore 的完整实现是怎样的？为什么外部 store 需要它而不能用 useEffect 订阅？

**答**：
- 它解决三件事：**订阅**（subscribe 在 mount 时建立、unmount 时清理）、**快照一致性**（每次渲染用 getSnapshot 取值，必须返回稳定引用）、**并发撕裂（tearing）防护**——Concurrent 渲染可中断，若渲染途中外部 store 变化，组件树一部分用旧值一部分用新值，useSyncExternalStore 在渲染前后检查快照是否一致，不一致**强制同步重渲染**。
- 为什么不能用 useEffect + setState 订阅：useEffect 在 paint 后执行，存在**错过更新窗口**（订阅建立前的变更丢失）；getSnapshot 每次返回新对象会让 useEffect 死循环；并发模式下无法保证整棵树读到同一快照。
- 完整实现要点：mount 阶段 `subscribe(handleStoreChange)` 并首检；每次渲染比对 `getSnapshot()` 与缓存值，不同则 `forceStoreRerender`；`getServerSnapshot` 支持 SSR。

```javascript
// 简化实现，帮助理解订阅 + 快照一致性 + 撕裂防护
function useMySyncExternalStore(subscribe, getSnapshot, getServerSnapshot = getSnapshot) {
  // 1. 渲染时取快照并缓存为 hook 状态
  let value = getSnapshot();
  let prevValue = value;

  // 2. 渲染后再取一次：发现变了说明并发渲染期间 store 被改（撕裂）-> 强制重渲染
  if (getSnapshot() !== prevValue) {
    forceStoreRerender();
  }

  // 3. mount/unmount 管理：订阅回调里检查快照变化
  const handleStoreChange = () => {
    if (getSnapshot() !== prevValue) {
      prevValue = getSnapshot();
      forceStoreRerender(); // 外部变化 -> 以新快照重渲染
    }
  };
  // 真实实现由 React 在 commit 时决定订阅时机，这里模拟立即订阅
  const unsubscribe = subscribe(handleStoreChange);
  return value;
}
let forceStoreRerender = () => {};

// 模拟一个外部 store
function createStore() {
  let state = { count: 0 };
  const listeners = new Set();
  return {
    subscribe(fn) { listeners.add(fn); return () => listeners.delete(fn); },
    getSnapshot: () => state, // 必须稳定引用，不可每次新建对象
    setCount(n) { state = { count: n }; listeners.forEach((f) => f()); },
  };
}
const store = createStore();

// 组件渲染逻辑（模拟两次渲染）
function render() {
  const count = useMySyncExternalStore(store.subscribe, store.getSnapshot);
  console.log('rendered with count =', count.count);
}
forceStoreRerender = () => { console.log('(tearing detected / store changed) re-render'); render(); };
render();
store.setCount(1); // (store changed) re-render -> rendered with count = 1

// 对比错误示范：useEffect 订阅 + getSnapshot 返回新对象
// useEffect(() => store.subscribe(() => setState(store.getSnapshot())), [])
// 1. 订阅在 paint 后，之前的更新丢失；2. 若 getSnapshot 返回 {count} 新对象，浅比较永不等 -> 死循环
```
