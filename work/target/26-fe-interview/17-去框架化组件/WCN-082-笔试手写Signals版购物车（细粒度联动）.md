---
title: [WCN-082] 笔试：手写 Signals 版购物车（总额/数量/减免细粒度联动）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Signals]
type: 笔试题
---

## WCN-082：笔试：手写 Signals 版购物车

**题目**：① `items` 为 signal（数组，元素 `{ id, name, price, qty }`）；② `totalCount / totalPrice / discount` 均 computed（满 300 减 30，满 3 件减运费）；③ `bindList` 式渲染：qty 修改只更新对应行与汇总文本，不重建列表；④ 删除、清空接口；⑤ 快照 `toJSON` 供提交。

**答**：

```javascript
import { createSignal, computed } from './mini.js';
import { bindList } from './w73.js';

export function createCart(container, rowTpl) {
  const [items, setItems] = createSignal([]);

  const totalCount = computed(() => items().reduce((s, i) => s + i.qty, 0));
  const subtotal = computed(() => items().reduce((s, i) => s + i.price * i.qty, 0));
  const discount = computed(() => subtotal() >= 300 ? 30 : 0);
  const freeShip = computed(() => totalCount() >= 3);
  const totalPrice = computed(() => subtotal() - discount() + (freeShip() ? 0 : 10));

  // 细粒度绑定：列表 keyed 复用（WCN-073），汇总文本独立 effect
  const stopList = bindList(container, items,
    (el, it) => { el ??= document.createElement('div'); el.textContent = `${it.name} ×${it.qty} ¥${it.price * it.qty}`; return el; },
    (it) => it.id);
  const stops = [effect(() => { document.querySelector('#sum').textContent = `¥${totalPrice()}`; })];

  const api = {
    add(it) { setItems([...items(), { qty: 1, ...it }]); },
    setQty(id, qty) {
      setItems(items().map((i) => i.id === id ? { ...i, qty } : i)); // 不可变更新
    },
    remove(id) { setItems(items().filter((i) => i.id !== id)); },
    clear() { setItems([]); },
    toJSON() { return { items: items(), total: totalPrice(), discount: discount() }; },
    destroy() { stopList(); stops.forEach((s) => s()); },
  };
  return api;
}
// setQty 只让受影响的 computed（totalCount/subtotal 链）重算，行 DOM keyed 复用
```

**评分点**：
- computed 分层（subtotal→discount→totalPrice），依赖链清晰且惰性。
- 不可变更新触发正确（map/filter 返回新数组）。
- bindList keyed 复用：qty 修改不重建整表。
- toJSON 与 destroy 接口完整（提交与清理）。
