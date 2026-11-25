---
title: [FRP-078] Pinia 的插件机制如何实现？持久化插件（persist）的原理是什么？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-078：Pinia 的插件机制如何实现？持久化插件（persist）的原理是什么？

**答**：
- 插件是 `pinia.use((context) => {...})` 注册的函数，context 为 `{ store, app, pinia, options }`，在**每个 store 创建时**被调用一次——返回的对象会被 `merge` 进 store（可以添加新 state/方法），这就是"给所有 store 批量加能力"的机制。
- 持久化原理三板斧：初始化时从 `localStorage` 读缓存并 `$patch` 进 state；`store.$subscribe` 订阅任意 state 变化写回 storage（默认 `store.$id` 为 key）；可配 `paths` 只持久化部分字段。
- `$subscribe` 基于内部 watcher：state 是 reactive 对象，订阅其变更回调收到 `(mutation, state)`；`$onAction` 同理可做 action 日志/埋点插件。
- 插件天然组合：同一 store 会被所有插件依次处理，持久化、撤销重做、日志互不干扰。

```javascript
// 简化实现，帮助理解插件机制与 persist 插件
function createPinia() {
  const pinia = { _s: new Map(), _p: [] };
  pinia.use = (plugin) => { pinia._p.push(plugin); return pinia; };
  pinia.createStore = (id, stateFactory) => {
    if (pinia._s.has(id)) return pinia._s.get(id);
    const store = { $id: id, ...reactive(stateFactory()) };
    store.$patch = (partial) => Object.assign(store, partial);
    const subs = new Set();
    store.$subscribe = (fn) => { subs.add(fn); return () => subs.delete(fn); };
    store._trigger = () => subs.forEach((f) => f({ storeId: id }, store));
    pinia._s.set(id, store);
    pinia._p.forEach((p) => p({ store, pinia })); // 创建时依次跑插件
    return store;
  };
  return pinia;
}

// persist 插件：读缓存 -> $patch 注入 -> $subscribe 写回
function persistPlugin({ store, pinia }) {
  const key = `pinia-${store.$id}`;
  const saved = JSON.parse(localStorage.getItem(key) || 'null');
  if (saved) store.$patch(saved);                        // 1. 启动时恢复
  store.$subscribe(() => {                               // 2. 变更写回
    localStorage.setItem(key, JSON.stringify({ n: store.n }));
  });
}

// 日志插件：演示多插件共存
const loggerPlugin = ({ store }) =>
  console.log(`[pinia] store ${store.$id} created`);

const pinia = createPinia();
pinia.use(persistPlugin);
pinia.use(loggerPlugin);

const store = pinia.createStore('cart', () => ({ n: 0 }));
store.$patch({ n: 5 });
store._trigger();                                        // 触发持久化写回
console.log(JSON.parse(localStorage.getItem('pinia-cart'))); // { n: 5 }
// 刷新后：persistPlugin 从 localStorage 恢复 n = 5，实现状态持久
```

## 十二、React Hooks 深入
