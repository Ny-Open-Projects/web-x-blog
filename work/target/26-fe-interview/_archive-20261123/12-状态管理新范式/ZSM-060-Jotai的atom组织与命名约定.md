---
title: [ZSM-060] 项目里 atom 越来越多怎么组织？Jotai 的文件结构和命名有什么推荐？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-060：项目里 atom 越来越多怎么组织？Jotai 的文件结构和命名有什么推荐？
**答**：
- 按业务域聚合成「atom 模块」文件：`atoms/cart.ts` 里集中定义基础 atom、派生 atom、write-only action，导出只留必要入口，内部 atom 不导出。
- 命名约定：数据 atom 名词（`cartItemsAtom`）、派生 `xxxAtom` 与基础区分注释、action 动词（`checkoutAtom`）。
- 派生只读不导出 setter：用 useAtomValue 消费；可写 action 单独导出，防止误写。
- 依赖方向单向：页面 atom 可依赖全局 atom，反向禁止；用 eslint 边界规则兜底。
- 团队关键点：atom 数量爆炸时先问「是不是把组件私有态也 atom 化了」，先删再拆。

```javascript
// atoms/cart.ts
const cartItemsBase = atom([])          // 私有基础
export const cartItemsAtom = cartItemsBase
export const cartTotalAtom = atom(g => g(cartItemsBase).reduce((s, i) => s + i.price, 0))
export const addItemAtom = atom(null, (g, s, item) => s(cartItemsBase, xs => [...xs, item]))
export const checkoutAtom = atom(null, async (g, s) => {
  await api.checkout(g(cartItemsBase))
  s(cartItemsBase, [])
})
```
