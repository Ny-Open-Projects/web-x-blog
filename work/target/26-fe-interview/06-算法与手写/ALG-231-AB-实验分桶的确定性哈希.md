---
title: [ALG-231] AB 实验：把用户稳定分到实验桶（确定性哈希 + 分桶不重叠 + 互斥实验域）
date: 2026-11-19
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---
## ALG-231：AB 实验：把用户稳定分到实验桶（确定性哈希 + 分桶不重叠 + 互斥实验域）
**答**：多实验并行（实验 A 占 10%、实验 B 占 20%），要求：同一用户分桶稳定（会话一致）；实验间互斥或正交可控；分桶比例调整时不引起大规模用户换桶（residual hashing 思想）。

**思路**：hash(userId + experimentId) % 10000 落段；互斥实验用同一 hash 段位（分段不重叠）；正交实验用不同盐（hash 域独立，各实验独立随机）。

```javascript
function bucket(userId, experimentId, salt = '') {
  let h = 2166136261;
  const s = `${experimentId}:${salt}:${userId}`;    // 实验域隔离：加 experimentId 盐
  for (const ch of s) { h ^= ch.charCodeAt(0); h = Math.imul(h, 16777619); }
  return (h >>> 0) % 10000;                          // 0..9999
}
function assign(userId, experiment, { ranges, orthogonal = false }) {
  // ranges: [{ start, end, bucket: 'treatment' }, ...] 按万分比
  const v = bucket(userId, experiment.id, orthogonal ? experiment.salt : '');
  const hit = ranges.find((r) => v >= r.start && v < r.end);
  return hit ? hit.bucket : 'control';
}
// 互斥实验：共用 hash 段位（A 占 0-999，B 占 1000-2999）——互不重叠
// 正交实验：不同 salt → 各自独立随机（A 的实验组里 B 均匀分布）——分层交叉分析可行
// 稳定性：同用户同实验永远同桶（确定性）；比例 10%→12% 扩量时老桶用户大概率留原桶
// （扩大段位覆盖老段位）—— 段位扩展而不是重排
```

**评分点**：
- 确定性哈希分桶（同用户永远同桶）——会话一致性的实现核心。
- 互斥（共享段位不重叠）与正交（独立盐）两种实验关系的实现差异。
- 扩量时"扩段位"保持老用户不换桶的意识。
- hash 用 FNV 类（不是 Math.random）。
