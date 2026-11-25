---
title: [ALG-412] 手写 BIT 多实例协同：多维度看板
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-412：手写 BIT 多实例协同：多维度看板

**答**：
- 题目：看板同屏多指标（PV/UV/转化），每个指标一棵 BIT（按时间桶），插入时同步更新所有 BIT，查询各自区间。多 BIT 一致性管理。
- 思路：BITs = Map<metric, BIT>；insert 遍历所有 metric 更新；查询按 metric 取。工程点：BIT 实例惰性创建（冷指标不占内存）。
- 评分点：惰性实例化；一致性（同事务更新多 BIT）；按 metric 分片。

```javascript
class DashboardBITs {
  constructor(n) { this.n = n; this.bits = new Map(); }     // metric -> BIT
  bit(metric) {                                             // 惰性创建
    return this.bits.get(metric) ?? this.bits.set(metric, new BIT(this.n)).get(metric);
  }
  insert(time, metrics) {                                   // 一次插入更新多 BIT
    for (const [m, v] of Object.entries(metrics)) this.bit(m).add(time, v);
  }
  range(metric, l, r) { return this.bit(metric).range(l, r); }
  snapshot() {                                              // 降级导出
    return Object.fromEntries([...this.bits].map(([m, b]) =>
      [m, Array.from({ length: this.n }, (_, i) => b.range(i + 1, i + 1))]));
  }
}
```
