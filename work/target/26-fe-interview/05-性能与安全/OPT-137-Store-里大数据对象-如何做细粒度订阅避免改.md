---
title: [OPT-137] Store 里大数据对象，如何做细粒度订阅避免"改一个字段全组件重渲"？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-137：Store 里大数据对象，如何做细粒度订阅避免"改一个字段全组件重渲"？

**答**：
- 问题本质：订阅粒度 = store 整体时，任何字段变化都通知所有订阅者。
- 三个层级的解法：①选择器（useSelector 传等值比较函数，只取所需字段）；②原子化 store（zustand/Jotai 按字段拆 store，天然细粒度）；③ Proxy 依赖追踪（Valtio，读哪个字段记哪个字段）。
- 选择器必须配合稳定引用：返回新对象/新数组的 selector 要用 `createSelector` 类记忆化，否则引用每次都变照样重渲。
- 深层列表场景：selector 直接定位到 `items[i].sub[j]`，上层节点变化不触发订阅该叶子节点的组件。

```javascript
// 一一对应：细粒度选择器 + 记忆化，只有真正依赖的叶子变化才重渲
import { createSelector } from 'reselect';
import { useSyncExternalStore } from 'react';

const store = {
  state: { cart: { items: [{ id: 1, qty: 2 }], coupon: null }, ui: { theme: 'light' } },
  listeners: new Set(),
  subscribe(fn) { this.listeners.add(fn); return () => this.listeners.delete(fn); },
  setState(patch) { this.state = { ...this.state, ...patch }; this.listeners.forEach(f => f()); },
};

// 粗粒度（反例）：useStore(s => s) —— cart 任何变化都重渲
// 细粒度：只订阅 qty，coupon/ui 变化与本组件无关
const selectQty = createSelector(
  [s => s.cart.items],
  items => items.reduce((n, it) => n + it.qty, 0) // 输入引用不变则返回上次结果
);

function useStore(selector) {
  return useSyncExternalStore(
    cb => store.subscribe(cb),
    () => selector(store.state),
    () => selector(store.state)
  );
}

function CartBadge() {
  const total = useStore(selectQty); // 只有 qty 总和变化才触发重渲
  return <span className="badge">{total}</span>;
}
```
