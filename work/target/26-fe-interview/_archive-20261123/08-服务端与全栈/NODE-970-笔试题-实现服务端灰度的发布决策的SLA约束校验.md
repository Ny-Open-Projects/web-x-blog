---
title: [NODE-970] 笔试题——实现发布决策 SLA 约束校验（决策时效）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-970：手写 SLA 约束

**需求与边界**：
- 需求：决策 SLA（SCN-OPS-970/210）——① 决策时效约束（告警 N 分钟内决策——SCN-OPS-210 升级）；② 超时升级（决策权上移——SCN-OPS-210）；③ 约束的监控（决策延迟分布——SCN-OPS-970）；④ 约束的审计（SCN-OPS-273）。
- 边界：① 分级的时效（P0 5min——SCN-OPS-210）；② 升级的自动触发（SCN-OPS-210）；③ 约束的演练（SCN-OPS-215）。

**答**：
```javascript
async function decisionSlaGuard(event, { sla = { P0: 5 * 60_000 } } = {}) {
  const timer = setTimeout(() => {                     // 超时升级（SCN-OPS-210）
    escalate(event); audit({ type: 'DECISION_ESCALATED', event: event.id });
  }, sla[event.level] ?? 10 * 60_000);
  event.onDecision(() => {                             // 决策完成
    clearTimeout(timer);
    telemetry.push({ delay: Date.now() - event.ts, level: event.level });   // 监控（SCN-OPS-970）
  });
}
```

**评分点**:
- 分级时效（P0 5min——SCN-OPS-210）。
- 超时升级自动触发（SCN-OPS-210）。
- 决策延迟监控（SCN-OPS-970）。
