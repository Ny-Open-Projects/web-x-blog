---
title: [SCN-821] 联想的 AB 实验（排序策略/UI 变体）怎么设计？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-821：联想 AB 实验怎么设计？
**答**：
- 实验分层：策略实验（排序因子调整，服务端分流）与 UI 实验（下拉样式，前端分流）分开评估；同一用户同一实验层只有一个变体（正交分层）。
- 核心指标：联想采纳率、采纳后搜索 CTR、零结果率、input-to-suggest 延迟（策略实验不能牺牲性能）。
- 分流键：用户维度（稳定哈希），新会话不变体；设备性能维度做分层（低端机自动排除重 UI 变体）。
- 结论标准：采纳率显著提升且延迟 P95 不劣化 > 5% 才放量；显著性检验 + 最低样本量前置计算。
- 追问钩子：为什么策略实验要看延迟指标——排序策略变复杂（更多因子计算）常以延迟为代价，采纳率赢但跟手性输了照样负收益。

```javascript
const suggestAB = {
  layers: ['strategy(server-split)', 'ui(client-split)', 'orthogonal: true'],
  metrics: { primary: 'adopt_rate', guard: ['latency_p95', 'zero_result_rate'] },
  gate: (exp) => exp.adoptLift > 0 && exp.latencyP95Delta < 0.05,
  split: (userId, layer) => hash(`${userId}:${layer}`) % 100,
};
```
