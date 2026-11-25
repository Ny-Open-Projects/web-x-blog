---
title: [WCN-264] Signals（细粒度可变）与不可变状态（Redux/Immutable）的互操作与选型？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-264：Signals（细粒度可变）与不可变状态（Redux/Immutable）的互操作与选型？
**答**：
- 互操作：不可变 store 的「选中切片」适配成 signal（store.subscribe → signal.set）——两世界桥接。
- 选型：高频局部更新选 signals（省 diff）；强审计/时间旅行需求选不可变（快照天然）。
- 混用风险：同一数据双源（signal + store 各一份）——必须单向同步（store 是唯一事实源，signal 是投影）。
- 演进：新模块用 signals，旧 Redux 数据桥接投影，逐域迁移。

```javascript
// Redux → signal 投影桥
const priceSignal = signal(0);
store.subscribe(() => {
  const v = selectPrice(store.getState());
  if (priceSignal.value !== v) priceSignal.value = v;   // 单向：store → signal
});
r
```
