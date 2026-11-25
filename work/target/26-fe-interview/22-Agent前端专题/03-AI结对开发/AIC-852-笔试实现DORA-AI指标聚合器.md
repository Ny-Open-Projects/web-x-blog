---
title: [AIC-852] 笔试：实现 DORA-AI 指标聚合器（含 AI 失败率差）
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-852：笔试：实现 DORA-AI 指标聚合器（含 AI 失败率差）
**答**：
- 核心需求：实现 `aggregateDORA(changes, windowDays)`，按天聚合 DORA 指标：`deployFreq`（日均部署数）、`leadTimeP50`（变更前置时间中位数）、`changeFailureRate`、`mttr`（失败恢复到正常的平均小时数）、`aiFailureGap`（AI 代码失败率 − 非 AI 代码失败率）。
- 边界：空输入返回各字段为 0 的完整对象；失败记录必须带 `restoredAt` 才能算 MTTR，否则跳过该记录；中位数要对偶数样本取中间两数平均；`aiFailureGap` 在某类样本为 0 时返回 0 而非 NaN。
- 输出要带 `windowDays` 与 `sampleCount`，便于判断统计显著性（样本少不下结论）。
- 追问钩子：追问「部署频率变高一定是好事吗」——能答出「要和小步提交、回滚率一起看，否则可能是 AI 批量灌水」的候选人理解指标的语境依赖。

```typescript
type Change = { id: string; deployedAt: number; leadMinutes: number;
  failed: boolean; aiGenerated: boolean; restoredAt?: number };

const median = (a: number[]) => {
  if (!a.length) return 0;
  const s = [...a].sort((x, y) => x - y), m = s.length >> 1;
  return s.length % 2 ? s[m] : (s[m - 1] + s[m]) / 2;
};
const rate = (n: number, d: number) => d > 0 ? n / d : 0;

function aggregateDORA(changes: Change[], windowDays = 7) {
  const list = changes ?? [];
  const ai = list.filter(c => c.aiGenerated), manual = list.filter(c => !c.aiGenerated);
  const failures = list.filter(c => c.failed);
  const mttrSamples = failures
    .filter(c => c.restoredAt != null)
    .map(c => (c.restoredAt! - c.deployedAt) / 3600000); // 小时
  return {
    windowDays,
    sampleCount: list.length,
    deployFreq: +(list.length / windowDays).toFixed(2),
    leadTimeP50: +median(list.map(c => c.leadMinutes)).toFixed(1),
    changeFailureRate: +rate(failures.length, list.length).toFixed(3),
    mttr: +(mttrSamples.reduce((s, v) => s + v, 0) / (mttrSamples.length || 1)).toFixed(2),
    aiFailureGap: +(rate(ai.filter(c => c.failed).length, ai.length) -
      rate(manual.filter(c => c.failed).length, manual.length)).toFixed(3),
  };
}
console.log(aggregateDORA([
  { id:'1', deployedAt:0, leadMinutes:30, failed:false, aiGenerated:true },
  { id:'2', deployedAt:10, leadMinutes:90, failed:true, aiGenerated:true, restoredAt:3600000 },
  { id:'3', deployedAt:20, leadMinutes:60, failed:false, aiGenerated:false },
]));
```
**评分点**：
- 中位数对偶数样本取两数平均，不是任取中间一个。
- MTTR 只统计有 restoredAt 的失败记录，缺失者跳过而非算 0。
- `rate()` 统一处理分母为 0，aiFailureGap 不产生 NaN。
- 输出带 windowDays/sampleCount 支持显著性判断。
- 空输入返回完整结构（非 undefined），调用方安全。
