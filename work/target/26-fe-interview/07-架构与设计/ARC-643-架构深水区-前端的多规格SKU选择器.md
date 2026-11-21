---
title: [ARC-643] 多规格 SKU 选择器（组合合法/库存联动）的前端架构如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-643：多规格 SKU 选择器
**答**:
- 数据模型：规格维度（颜色/尺码）× 规格值 → SKU 矩阵（组合 → skuId/价格/库存——ARC-617 矩阵预下发）；组合合法性（无效组合置灰：该规格值与其他已选值无 SKU——合法路径计算：图遍历或矩阵预计算）。
- 交互策略：任意顺序选（先选尺码后选颜色也可——合法性按当前选择集计算）、库存联动（选完 → 库存/价格/优惠切换；部分规格无库存 → 置灰 + 可选（提示无货）——到货通知入口）、换规格保留数量语义（数量重置 vs 保持——库存约束）。
- 性能：大规格矩阵（100+ SKU）——矩阵压缩传输 + 端上索引（规格值组合 hash → sku O(1)）。
- 无障碍：规格组 role=radiogroup（单选语义 per 维度）、置灰项 aria-disabled 原因朗读。
- 边界：单规格商品（跳过选择器）、规格图与主图联动（选颜色 → 头图切换）、价格区间（未选完显示价格区间——选完显示精确价）。
```javascript
// SKU 合法路径
function validOptions(selected) {                                 // 已选部分规格
  return matrix.filter(sku => matchesPartial(sku, selected));     // 剩余可选规格值集合
}
const sku = matrixByHash(hashKey(selected));                      // O(1) 命中
onSelect(dim, val) => update selected → recompute valid/stock/price → render states
```
