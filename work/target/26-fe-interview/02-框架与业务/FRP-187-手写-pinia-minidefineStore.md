---
title: [FRP-187] 手写 pinia mini：defineStore + 响应式 state + action 怎么组合？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 笔试题, 13]
type: 笔试题
---

## FRP-187：手写 pinia mini：defineStore + 响应式 state + action 怎么组合？

**答**：
- 内核三件套：`defineStore` 生成 useStore 函数；`useStore` 用 inject 拿 Pinia 实例、按 id 创建/复用 store；store 本体是 `reactive(state)` 的对象。
- action 就是普通函数，`this` 通过 `bind(store)` 指向 reactive store——改 state 自动触发依赖它的组件；getters 用 computed 缓存。
- `$patch` 用批量（一次 trigger）、`$reset` 重新执行 options.state 工厂、`$subscribe` 基于 watch 订阅变化（插件/持久化的挂点，见 FRP-078）。
- devtools 与 SSR 略去，但注意 store 必须**挂在 Pinia 实例上**（app 级单例）而不是模块级单例——SSR 与多应用共存的前提。

```javascript
// 简化实现，帮助理解 pinia mini
import { reactive, computed, inject, watch, effectScope } from 'vue';

const piniaSymbol = Symbol('pinia');

function createPinia() {
  const stores = new Map();      // id -> store 实例（app 级单例容器）
  return {
    install(app) { app.provide(piniaSymbol, this); },
    _stores: stores,
    _plugins: [],
    use(plugin) { this._plugins.push(plugin); return this; },
  };
}

function defineStore(id, options) {
  function useStore() {
    const pinia = inject(piniaSymbol);           // 拿 Pinia 实例
    if (!pinia._stores.has(id)) {
      const scope = effectScope();               // 每个 store 独立 scope
      const store = scope.run(() => {
        // 1. state：reactive 包装（core）
        const state = reactive(options.state?.() ?? {});
        // 2. getters：computed 缓存 + this 指向 store
        const getters = {};
        for (const key in options.getters ?? {}) {
          getters[key] = computed(() => options.getters[key].call(proxy));
        }
        // 3. actions：普通函数 bind 到 store
        const actions = {};
        for (const key in options.actions ?? {}) {
          actions[key] = (...args) => options.actions[key].apply(proxy, args);
        }
        const proxy = new Proxy({}, {
          get(_, key) {
            if (key in state) return state[key];       // state 优先
            if (key in getters) return getters[key].value;
            if (key in actions) return actions[key];
            if (key === '$patch') return patchFn;
            if (key === '$reset') return () => Object.assign(state, options.state());
            if (key === '$subscribe') return (cb) =>
              watch(state, (s) => cb({ type: 'patch' }, s), { deep: true });
            return undefined;
          },
          set(_, key, v) { state[key] = v; return true; } // store.count++ 直写 state
        });
        function patchFn(partial) {
          // $patch 函数式：在一个 tick 内多次改也只触发一轮依赖
          if (typeof partial === 'function') partial(state);
          else Object.assign(state, partial);
        }
        return proxy;
      });
      pinia._stores.set(id, store);
      // 4. 插件：拿到 store 上下文（持久化插件等在这里挂）
      pinia._plugins.forEach(p => p({ store, pinia, options }));
    }
    return pinia._stores.get(id);
  }
  useStore.$id = id;
  return useStore;
}

// 使用：
// const useCounter = defineStore('counter', {
//   state: () => ({ count: 0 }),
//   getters: { double: (s) => s.count * 2 },
//   actions: { inc() { this.count++ } },     // this 是 reactive store
// });
// const counter = useCounter();
// counter.inc();          // count++ 自动触发所有依赖组件
// counter.$patch({ count: 10 });
// counter.$subscribe((m, state) => localStorage.setItem('counter', JSON.stringify(state)));
// 与真实 Pinia 的差距：真实实现用 stop/setupStore 分层、devtools 钩子、SSR 序列化——核心思路一致
```
