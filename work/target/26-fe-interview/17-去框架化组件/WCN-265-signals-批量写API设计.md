---
title: [WCN-265] 信号库的批量写 API 设计（batch/update/setAll）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-265：信号库的批量写 API 设计（batch/update/setAll）？
**答**：
- batch(fn)：事务包裹（最小原语）。
- update(sig, updater)：函数式更新（基于旧值），避免读-改-写竞态。
- setAll({sig1: v1, ...})：声明式批量（对象字面量一目了然）。
- 组合：setAll 内部就是一次 batch——API 语义一致。

```javascript
update(cart, items => [...items, newItem]);      // 基于旧值
setAll({ cart: newItems, ui: { drawer: 'open' } });  // 声明式批量 = 一次 flush
r
```
