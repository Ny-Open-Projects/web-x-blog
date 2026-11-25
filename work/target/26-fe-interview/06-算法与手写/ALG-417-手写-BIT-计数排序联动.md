---
title: [ALG-417] 手写 BIT 计数排序联动：分布直方图增量
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-417：手写 BIT 计数排序联动：分布直方图增量

**答**：
- 题目：年龄段分布直方图（0~100 岁），持续插入年龄，查「任意年龄段区间的用户数」并支持「某条记录修正」。值域即桶：BIT 直接建 101 桶。
- 思路：BIT[age] = 该岁人数；区间查 = range(l, r)；修正 = 先减旧再加新。100 桶太小可直接数组——但值域到 1 万（精确月龄）时 BIT 的 O(log) 查询有意义。
- 评分点：桶即下标；修正的两步更新；小值域数组 vs 大值域 BIT 的取舍。

```javascript
class AgeHistogram {
  constructor(maxAge = 10000) { this.max = maxAge; this.bit = new BIT(maxAge);
    this.records = new Map(); }                             // userId -> age
  upsert(userId, age) {
    const old = this.records.get(userId);
    if (old != null) this.bit.add(old, -1);                 // 修正：先减旧
    this.bit.add(age, 1); this.records.set(userId, age);
  }
  countRange(lo, hi) { return this.bit.range(lo, hi); }     // 年龄段人数
  total() { return this.records.size; }
  medianAge() {                                             // 中位年龄（倍增 kth）
    const k = Math.ceil(this.total() / 2);
    let pos = 0;
    for (let pw = 1 << 15; pw > 0; pw >>= 1) {
      const next = pos + pw;
      if (next <= this.max && this.bit.sum(next) < k) pos = next;
    }
    return pos + 1;
  }
}
```
