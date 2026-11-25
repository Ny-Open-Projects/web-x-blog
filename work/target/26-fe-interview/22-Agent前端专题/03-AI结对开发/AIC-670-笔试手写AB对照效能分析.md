---
title: [AIC-670] 笔试：手写 A/B 对照效能分析器
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-670：笔试：手写 A/B 对照效能分析器

**答**：实现 `analyzeAB(samples, opts)`。samples: `{ group:'A'|'B', leadTimeH:number, escaped:boolean, complexity:number, survived:boolean }[]`（A=无AI对照组，B=AI实验组）；opts: `{ maxComplexityDiff?:number, minSamples?:number, alpha?:number }`（默认 0.2/10/0.05）。规则：1) 样本量检查：每组 < minSamples → 'insufficient'；2) 复杂度混淆检查：|avgComplexityA − avgComplexityB| / max > maxComplexityDiff → 'confounded'；3) 计算各组的平均前置时间、逃逸率、存活率；4) 速度提升 = (avgLeadA − avgLeadB)/avgLeadA；5) 若 speedup>0 但逃逸率 B>A → 'efficiency-illusion'（提效幻觉）；6) 返回 `{ valid:boolean, reason:string, metrics:{A:any,B:any}, speedup:number, flags:string[] }`。边界：samples 空返回 valid=false reason='empty'。

```javascript
function analyzeAB(samples = [], opts = {}) {
  const { maxComplexityDiff = 0.2, minSamples = 10, alpha = 0.05 } = opts;
  if (!samples.length) return { valid: false, reason: 'empty', metrics: {}, speedup: 0, flags: [] };
  const A = samples.filter(s => s.group === 'A');
  const B = samples.filter(s => s.group === 'B');
  if (A.length < minSamples || B.length < minSamples) {
    return { valid: false, reason: 'insufficient', metrics: {}, speedup: 0, flags: ['low-sample'] };
  }
  const avg = (g, k) => g.reduce((s, x) => s + x[k], 0) / g.length;
  const rate = (g, k) => g.filter(x => x[k]).length / g.length;
  const metrics = {
    A: { leadTime: avg(A, 'leadTimeH'), escapeRate: rate(A, 'escaped'), surviveRate: rate(A, 'survived'), complexity: avg(A, 'complexity') },
    B: { leadTime: avg(B, 'leadTimeH'), escapeRate: rate(B, 'escaped'), surviveRate: rate(B, 'survived'), complexity: avg(B, 'complexity') },
  };
  const flags = [];
  const cplxDiff = Math.abs(metrics.A.complexity - metrics.B.complexity) / Math.max(metrics.A.complexity, metrics.B.complexity, 1);
  if (cplxDiff > maxComplexityDiff) flags.push('confounded');
  const speedup = (metrics.A.leadTime - metrics.B.leadTime) / metrics.A.leadTime;
  if (speedup > 0 && metrics.B.escapeRate > metrics.A.escapeRate) flags.push('efficiency-illusion');
  return {
    valid: !flags.includes('confounded'),
    reason: flags.includes('confounded') ? 'confounded' : 'ok',
    metrics, speedup, flags,
  };
}

// 自测
const samples = [];
for (let i = 0; i < 12; i++) {
  samples.push({ group: 'A', leadTimeH: 20, escaped: i < 1, complexity: 100, survived: true });
  samples.push({ group: 'B', leadTimeH: 12, escaped: i < 3, complexity: 102, survived: true });
}
const r = analyzeAB(samples);
console.log(r.valid === true);
console.log(Math.abs(r.speedup - 0.4) < 0.001);
console.log(r.flags.includes('efficiency-illusion')); // 提速但逃逸率升
console.log(analyzeAB([]).reason === 'empty');
```

**评分点**：
- 样本量与复杂度混淆检查（valid=false 条件）
- 各组平均前置时间/逃逸率/存活率计算
- speedup 公式与提效幻觉判定（提速但逃逸率升）
- 边界：空样本 insufficient 区分
- 能说清「提效幻觉 = 速度提升但质量下降；对照必须排除复杂度混淆变量，否则归因不成立」属于加分
