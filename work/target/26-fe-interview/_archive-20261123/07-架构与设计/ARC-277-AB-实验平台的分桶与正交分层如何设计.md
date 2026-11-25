---
title: [ARC-277] AB 实验平台的分桶与正交分层如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-277：AB 实验平台的分桶与正交分层如何设计？
**答**：
- 分桶算法：`hash(layer:salt:userId) % 1000 → 桶号`，同一层内桶互斥（每个用户同层最多进一个实验），不同层之间正交（互相独立组合）。
- 分层治理：核心交易一个层、首页运营一个层……层是稀缺资源（每层容量有限），平台管理"哪个实验占哪层哪段桶"，防止实验互相污染。
- 前端接入：实验配置（分层+桶段+变量值）在 SDK 初始化时一次性拉取，`exp.get('newCheckout')` 本地判定；分桶因子必须用稳定 ID（userId），设备 ID 只做兜底。
- SRM 检查：样本比例与配置比例不符（sample ratio mismatch）自动告警——分桶代码 bug 的探测器。

```typescript
function bucketId(layer: string, salt: string, uid: string) {
  let h = 0;
  const s = `${layer}:${salt}:${uid}`;
  for (const c of s) h = (h * 31 + c.charCodeAt(0)) >>> 0;
  return h % 1000;                                           // 0~999
}
// 实验：{ name: 'checkoutB', layer: 'trade', slots: [[0, 50]], value: 'B' }
function inExperiment(exp, uid) {
  const b = bucketId(exp.layer, exp.salt, uid);
  return exp.slots.some(([lo, hi]) => b >= lo && b < hi) ? exp.value : null;
}
// SRM：observedRatio vs configuredRatio，卡方检验 p < 0.001 → 告警分桶异常
```
