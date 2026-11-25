---
title: [PER-910] 性能实验（A/B）与性能优化如何协同
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-910：性能实验（A/B）与性能优化如何协同

**答**：
- 优化方案上线前先灰度实验：对照组 vs 实验组按 uid 分桶，比较 P75 LCP/INP 与业务指标（转化率），防"优化反而劣化"。
- 性能实验的指标置信度：用 bootstrap 或 t 检验对分位数做区间估计，样本不足时延长实验而非拍板上。
- 注意干扰因素：实验分流要按 uid 稳定哈希，且两组流量结构（机型/地域）需做 SRM 校验（样本比例失衡检测）。
- 实验结论沉淀为平台知识库：方案、收益、成本、适用条件，供后续类似场景复用。

```javascript
// SRM 校验：实验分流是否失衡
function checkSRM(control, treatment, expected = 0.5) {
  const total = control + treatment;
  const obs = treatment / total;
  const se = Math.sqrt(expected * (1 - expected) / total);   // 正态近似
  const z = (obs - expected) / se;
  return { ratio: +obs.toFixed(4), z: +z.toFixed(2),
           ok: Math.abs(z) < 3 };   // |z|>=3 视为分流异常，结论不可信
}
// checkSRM(50400, 49600) -> { ratio: 0.496, z: -1.13, ok: true }
```
