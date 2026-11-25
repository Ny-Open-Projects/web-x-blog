---
title: [ALG-401] 手写 BIT 多维计数：双条件累计
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-401：手写 BIT 多维计数：双条件累计

**答**：
- 题目：订单记录 (城市, 类目)，查「某城市+某类目」的订单数并支持实时插入。二维计数：城市×类目 组合键 + BIT 按序（或 Map 组合计数即可）。
- 思路：维度固定时直接 Map<city|cat, count>（O(1)）；若需「前缀城市 + 类目」类查询 → 按城市离散化建 per-类目 BIT。维度≤2 可 BIT，≥3 退化。
- 评分点：维度小用 Map 直查；BIT 只在「有序前缀语义」时需要；多维退化认知。

```javascript
class CityCategoryCounter {
  constructor() { this.direct = new Map(); this.perCat = new Map(); }
  add(city, cat) {                                          // 实时插入
    const k = city + '|' + cat;
    this.direct.set(k, (this.direct.get(k) ?? 0) + 1);
    (this.perCat.get(cat) ?? this.perCat.set(cat, new BIT(1000)).get(cat))
      .add(cityId(city), 1);                                // per-类目 BIT（前缀城市语义）
  }
  count(city, cat) { return this.direct.get(city + '|' + cat) ?? 0; }   // 精确双条件 O(1)
  prefixByCat(cat, cityUpper) {                             // 城市 ID 前缀统计
    return this.perCat.get(cat)?.sum(cityUpper) ?? 0;
  }
}
// 认知：维度组合计数直接 Map；「前缀语义」才需要 BIT；三维以上 BIT 套娃不划算
```
