---
title: [MFW-488] 笔试：手写边缘 AB 采样权重再平衡器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-488：边缘 AB 实验权重再平衡器
**答**：实现 `rebalance(experiment, observed)`：1) experiment = { buckets: [{ name, weight }] }，observed = { bucket: samples }；2) 线上样本比与配置权重比偏差 > 5%（SRM，样本比例失配）时报警并输出修正建议权重（使期望流量与实际对齐）；3) sticky 不变：修正只影响新进入用户，已分桶用户 uid → bucket 映射不动（hash 分桶输出保持）；4) 权重和必须归一到 100，某个 bucket 权重到 0 表示停止进人（自然出清）。

```javascript
export function rebalance(experiment, observed, { srmTol = 0.05 } = {}) {
  const buckets = experiment.buckets
  const totalW = buckets.reduce((a, b) => a + b.weight, 0)
  const totalS = Object.values(observed).reduce((a, b) => a + b, 0)

  const issues = []
  for (const b of buckets) {
    const expect = (b.weight / totalW) * totalS
    const actual = observed[b.name] || 0
    if (totalS > 1000 && Math.abs(actual - expect) / expect > srmTol)
      issues.push({ bucket: b.name, expect: Math.round(expect), actual, drift: (actual - expect) / expect })
  }

  // 修正：按观察比例重新归一（只对新用户生效）
  const corrected = buckets.map(b => {
    const s = observed[b.name] || 0
    const w = totalS > 0 ? Math.round((s / totalS) * 100) : b.weight
    return { name: b.name, weight: Math.max(0, w) }
  })
  const sum = corrected.reduce((a, b) => a + b.weight, 0) || 1
  const normalized = corrected.map(c => ({ ...c, weight: Math.round((c.weight / sum) * 100) }))

  return { srm: issues.length > 0 ? issues : null, corrected: normalized, stickyNote: 'existing uid->bucket map untouched' }
}
```

**评分点**：
- SRM 检测有样本量门槛（1000 以下噪声即报会狼来了）
- 修正只影响新用户（sticky 分桶不被重算——实验统计正确性红线）
- 权重归一 + 0 权重出清语义（下线 bucket 让存量自然消化）
- drift 数值随报警输出（不只是布尔，方便定位哪桶失配）
