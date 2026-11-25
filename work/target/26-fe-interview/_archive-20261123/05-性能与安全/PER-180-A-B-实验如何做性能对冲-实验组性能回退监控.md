---
title: [PER-180] A/B 实验如何做性能对冲（实验组性能回退监控）？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-180：A/B 实验如何做性能对冲（实验组性能回退监控）？

**答**：
- 问题本质：实验只看转化收益，容易引入"性能暗成本"（实验组多加载 SDK/逻辑），性能回退最终吃掉转化收益。
- 机制：每个实验登记**性能预算**（如 LCP P75 劣化上限 300ms、INP 上限 100ms），监控哨兵对比实验组与对照组同时段指标，超预算自动暂停放量并通知实验 owner。
- 分层归因：性能劣化是实验本身引入的，还是实验框架引入的（分组 SDK 开销）——对照组也要留一个"纯框架"组。
- 原则写入平台：放量按钮与性能哨兵联动，性能超预算的实验不能靠人肉继续放量。

```javascript
// A/B 性能对冲：实验组上线即绑性能哨兵，回退超阈值自动暂停放量
const EXPERIMENTS = {
  exp_new_checkout: {
    owner: 'trade',
    perfBudget: { lcpP75DeltaMs: 300, inpP98DeltaMs: 100 },
  },
};

export function guardExperiment(expId, metrics) {
  const cfg = EXPERIMENTS[expId];
  const base = baselineMetrics(metrics.page);   // 对照组同时段数据
  const lcpDelta = metrics.lcpP75 - base.lcpP75;
  const inpDelta = metrics.inpP98 - base.inpP98;

  if (lcpDelta > cfg.perfBudget.lcpP75DeltaMs || inpDelta > cfg.perfBudget.inpP98DeltaMs) {
    alertOwner(cfg.owner, `${expId} 实验组 LCP 劣化 ${lcpDelta}ms 超预算`);
    return { action: 'pause_rollout' };         // 自动停在当前流量比例
  }
  return { action: 'continue' };
}
// 归因提示：对照组要留一个纯框架组，区分实验本身与实验框架的开销
```
