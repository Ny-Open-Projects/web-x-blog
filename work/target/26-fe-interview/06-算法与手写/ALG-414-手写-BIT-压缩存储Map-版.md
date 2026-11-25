---
title: [ALG-414] 手写 BIT 压缩存储（Map 版）：稀疏索引
date: 2026-11-21
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-414：手写 BIT 压缩存储（Map 版）：稀疏索引

**答**：
- 题目：ID 空间巨大但活跃 ID 稀疏（百万中千个活跃），统计「ID 前缀区间内的活跃数」。数组 BIT 会爆内存——用 Map 实现 BIT（只存非零节点）。
- 思路：BIT 的节点访问改为 Map get/set（不存在的节点视为 0）；lowbit 逻辑不变。空间 O(活跃数 × log n)。
- 评分点：Map 版 BIT 的节点惰性；空间复杂度对比（n vs k log n）；适用前提（稀疏且查询少全扫）。

```javascript
class SparseBIT {
  constructor(n) { this.n = n; this.t = new Map(); }        // 稀疏 Map 存储
  add(i, v) { for (; i <= this.n; i += i & -i)
    this.t.set(i, (this.t.get(i) ?? 0) + v); }
  sum(i) { let s = 0; for (; i > 0; i -= i & -i) s += this.t.get(i) ?? 0; return s; }
}
// 空间对比：数组 BIT 1e9×8B = 8GB；SparseBIT 仅 O(k log n)，k=活跃数
// 注意：sum(i) 沿路径访问 O(log n) 个节点，稀疏 Map 查询常数略高（哈希开销）
```
