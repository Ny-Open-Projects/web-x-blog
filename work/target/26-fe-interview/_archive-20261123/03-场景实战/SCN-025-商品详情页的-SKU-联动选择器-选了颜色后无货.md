---
title: [SCN-025] 商品详情页的 SKU 联动选择器（选了颜色后无货尺码自动置灰）怎么设计？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-025：商品详情页的 SKU 联动选择器（选了颜色后无货尺码自动置灰）怎么设计？
**答**：
- 数据模型：每条 SKU 记录是"属性组合 + 库存"，如 color=红 & size=M & stock=3。
- 联动算法：选择状态变化时，对每个未选维度做可解性检测——固定其余已选维度，枚举该维度每个取值是否存在有库存的组合，无解则置灰。
- 全部维度选完后命中唯一 SKU 记录，取其价格与库存；数据量小直接 some/every 检索即可。

```typescript
interface Sku {
  attrs: Record<string, string>; // 例如 { color: '红', size: 'M' }
  stock: number;
}

// 判断某维度的某个取值是否可选：固定已选维度后，仍需存在有库存的组合
function isOptionDisabled(
  skus: Sku[],
  selected: Record<string, string>, // 当前已选，如 { color: '红', size: '' }
  dim: string,
  val: string,
): boolean {
  return !skus.some((sku) =>
    sku.stock > 0 &&
    sku.attrs[dim] === val &&
    Object.entries(selected).every(([k, v]) => !v || sku.attrs[k] === v),
  );
}

// 全部维度都有值时命中唯一 SKU
function matchSku(skus: Sku[], selected: Record<string, string>) {
  return skus.find((s) =>
    s.stock > 0 &&
    Object.entries(selected).every(([k, v]) => v && s.attrs[k] === v),
  );
}
```

## 七、权限与安全
