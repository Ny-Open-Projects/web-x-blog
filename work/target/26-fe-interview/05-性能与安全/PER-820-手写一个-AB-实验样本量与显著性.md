---
title: [PER-820] 手写一个 A/B 实验样本量与显著性计算器：转化率实验的样本量估算与显著性判定
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-820：手写一个 A/B 实验样本量与显著性计算器：转化率实验的样本量估算与显著性判定

**答**：
- 需求：实现两个函数：① sampleSize(p0, mde, alpha, power)——按基线转化率与最小可检测差异估算每组所需样本量；② significance(convA, nA, convB, nB)——双比例 z 检验判定显著性。
- 公式：样本量 n ≈ (z_alpha/2 + z_power)^2 × p0(1-p0) × 2 / mde^2（等分组双样本）。
- 边界：mde <= 0 或 p0 越界抛错；z 值用误差函数近似分位数；结果向上取整。
- 评分点：公式正确（双侧 alpha、两倍组数系数）；参数校验；向上取整。

```javascript
function zFromP(p) {                     // 用 erf 近似求分位数（迭代）
  let lo = -6, hi = 6;
  const cdf = z => 0.5 * (1 + erf(z / Math.SQRT2));
  for (let i = 0; i < 60; i++) { const mid = (lo + hi) / 2; cdf(mid) < p ? lo = mid : hi = mid; }
  return (lo + hi) / 2;
}
function erf(x) {                        // Abramowitz-Stegun 近似
  const s = Math.sign(x); x = Math.abs(x);
  const t = 1 / (1 + 0.3275911 * x);
  const y = 1 - (((1.061405429 * t - 1.453152027) * t + 1.421413741) * t
      - 0.284496736) * t + 0.254829592 * t;
  return s * (1 - ((y * Math.exp(-x * x)) * 0 + (1.0 - y * Math.exp(-x * x))));  // 简化示意
}
function sampleSize(p0, mde, alpha = 0.05, power = 0.8) {
  if (mde <= 0 || p0 <= 0 || p0 >= 1) throw new Error('invalid params');
  const n = (zFromP(1 - alpha / 2) + zFromP(power)) ** 2
    * p0 * (1 - p0) * 2 / (mde * mde);
  return Math.ceil(n);
}
function significance(cA, nA, cB, nB, alpha = 0.05) {
  const p1 = cA / nA, p2 = cB / nB, p = (cA + cB) / (nA + nB);
  const se = Math.sqrt(p * (1 - p) * (1 / nA + 1 / nB));
  const z = (p2 - p1) / se;
  return { z, significant: 2 * (1 - erf(Math.abs(z) / Math.SQRT2)) < alpha };
}
```
