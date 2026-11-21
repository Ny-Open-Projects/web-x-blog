---
title: [ALG-050] 购物车"凑单"功能：给定商品价格数组与目标满减金额 X，找出"两件商品价格之和恰好为 X"的组合并高亮。如何 O(n) 求解两数之和的变体？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-050：购物车"凑单"功能：给定商品价格数组与目标满减金额 X，找出"两件商品价格之和恰好为 X"的组合并高亮。如何 O(n) 求解两数之和的变体？
**答**：一次遍历 + 哈希：对每个商品算 `need = X - price`，若 need 已在 Map 中说明之前的商品能与它凑单，直接返回组合；否则把 `price -> 商品` 存入。相比暴力双循环 O(n²) 大幅提速。时间 O(n)，空间 O(n)。

```javascript
function findCombo(items, target) {
  const seen = new Map(); // price -> item
  for (const item of items) {
    const need = target - item.price;
    if (seen.has(need)) return [seen.get(need), item];
    seen.set(item.price, item); // 注意：先查后存，避免同一商品配自己
  }
  return null; // 找不到可退化为"最接近 target"的两件：排序 + 双指针
}
```
