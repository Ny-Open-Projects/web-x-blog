---
title: [DP-009] 为什么说 ES Module 是"天然单例"？
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-009：为什么说 ES Module 是"天然单例"？
**答**：
- 模块在首次被 import 时执行一次，其导出（对象/类/函数）被所有导入方共享同一份引用——这正好满足单例语义。
- 推论：`export const store = createStore()` 不需要任何 getInstance 代码，模块系统就是单例容器。
- 注意边界：单例的是"模块实例"，不是"类实例"——如果导出的是 class，每次 new 仍会产生多实例。
- 面试延伸：单例 + 惰性创建在模块化下可用"动态 import"实现按需加载。

```javascript
// store.js —— 模块顶层只执行一次
let state = 0;
const listeners = new Set();
export const store = {
  setState(next) {
    state = next;
    listeners.forEach((fn) => fn(state)); // 变更后通知所有订阅者（观察者）
  },
  subscribe(fn) { listeners.add(fn); return () => listeners.delete(fn); },
  getState: () => state,
};

// a.js 与 b.js 各自导入，拿到的是同一份实例
// a.js: import { store } from './store.js';
// b.js: import { store } from './store.js';
// main.js 验证：
// import { store as s1 } from './store.js';
// import { store as s2 } from './store.js';
// console.log(s1 === s2); // true —— 模块缓存保证了单例

// 若导出的是 class，则不再是单例，要克制 new
export class Service {}
// new Service() !== new Service() —— 常见踩坑
// 需要惰性加载的单例：动态 import
export async function getHeavyStore() {
  const { HeavyStore } = await import('./heavy-store.js'); // 首次调用才加载模块
  return HeavyStore.getInstance();
}
```
