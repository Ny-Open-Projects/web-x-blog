---
title: [RBL-881] 笔试：手写 RUM 劣化分桶检测器（分桶 P75 对比 + 归因候选）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-881：笔试：手写 RUM 劣化分桶检测器（P75 对比 + 归因）

**答**：实现 `detectRegression(samples, baselines, { threshold, minSamples })`。samples: `{ route, deviceTier, lcp, buildId }[]`；baselines: `Record<bucketKey, { p75, release }>`（bucketKey = 'route|tier'）。规则：1) 分桶聚合：每桶样本 < minSamples 跳过（样本不足）；2) 桶 P75 > baseline.p75 × (1 + threshold) → 劣化 `{ bucket, p75, base, drift }`；3) 归因候选：该桶样本的 buildId 与 baseline.release 不同的样本占比 → driftSource（'new-release' 占比 > 50% 时归因新发布，否则 'mixed'）；4) 返回 `{ degraded: Array, ok }`（ok = 无劣化）。边界：无 baselines 的桶跳过（新路由）；samples 空。

```javascript
const percentile = (arr, q) => { const s = [...arr].sort((a, b) => a - b);
  return s[Math.min(s.length - 1, Math.floor(q * s.length))] ?? 0; };

function detectRegression(samples, baselines, { threshold = 0.15, minSamples = 50 } = {}) {
  const buckets = new Map();
  for (const s of samples ?? []) {
    const key = `${s.route}|${s.deviceTier}`;
    (buckets.get(key) || buckets.set(key, []).get(key)).push(s);
  }
  const degraded = [];
  for (const [key, list] of buckets) {
    const base = baselines?.[key];
    if (!base) continue;                                 // 新路由无基线跳过
    if (list.length < minSamples) continue;
    const p75 = percentile(list.map(s => s.lcp), 0.75);
    if (p75 > base.p75 * (1 + threshold)) {
      const newRelease = list.filter(s => s.buildId !== base.release).length;
      degraded.push({ bucket: key, p75, base: base.p75,
        drift: +((p75 / base.p75 - 1) * 100).toFixed(1),
        driftSource: newRelease / list.length > 0.5 ? 'new-release' : 'mixed' });
    }
  }
  degraded.sort((a, b) => b.drift - a.drift);
  return { degraded, ok: degraded.length === 0 };
}

// 自测
const samples = [];
for (let i = 0; i < 100; i++) samples.push({ route: '/home', deviceTier: 'low', lcp: 3500 + (i < 60 ? 0 : 0), buildId: 'r2' });
for (let i = 0; i < 100; i++) samples.push({ route: '/home', deviceTier: 'high', lcp: 1200, buildId: 'r2' });
const baselines = { '/home|low': { p75: 2800, release: 'r1' }, '/home|high': { p75: 1200, release: 'r1' } };

let r = detectRegression(samples, baselines, { threshold: 0.15 });
console.log(r.ok === false);
console.log(r.degraded[0].bucket === '/home|low');
console.log(r.degraded[0].drift === '25.0');             // 3500/2800 = 1.25
console.log(r.degraded[0].driftSource === 'new-release');// 全部 r2
console.log(r.degraded.length === 1);                    // high 桶未劣化

// 样本不足
r = detectRegression([{ route: '/x', deviceTier: 'low', lcp: 9000, buildId: 'r2' }], baselines);
console.log(r.ok === true && r.degraded.length === 0);   // <50 跳过

// 新路由无基线
r = detectRegression(Array.from({ length: 60 }, () =>
  ({ route: '/new', deviceTier: 'low', lcp: 9000, buildId: 'r2' })), baselines);
console.log(r.ok === true);
console.log(detectRegression([], baselines).ok === true);
```

**评分点**：
- 分桶聚合与 P75 计算正确；样本量门禁（<minSamples 跳过不误报）；新路由无基线跳过
- 劣化判定相对阈值；driftSource 归因（新 release 样本占比 >50%）
- 排序按 drift 降序（最劣化优先）；边界：空 samples
- 能说清「RUM 回流让预算从约定变实证校准，单看 CI 体积是半闭环」属于加分
