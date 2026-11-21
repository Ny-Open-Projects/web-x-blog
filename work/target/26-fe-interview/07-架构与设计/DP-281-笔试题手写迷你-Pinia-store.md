---
title: [DP-281] 笔试题：手写迷你 Pinia（工厂+观察者+持久化）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-281：笔试题：手写迷你 Pinia（工厂+观察者+持久化）？
**题目**：实现 `defineStore(id, setup)` 与 `useStore()`：1) 同 id 单例；2) state 变更通知订阅者；3) $patch 批量合并；4) 订阅函数支持立即回放当前 state；5) 持久化插件（$subscribe 时写 localStorage）。
**评分点**：
- 单例容器正确（Map + inject/全局兜底）。
- 观察者通知在批量合并后只触发一次（$patch 合一）。
- 插件注册时序正确（store 创建后调用，拿到 $subscribe）。
- 卸载清理（unsubscribe 返回解绑函数）。
```javascript
function createPinia() { const stores = new Map(); const plugins = [];
  return { stores, plugins, use: p => plugins.push(p) }; }
function defineStore(id, setup) {
  return function useStore(pinia = globalPinia) {
    if (pinia.stores.has(id)) return pinia.stores.get(id);
    const listeners = new Set();
    let state = { ...setup() };
    const subscribe = (fn) => { listeners.add(fn);
      return () => listeners.delete(fn); };                  // 4) 立即回放可加 once 参数
    const store = {
      $state: state,
      $patch(partial) { Object.assign(state, partial); notify(); },  // 3) 合并后单次通知
      $subscribe: subscribe,
      $id: id,
    };
    function notify() { listeners.forEach(l => l(state)); }
    pinia.stores.set(id, store);
    pinia.plugins.forEach(p => p({ store, pinia }));        // 5) 插件时序
    return store;
  };
}
const persist = ({ store }) => store.$subscribe(s =>
  localStorage.setItem(store.$id, JSON.stringify(s)));
// 用：const useUser = defineStore('user', () => ({ name: 'a', age: 1 })); pinia.use(persist)
```
