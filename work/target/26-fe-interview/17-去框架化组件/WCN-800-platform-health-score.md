---
title: [WCN-800] 笔试终局：手写组件平台健康度综合评分器（采纳×质量×成本三维）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-800：笔试终局：手写组件平台健康度综合评分器（采纳×质量×成本三维）

**答**：
- 需求：实现 `healthScore(metrics)`，metrics 为 `{ adoption, quality, cost }` 三个 0~100 的维度分，外加权重 `weights = { adoption:0.4, quality:0.35, cost:0.25 }`（可作为第二参数覆盖）。总分 = 各维度×权重之和（0~100）；判定等级：≥80 'excellent'、≥60 'good'、≥40 'warning'、否则 'critical'。返回 `{ total, level, weakest }`（weakest 为得分最低的维度名）。边界：维度缺失按 0 计；权重和不为 1 时按比例归一化。
- 要点：权重归一化（除以权重和）；加权求和；等级阈值；找最低维度；边界防御。

```javascript
function healthScore(metrics = {}, weights = { adoption: 0.4, quality: 0.35, cost: 0.25 }) {
  const dims = ['adoption', 'quality', 'cost'];
  const w = {}, wsum = dims.reduce((s, d) => s + (weights[d] ?? 0), 0) || 1;
  dims.forEach((d) => { w[d] = (weights[d] ?? 0) / wsum; });     // 权重归一化
  let total = 0, weakest = dims[0], min = Infinity;
  for (const d of dims) {
    const v = Math.max(0, Math.min(100, metrics[d] ?? 0));       // 缺失/越界 -> 0~100
    total += v * w[d];
    if (v < min) { min = v; weakest = d; }
  }
  const level = total >= 80 ? 'excellent' : total >= 60 ? 'good'
    : total >= 40 ? 'warning' : 'critical';
  return { total: Math.round(total), level, weakest };
}
console.log(healthScore({ adoption: 90, quality: 70, cost: 50 }));
```

**评分点**：
- 权重按和归一化，避免权重和不为 1 导致的偏差。
- 维度缺失/越界按 0~100 限幅处理，边界健壮。
- 等级阈值判定正确（含边界值 80/60/40）。
-  weakest 定位最弱维度，输出可驱动改进。
