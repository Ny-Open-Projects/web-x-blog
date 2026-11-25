---
title: [RBL-905] 笔试：手写 SLO 错误预算计算器（SLI 分桶 + 预算冻结判定）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-905：笔试：手写 SLO 错误预算计算器（SLI + 预算）

**答**：实现 `budgetCheck(stats, slo, { windowDays })`。stats: 28 天窗口数据 `{ totalBuilds, platformFailures, p95BuildMs, baselineMs, sampledStale, sampled, behaviorPass }`；slo: `{ availability: 0.995, latencyFactor: 1.1, freshness: 0.001, correctness: 1.0 }`. 规则：1) 四个 SLI：availability = 1 − platformFailures/totalBuilds；latency ok = p95 ≤ baseline × factor；freshness ok = sampledStale/sampled ≤ target；correctness = behaviorPass；2) 每项与目标比较：过 → 'ok'；不过 → 该项剩余预算 = (实际允许错误 − 已用)/允许错误，≤ 0 → 'exhausted'；3) 全 ok → 'healthy'；任一 exhausted → `{ verdict: 'freeze', items }`（冻结特性变更）；4) availability 为 0 构建时（totalBuilds=0）→ 'no-data'。边界：sampled=0（freshness 跳过标 'no-data'）。

```javascript
function budgetCheck(stats, slo = { availability: 0.995, latencyFactor: 1.1, freshness: 0.001, correctness: 1.0 }) {
  const items = [];
  if (!stats.totalBuilds) return { verdict: 'no-data', items: [] };

  const avail = 1 - stats.platformFailures / stats.totalBuilds;
  const allowedFail = stats.totalBuilds * (1 - slo.availability);
  items.push({ sli: 'availability', ok: avail >= slo.availability,
    budgetLeft: +Math.max(0, (allowedFail - stats.platformFailures) / Math.max(allowedFail, 1e-9)).toFixed(2) });

  const latOk = stats.p95BuildMs <= stats.baselineMs * slo.latencyFactor;
  items.push({ sli: 'latency', ok: latOk });

  if (stats.sampled > 0) {
    const staleRate = stats.sampledStale / stats.sampled;
    items.push({ sli: 'freshness', ok: staleRate <= slo.freshness });
  } else items.push({ sli: 'freshness', ok: null, note: 'no-data' });

  items.push({ sli: 'correctness', ok: stats.behaviorPass >= slo.correctness });

  const exhausted = items.some(i => i.ok === false && i.budgetLeft !== undefined && i.budgetLeft <= 0);
  const anyFail = items.some(i => i.ok === false);
  return { verdict: exhausted ? 'freeze' : anyFail ? 'warn' : 'healthy', items };
}

// 自测
const base = { totalBuilds: 10000, platformFailures: 30, p95BuildMs: 1000, baselineMs: 1000,
  sampledStale: 5, sampled: 5000, behaviorPass: 1.0 };
let r = budgetCheck(base);
console.log(r.verdict === 'healthy');                    // avail 99.7% > 99.5%

// 预算耗尽
r = budgetCheck({ ...base, platformFailures: 60 });      // 40 允许，用 60
console.log(r.verdict === 'freeze' && r.items[0].budgetLeft === 0);

// 超时延
r = budgetCheck({ ...base, p95BuildMs: 1200 });
console.log(r.items.find(i => i.sli === 'latency').ok === false && r.verdict === 'warn');

// 静默错误：stale 超标
r = budgetCheck({ ...base, sampledStale: 10 });          // 0.2% > 0.1%
console.log(r.items.find(i => i.sli === 'freshness').ok === false && r.verdict === 'warn');

// 边界
console.log(budgetCheck({ ...base, totalBuilds: 0 }).verdict === 'no-data');
r = budgetCheck({ ...base, sampled: 0 });
console.log(r.items.find(i => i.sli === 'freshness').ok === null);
```

**评分点**：
- 四 SLI 计算正确；错误预算公式（允许错误 − 已用）/ 允许错误
- verdict 三档：healthy/warn/freeze（预算耗尽 → 冻结特性）；no-data 处理（totalBuilds=0、sampled=0）
- freshness 的静默性在用例中体现（stale 超标仅 warn 但绝不放过）
- 能说清「可用性坏了立刻可见、缓存新鲜度坏了是静默错误——SLI 体系完整性由最静默的失败决定」属于加分
