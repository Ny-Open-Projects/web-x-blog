---
title: [ALG-410] 手写 BIT 惰性重建：数据分代统计
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-410：手写 BIT 惰性重建：数据分代统计

**答**：
- 题目：统计场景数据分代（每小时一批新数据），查询要「合并所有完整批次 + 当前批」，当前批频繁变化——完整批次冻结为前缀数组，当前批用 BIT，查询 = 前缀和 + BIT 查询，批切换时惰性重建。
- 思路：frozenPrefix[i] = 已冻结批次累计（数组直接前缀和 O(1) 查）；currentBatch 用 BIT（支持增删）；整点切换：BIT 内容并入 frozenPrefix，BIT 清零（惰性：下个查询触发）。
- 评分点：分代冻结思想；重建惰性触发；避免全量重建的停顿。

```javascript
class GenerationalStats {
  constructor(n) { this.n = n; this.frozen = new Array(n + 1).fill(0);
    this.bit = new BIT(n); this.pending = false; }
  add(i, v) { this.bit.add(i, v); }                         // 当前批写入
  rollGeneration() { this.pending = true; }                  // 批切换（惰性）
  rollNow() {                                               // 合并 BIT → frozen
    for (let i = 1; i <= this.n; i++) this.frozen[i] += this.bit.sum(i) - this.bit.sum(i - 1);
    this.bit = new BIT(this.n); this.pending = false;
  }
  query(i) {
    if (this.pending) this.rollNow();                        // 惰性重建触发
    return this.frozen[i] + this.bit.sum(i);                 // 冻结 + 当前批
  }
}
```
