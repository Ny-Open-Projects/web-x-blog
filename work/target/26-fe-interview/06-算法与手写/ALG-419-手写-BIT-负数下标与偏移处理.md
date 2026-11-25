---
title: [ALG-419] 手写 BIT 负数下标与偏移处理：相对偏移统计
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-419：手写 BIT 负数下标与偏移处理：相对偏移统计

**答**：
- 题目：数据含负数下标（如温度 -50~50、相对偏移 -1e5~1e5），BIT 只支持 1-based 正数——统一偏移（offset 变换）解决。
- 思路：建 BIT 时下标 = 原值 + OFFSET（OFFSET = 负界绝对值 + 1）；查询端点同样偏移。所有「负下标报错」的坑一次说清。
- 评分点：OFFSET 偏移变换；1-based 约定；端点也要偏移（查询漏移是高频 bug）。

```javascript
class OffsetBIT {
  constructor(minVal, maxVal) {
    this.offset = 1 - minVal;                               // 最小值映射到 1
    this.n = maxVal + this.offset;
    this.bit = new BIT(this.n);
  }
  idx(v) { return v + this.offset; }                        // 偏移变换
  add(v, count) { this.bit.add(this.idx(v), count); }       // 负数下标安全
  countRange(lo, hi) { return this.bit.range(this.idx(lo), this.idx(hi)); }
}
// 例：温度统计 new OffsetBIT(-50, 50) → add(-30, 1) 内部走 idx(-30)=21
// 坑点清单：查询端点必须同样偏移；BIT 永远 1-based；lowbit(0) 死循环防护
```
