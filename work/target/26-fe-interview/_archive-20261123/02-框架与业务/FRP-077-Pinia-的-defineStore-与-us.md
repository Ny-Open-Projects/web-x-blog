---
title: [FRP-077] Pinia 的 defineStore 与 useStore 是怎么实现的？为什么不用 Symbol inject 也能拿到 store？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-077：Pinia 的 defineStore 与 useStore 是怎么实现的？为什么不用 Symbol inject 也能拿到 store？

**答**：
- `defineStore(id, setup)` **只定义不创建**：返回一个 `useStore` 函数；真正的 store 在**第一次调用 useStore 时才创建**（惰性单例）。
- useStore 内部：从当前组件实例 `inject(piniaSymbol)` 拿到 **pinia 实例**（app.use(pinia) 时 `provide` 进去），查 `pinia._s.has(id)`——已创建直接返回缓存；没有则 `createSetupStore`/`createOptionsStore` 创建并 `pinia._s.set(id, store)`。
- store 本体 = `reactive({ ...state })` + getters（computed 包装）+ actions（函数直接挂上，内部用 `activePinia/currentInstance` 定位）+ `$patch/$reset/$subscribe/$onAction` 等方法。
- useStore 能在组件外用是靠 `getActivePinia()`（setActivePinia 维护的模块级变量）；不用 Symbol 字符串拿是因为 Vue 的 inject 需要组件上下文，pinia 把"容器注入"与"store 单例"两层分离。

```javascript
// 简化实现，帮助理解 defineStore -> useStore 的注入与单例
function createPinia() {
  const pinia = {
    _s: new Map(),        // id -> store 单例缓存
    _p: [],               // 插件列表
    install(app) {
      app.provide(piniaSymbol, pinia); // 应用级 provide，所有组件可 inject
    },
  };
  return pinia;
}
const piniaSymbol = Symbol('pinia');

function defineStore(id, setup) {
  function useStore() {
    // 组件内：inject 拿容器；组件外：getActivePinia 兜底
    const pinia = currentInstance?.[piniaSymbol] || activePinia;
    if (!pinia._s.has(id)) {
      // 惰性创建：state 用 reactive，getters 用 computed 缓存
      const state = reactive(setup.state ? setup.state() : {});
      const store = { $id: id, ...state };
      for (const [k, g] of Object.entries(setup.getters || {})) {
        Object.defineProperty(store, k, {
          get: () => g(store),        // computed 的简化形态：按需求值
        });
      }
      for (const [k, a] of Object.entries(setup.actions || {})) {
        store[k] = (...args) => a(store, ...args);
      }
      pinia._s.set(id, store);        // 单例注册
      pinia._p.forEach((p) => p({ store, pinia })); // 插件在创建时介入
    }
    return pinia._s.get(id);
  }
  useStore.$id = id;
  return useStore;
}

let activePinia = null;
let currentInstance = null;

// 用法演示
const useCounter = defineStore('counter', {
  state: () => ({ n: 0 }),
  getters: { double: (s) => s.n * 2 },
  actions: { inc() { this.n++; } },
});
activePinia = createPinia();
const store = useCounter();
store.inc();
console.log(store.n, store.double); // 1 2
console.log(useCounter() === store); // true：同 id 返回同一单例
```
