---
title: [NODE-813] 笔试题——实现 BFF 拓扑编排器（DAG 依赖 + 部分成功 + 预算）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-813：手写拓扑编排

**需求与边界**：
- 需求：DAG 编排器（SCN-NODE-740/729）——① DAG 依赖图调度（拓扑批次——SCN-BLD-324）；② 部分成功 + criticality（SCN-NODE-729）；③ 预算按 DAG 权重分配（SCN-NODE-795 树形）；④ 上游结果注入依赖下游（SCN-NODE-740）。
- 边界：① DAG 环检测（声明错误 fail-fast——SCN-BLD-324）；② 并行批次间流水（前批结果可被后批用——数据依赖）；③ 预算不足的降级（关键路径优先——SCN-NODE-795 抢占）。

**答**：
```javascript
async function dagOrchestrate(spec, ctx) {
  assertNoCycle(spec);                                 // 环检测（SCN-BLD-324 fail-fast）
  const batches = topoBatches(spec);
  const results = {}; const degraded = [];
  const abort = new AbortController();
  for (const batch of batches) {
    const settled = await Promise.allSettled(batch.map(async (d) => {
      if (hardFail) throw CANCELLED;
      const budget = allocBudget(d, remaining());      // 权重预算（SCN-NODE-795）
      const deps = pickDeps(d.dependsOn, results);     // 上游结果注入（SCN-NODE-740）
      return trim(await d.call(ctx, { ...deps, signal: abort.signal, budget }), ctx);
    }));
    for (let i = 0; i < batch.length; i++) {
      if (settled[i].status === 'rejected') {
        if (batch[i].criticality === 'must') { hardFail = settled[i].reason; abort.abort(); break; }
        results[batch[i].key] = batch[i].fallback; degraded.push(batch[i].key);   // 降级（SCN-NODE-729）
      } else results[batch[i].key] = settled[i].value;
    }
    if (hardFail) break;
  }
  if (hardFail) throw hardFail;
  return { data: results, degraded };
}
```

**评分点**:
- DAG 环检测 fail-fast + 拓扑批次（SCN-BLD-324）。
- 上游结果注入（数据依赖链——SCN-NODE-740）。
- criticality 三级 + abort 取消（SCN-NODE-729）。
- 树形预算分配（SCN-NODE-795 联动）。
