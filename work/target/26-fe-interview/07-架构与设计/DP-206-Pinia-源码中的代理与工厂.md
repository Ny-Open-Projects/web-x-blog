---
title: [DP-206] 源码识别：Pinia 源码中的工厂与上下文注入？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-206：源码识别：Pinia 源码中的工厂与上下文注入？
**答**：
- 工厂+单例容器：defineStore 是工厂（返回 useStore），createPinia 是单例容器（全局 pinia 实例持有 stores Map，同名 store 只创建一次）。
- 依赖注入：useStore 里 inject(piniaSymbol) 拿容器——Flutter/组件化的 provide/inject 模式；SSR 下每个请求一个 pinia 实例（作用域化单例）。
- 组合+备忘录：store 由 state/ref + getters(computed 备忘录) + actions 组成；getter 的 computed 是 Vue 级备忘录（依赖变了才重算）。
- 插件化：pinia.use(plugin) 注册扩展（持久化/日志），插件拿到 context（store/api）——观察者（订阅 $patch）与装饰（包装 actions）混合。

```javascript
// Pinia 简化源码
function createPinia() {
  const stores = new Map();                    // 单例容器
  const plugins = [];
  return { stores, plugins, use(p) { plugins.push(p); } };
}
function defineStore(id, setup) {              // 工厂
  function useStore() {
    const pinia = inject(piniaSymbol);         // 依赖注入
    if (!pinia.stores.has(id)) {               // 单例化
      const store = reactive({});              // 代理
      setup(ctx).forEach(([k, v]) => store[k] = v);
      pinia.plugins.forEach(p => p({ store, pinia }));   // 插件装饰/观察
      pinia.stores.set(id, store);
    }
    return pinia.stores.get(id);
  }
  useStore.$id = id;
  return useStore;
}
```
