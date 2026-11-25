---
title: [WCN-628] 细粒度 Signal 更新与 VDOM diff 各自适合什么场景，如何取舍？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-628：细粒度 Signal 更新与 VDOM diff 各自适合什么场景，如何取舍？

**答**：
- 结论：VDOM 适合「树结构频繁变化、开发心智负担低」的业务；细粒度 Signal 适合「高频局部更新、大体量列表」的性能敏感场景。
- 机制：VDOM 每次状态变重建虚拟树再 diff（成本与树大小相关）；Signal 在依赖收集阶段就绑定 DOM 节点（更新成本与变化量相关）。
- 追问钩子：为什么大列表用 Signal 优势明显？因为改一项只更新对应行节点，无需 diff 整棵列表——引出列表 keyed 更新话题。

```javascript
// 同一「计数器列表」，两种范式的更新范围对比
// VDOM 范式：count 变 → 整个列表 render 函数重跑 + diff
function VdomList({ items }) {
  return items.map(i => `<div>${i}</div>`).join(''); // 每次全量生成
}
// Signal 范式：每个 item 绑定自己的 effect
function signalList(items) {
  return items.map(v => {
    const s = signal(v);
    const div = document.createElement('div');
    effect(() => { div.textContent = s.get(); });
    return { el: div, set: s.set };
  });
}
const rows = signalList([1, 2, 3]);
rows[1].set(20); // 只更新第 2 行的 DOM，其他行零开销
```
