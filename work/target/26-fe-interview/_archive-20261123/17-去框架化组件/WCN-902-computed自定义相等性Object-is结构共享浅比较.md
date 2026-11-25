---
title: [WCN-902] computed 默认用 Object.is 比较，对象/数组每次都触发更新，怎么自定义相等性
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-902：computed 默认用 Object.is 比较，对象/数组每次都触发更新，怎么自定义相等性

**答**：
- 结论先行：Signals 的 computed 默认用 Object.is 判定值是否变化，返回新对象引用必然被视为变化，导致下游 effect 反复执行。
- 解法一是「结构共享 / 稳定引用」：用 Immer 或手写只在字段真变时返回新对象，否则返回旧引用，让 Object.is 自然命中。
- 解法二是给 computed 传自定义相等函数（部分库支持 `computed(fn, { equals })`），用浅比较或 lodash.isEqual 做值语义比较，引用变了但内容相同则不触发。
- 深比较有成本：对大对象用 JSON.stringify 或深比较可能比多跑一次 effect 更贵，要按「比较成本 vs 下游重算成本」权衡（商品 SKU 列表常用浅比较 + 关键字段）。
- 追问钩子：追问「自定义 equals 会不会漏掉嵌套字段变化」——答：值语义比较按你实现的深度生效，浅比较会漏深层字段，需明确约定不可变更新。

```javascript
// 自定义相等函数的 computed（伪实现，示意 equals 判定）
import { signal, computed } from '@preact/signals-core';
const list = signal([{ id: 1, qty: 1 }]);

function shallowArrayEq(a, b) {
  return a.length === b.length && a.every((x, i) => x === b[i]);
}
// 假设 computed 支持 { equals }
const total = computed(() => list.value.reduce((s, x) => s + x.qty, 0));
const snapshot = computed(() => list.value.map(x => ({ ...x })), { equals: shallowArrayEq });

list.value = list.value.map(x => ({ ...x })); // 内容相同、引用不同
console.log(snapshot.value); // equals 命中，不触发下游
```
