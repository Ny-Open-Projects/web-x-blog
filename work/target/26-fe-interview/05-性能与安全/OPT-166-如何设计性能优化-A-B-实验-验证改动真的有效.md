---
title: [OPT-166] 如何设计性能优化 A/B 实验，验证"改动真的有效"？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-166：如何设计性能优化 A/B 实验，验证"改动真的有效"？

**答**：
- 对照原则：同时期随机分流（实验组/对照组同机房同流量结构），避免"上周 vs 本周"的时间混淆（流量结构、天气、营销活动都会变）。
- 实验设计五要素：假设（改 X 会改善 Y 指标 μ ms）、分流单元（用户级，保证体验一致）、最小样本量（按指标方差与预期效应量算，MDE 越小样本越大）、指标（主指标 + 护栏指标，如 LCP 降了但转化也降就是护栏报警）、周期（≥ 1 个完整周，覆盖周中/周末）。
- 性能实验的特殊性：性能改动常"全量上线更省事"，但无损改动可灰度验证后直接放量；验证意义在于建立团队"改动→收益"的信用记录。
- 显著性判定：t 检验/ bootstrap，报告置信区间而不只是 p 值；指标用分位数对比时用 bootstrap 置信区间。

```javascript
// 一一对应：性能 A/B 分流 + 分位数 bootstrap 显著性检验
// 1. 用户级稳定分流（同一用户始终同组）
function assignGroup(userId, experiment = 'lcp-image-opt') {
  const h = [...`${experiment}:${userId}`].reduce((a, c) => (a * 33 + c.charCodeAt(0)) >>> 0, 5381);
  return (h % 100) < 50 ? 'treatment' : 'control';  // 50/50，哈希稳定
}

// 2. bootstrap 比较两组 P75 的置信区间
function bootstrapP75Diff(a, b, iterations = 2000) {
  const p75 = arr => { const s = [...arr].sort((x, y) => x - y); return s[Math.floor(s.length * 0.75)]; };
  const diffs = [];
  for (let i = 0; i < iterations; i++) {
    const ra = Array.from({ length: a.length }, () => a[Math.random() * a.length | 0]);
    const rb = Array.from({ length: b.length }, () => b[Math.random() * b.length | 0]);
    diffs.push(p75(ra) - p75(rb));   // 正数 = 实验组更快
  }
  diffs.sort((x, y) => x - y);
  const ci = [diffs[Math.floor(iterations * 0.025)], diffs[Math.floor(iterations * 0.975)]];
  return {
    p75_diff: p75(a) - p75(b),
    ci95: ci.map(v => Math.round(v)),
    significant: ci[0] > 0 || ci[1] < 0,  // 区间不含 0 即显著
  };
}

// 3. 实验读取：上报时带分组，服务端按组聚合
const group = assignGroup(user.id);
reportPerf({ metric: 'LCP', value: lcp, group, exp: 'lcp-image-opt' });
// 收尾：bootstrapP75Diff(treatmentLCPs, controlLCPs) → { p75_diff: -420, ci95: [-510, -330], significant: true }
```
