---
title: [ZSM-152] Zustand 里怎么存「关联实体」？归一化（.byId + .allIds）和嵌套对象怎么选？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-152：Zustand 里怎么存「关联实体」？归一化（.byId + .allIds）和嵌套对象怎么选？
**答**：
- 嵌套结构（order.items[].goods）的问题：改一条商品要逐层展开重建引用，selector 粒度粗、更新成本高、容易整棵树重渲染。
- 归一化结构：`byId: { [id]: entity }` + `allIds: string[]`（或按关系分表），更新只重建对应实体的引用，selector `s.byId[id]` 粒度天然对齐。
- 关系数据拆「事实表」：goods 表 + cart 关系表（goodsId + qty），购物车数量变化不动 goods；派生展示数据（小计）放 selector 现算，不冗余存储。
- 选型边界：层级浅、只读展示用嵌套够了；要跨视图共享实体、频繁局部更新就用归一化——和 127 的服务端缓存归一化是同一思想在客户端层的应用。

```javascript
const useShopStore = create((set, get) => ({
  goods: { byId: { g1: { id: 'g1', price: 99, name: '键盘' } },
           allIds: ['g1'] },
  cart: [{ goodsId: 'g1', qty: 2 }],              // 关系表，不含实体副本

  updateGoods: (id, patch) => set((s) => ({
    goods: {
      ...s.goods,
      byId: { ...s.goods.byId, [id]: { ...s.goods.byId[id], ...patch } },
    },
  })),                                             // 只重建单个实体引用

  changeQty: (goodsId, qty) => set((s) => ({
    cart: s.cart.map(i => i.goodsId === goodsId ? { ...i, qty } : i),
  })),
}))

// 派生：selector 现算小计，不存冗余字段
export const selectCartTotal = (s) =>
  s.cart.reduce((sum, i) =>
    sum + s.goods.byId[i.goodsId].price * i.qty, 0)
```
