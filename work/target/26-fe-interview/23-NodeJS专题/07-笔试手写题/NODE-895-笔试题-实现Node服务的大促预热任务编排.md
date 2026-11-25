---
title: [NODE-895] 笔试题——实现大促预热任务编排（T-1h 预热清单）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-895：手写预热编排

**需求与边界**：
- 需求：大促预热（SCN-联想-859/699）——① 预热清单（连接池预热/缓存预热/CDN 预热/JIT 预热——SCN-联想-859）；② 时间编排（T-24h/T-1h/T-5min——SCN-联想-856 预热推送）；③ 预热验证（各层命中率——SCN-OPS-246）；④ 预热失败告警（SCN-联想-861）。
- 边界：① JIT 预热（Node 函数预执行——SCN-NODE-673 线程池联动）；② 预热任务的幂等（SCN-NODE-655）；③ 预热与压测的区分（SCN-NODE-717 标记）。

**答**：
```javascript
const WARMUP_PLAN = [
  { at: 'T-24h', tasks: ['cdn-prefetch-assets', 'config-push'] },   // SCN-联想-859
  { at: 'T-1h', tasks: ['db-conn-warmup', 'redis-cache-warmup', 'jit-warmup'] },   // SCN-NODE-673
  { at: 'T-5min', tasks: ['ws-preconnect', 'final-health-check'] },   // SCN-联想-882
];
async function runWarmup(now) {
  for (const phase of WARMUP_PLAN.filter(p => due(p.at, now)))
    for (const task of phase.tasks) {
      const r = await warmupTasks[task]();             // 幂等（SCN-NODE-655）
      if (!r.ok) alert({ type: 'WARMUP_FAIL', task, phase: phase.at });   // 失败告警（SCN-联想-861）
    }
}
```

**评分点**:
- 三阶段时间编排（T-24h/T-1h/T-5min——SCN-联想-859）。
- 各层预热（连接池/缓存/CDN/JIT——SCN-NODE-673/联想-859）。
- 预热验证 + 失败告警（SCN-OPS-246/联想-861）。
- 幂等 + 压测标记区分（SCN-NODE-655/717）。
