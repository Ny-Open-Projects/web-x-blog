---
title: [ZSM-032] Zustand 切片之间有依赖（下单要同时扣库存和积分）怎么设计？怎么避免循环引用？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-032：Zustand 切片之间有依赖（下单要同时扣库存和积分）怎么设计？怎么避免循环引用？
**答**：
- 切片在同一 store 内时，通过 `get()` 直接跨切片读写，这是切片模式的核心优势。
- 循环引用发生在**拆成多个独立 store** 且互相 import actions 时（A import B，B import A）；解法是抽公共编排层（service/流程函数）统一调度，store 之间不互相 import。
- 设计原则：切片只管本域状态，业务流程（下单 = 扣库存 + 扣积分 + 写日志）放在流程层，按序调用各 store 的 actions。
- 若必须单 store，把跨域 action 放在组合后的 store 里定义（在 create 工厂里先合并切片再补编排 actions）。

```javascript
// 流程层：store 间零 import 循环
export async function checkout(orderId) {
  const stock = useStockStore.getState()
  if (!stock.enough(orderId)) throw new Error('库存不足')
  await useOrderStore.getState().create(orderId)   // 先建单
  useStockStore.getState().deduct(orderId)          // 再扣库存
  usePointsStore.getState().add(orderId)            // 最后积分
}
```
