---
title: [SCN-413] 笔试题——实现商品 SKU 选择器（规格联动/置灰/价格更新）？
date: 2026-11-20
categories: [场景实战]
tags: [前端面试, 笔试题, 场景实战]
type: 笔试题
---

## SCN-413：手写 SKU 选择器：多规格联动、无货置灰、价格数量更新

**需求与边界**：
- 输入：规格列表（颜色/尺码）、SKU 组合表（规格组合→{price, stock, skuId}）；输出：选择状态。
- 边界要求：① 已选规格的组合查询（部分选择也要判定可售性）；② 不可售组合置灰（其余规格的可选范围随已选联动收窄）；③ 全选→价格/库存更新；④ 无货可切换规格不锁死。

**答**：
```javascript
class SkuSelector {
  constructor(skus, specs) {
    this.skus = skus;                          // [{spec:{color, size}, stock, price}]
    this.specs = specs;                        // [{key:'color', values:[...]}]
    this.selected = {};                        // {color:'红'}
  }
  combinations(partial) {                      // 部分选择的组合匹配
    return this.skus.filter(s =>
      Object.entries(partial).every(([k, v]) =>
        !v || s.spec[k] === v));
  }
  isOptionDisabled(specKey, value) {
    const trial = { ...this.selected, [specKey]: value };
    return this.combinations(trial)
      .reduce((s, x) => s + x.stock, 0) === 0;   // 无任何库存→置灰
  }
  select(specKey, value) {
    this.selected[specKey] = value;
    // 清除被禁用的下游选择（联动收窄后当前选择失效）
    for (const s of this.specs) {
      if (s.key === specKey) continue;
      const cur = this.selected[s.key];
      if (cur && this.isOptionDisabled(s.key, cur))
        delete this.selected[s.key];             // 自动取消失效选择
    }
    return this.state();
  }
  state() {
    const matched = this.combinations(this.selected);
    const exact = matched.length === 1 &&
      Object.keys(this.selected).length === this.specs.length
      ? matched[0] : null;
    return {
      selected: { ...this.selected },
      disabled: Object.fromEntries(this.specs.map(s =>
        [s.key, s.values.map(v => this.isOptionDisabled(s.key, v))])),
      price: exact?.price, stock: exact?.stock,
      skuId: exact?.skuId,                       // 全选→精确 SKU
    };
  }
}
```

**评分点**:
- 部分选择组合查询（combinations 容忍未选维度）——联动判定正确。
- 置灰判定基于"组合库存和=0"，且随已选动态收窄。
- 选择失效的下游自动清除（切换规格不锁死）。
- 全选匹配唯一 SKU 输出价格/库存/skuId。
