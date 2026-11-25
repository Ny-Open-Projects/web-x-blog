---
title: [ARC-278] AB 实验的指标体系与显著性判定如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-278：AB 实验的指标体系与显著性判定如何设计？
**答**：
- 指标三层：北极星（决策指标，如人均 GMV）、护栏（不可变差的约束，如白屏率/投诉率）、观察指标（解释机制用）。实验结论只看北极星+护栏，防止挑数据。
- 判定纪律：实验设计期定好**最小可检测效应（MDE）与样本量**，跑满周期再看结果；禁止中途偷看并提前下结论（多重检验膨胀假阳性）；显著 ≠ 重要，还要看效应量与置信区间。
- 前端实验的特殊噪声：指标受设备/网络混杂影响——分层分析（按设备档拆）+ CUPED 降方差是加分项。
- 长期效应：新奇效应（上线首周虚高）要求观察 2 周以上或看留存曲线收敛。

```typescript
// 简化的显著性检验（比例类指标）
function zTest(pA, nA, pB, nB) {
  const p = (pA * nA + pB * nB) / (nA + nB);
  const se = Math.sqrt(p * (1 - p) * (1 / nA + 1 / nB));
  const z = (pB - pA) / se;
  return { z, pValue: 2 * (1 - erf(Math.abs(z) / Math.SQRT2)) };
}
// 样本量预估：n per arm ≈ 16 * p(1-p) / (MDE^2)（α=0.05, power=0.8 近似）
// 报告：{ metric: 'gmvPerUser', lift: +2.3%, ci: [+0.4%, +4.2%], guard: { whiteRate: ns } }
```
