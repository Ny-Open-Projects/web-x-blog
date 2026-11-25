---
title: [RBL-863] 笔试：手写 canary 指标对比门禁（相对基线 + 样本量校验）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-863：笔试：手写 canary 指标对比门禁（相对基线 + 样本量）

**答**：实现 `canaryGate(canary, baseline, { rules, minSamples })`。双方： `{ errorRate, p95, samples }`。rules: `Record<metric, { maxRel: number, absCap?: number }>`（相对基线允许涨幅；absCap 绝对上限二重保险）。规则：1) 样本量不足（canary.samples < minSamples）→ verdict 'insufficient'（不判成败，要求继续观察）；2) 相对判定：canary[m] > baseline[m] × (1 + maxRel) → fail 该指标；3) absCap 存在且 canary[m] > absCap → 直接 fail（低基线时的兜底）；4) 全过 → 'pass'。返回 `{ verdict, failed: Array<{ metric, canary, baseline, limit }> }`。边界：baseline 指标为 0（相对判定除零——用 absCap 或跳过相对判定只看 absCap）。

```javascript
function canaryGate(canary, baseline, { rules, minSamples = 1000 } = {}) {
  if ((canary.samples ?? 0) < minSamples)
    return { verdict: 'insufficient', failed: [] };
  const failed = [];
  for (const [metric, rule] of Object.entries(rules)) {
    const c = canary[metric], b = baseline[metric];
    const limit = b > 0 ? b * (1 + rule.maxRel) : null;
    const relFail = limit !== null && c > limit;
    const absFail = rule.absCap != null && c > rule.absCap;
    if (relFail || absFail)
      failed.push({ metric, canary: c, baseline: b,
        limit: limit !== null && !absFail ? limit : rule.absCap,
        by: absFail ? 'abs-cap' : 'rel' });
  }
  return { verdict: failed.length ? 'fail' : 'pass', failed };
}

// 自测
const rules = {
  errorRate: { maxRel: 0.2, absCap: 0.02 },
  p95: { maxRel: 0.1 },
};
const baseline = { errorRate: 0.01, p95: 200, samples: 100000 };
let r = canaryGate({ errorRate: 0.011, p95: 210, samples: 5000 }, baseline, { rules });
console.log(r.verdict === 'pass');

r = canaryGate({ errorRate: 0.015, p95: 210, samples: 5000 }, baseline, { rules });
console.log(r.verdict === 'fail');
console.log(r.failed[0].metric === 'errorRate' && r.failed[0].by === 'rel');

// abs-cap 兜底（基线极低时）
r = canaryGate({ errorRate: 0.03, p95: 210, samples: 5000 },
  { errorRate: 0.001, p95: 200, samples: 100000 }, { rules });
console.log(r.failed[0].by === 'abs-cap' && r.failed[0].limit === 0.02);

// 样本不足
console.log(canaryGate({ errorRate: 0.5, p95: 9000, samples: 100 }, baseline, { rules }).verdict === 'insufficient');

// 基线为 0：只用 absCap
r = canaryGate({ errorRate: 0.03, p95: 200, samples: 5000 },
  { errorRate: 0, p95: 200, samples: 100000 }, { rules });
console.log(r.failed[0].metric === 'errorRate');
```

**评分点**：
- 相对基线判定（控制变量）与 absCap 二重保险（低基线兜底）；样本量门禁（insufficient 不武断）
- 基线为 0 的除零防御（退化为 absCap 或跳过）；failed 携带判定依据（by: rel/abs）
- 边界：样本不足、全过
- 能说清「canary 统计要对比基线消除流量/时间因素，样本量不足时宁可不判」属于加分
