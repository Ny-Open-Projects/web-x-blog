---
title: [AIC-424] 笔试：实现评审升级（escalation）SLA 计时器。
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-424：笔试：实现评审升级（escalation）SLA 计时器。
**答**：高危发现 4 小时未确认自动升级。输入发现列表 `[{id, createdAt, confirmedAt}]` 与 now，输出待升级清单（超时未确认）与在途清单。时间比较用毫秒，4h = 14_400_000。

```javascript
const SLA = 4 * 3600 * 1000;
function escalationSweep(findings, now) {
  const out = { toEscalate: [], inFlight: [] };
  for (const f of findings) {
    if (f.confirmedAt) continue;
    const age = now - f.createdAt;
    if (age >= SLA) out.toEscalate.push({ id: f.id, overdueMs: age - SLA });
    else out.inFlight.push({ id: f.id, remainMs: SLA - age });
  }
  return out;
}
console.log(escalationSweep([
  { id: 1, createdAt: 0, confirmedAt: null },
  { id: 2, createdAt: 0, confirmedAt: 1000 },
  { id: 3, createdAt: SLA - 1000, confirmedAt: null },
], SLA + 500)); // toEscalate: [1]，inFlight: [3]

```

**评分点**：
- 状态三分类：已确认/在途（未超时）/待升级（超时）。
- 时间边界：恰好 4h 算超时（>=）。
- confirmedAt 为 null 视为未确认。
- 输出带超时时长便于催办。
