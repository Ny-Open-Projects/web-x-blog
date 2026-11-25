---
title: [NODE-740] 笔试题——实现 BFF 聚合器完整版（依赖图调度 + 裁剪 + 降级）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-740：手写 BFF 聚合器

**需求与边界**：
- 需求：声明式聚合器（SCN-NODE-644/729）——① 依赖图声明（dependsOn——有依赖串行/无依赖并行——拓扑调度，SCN-BLD-324 关键路径）；② 字段裁剪（per 端 profile——SCN-NODE-712）；③ criticality 降级（SCN-NODE-729）；④ deadline 全局预算（SCN-NODE-728）。

**答**：
```javascript
function createAggregator(spec) {
  return async (ctx) => {
    const results = {};
    const batches = topoBatches(spec);                 // 依赖拓扑分批（SCN-BLD-324）
    const abort = new AbortController();
    let hardFail = null;
    for (const batch of batches) {
      const settled = await Promise.allSettled(batch.map(async (d) => {
        if (hardFail) throw CANCELLED;                 // must 失败：后续跳过
        const out = await d.call(ctx, {
          ...depsFrom(results, d.dependsOn),           // 上游结果注入
          signal: abort.signal });
        results[d.key] = trim(out, ctx.profile, d.schema);   // 端裁剪（SCN-NODE-712）
      }));
      for (let i = 0; i < batch.length; i++) {
        const d = batch[i], r = settled[i];
        if (r.status === 'rejected') {
          if (d.criticality === 'must') { hardFail = r.reason; abort.abort(); break; }
          results[d.key] = d.fallback ?? null;         // should/may 降级
          ctx.degraded.push(d.key);
        }
      }
      if (hardFail) break;
    }
    if (hardFail) throw hardFail;
    return { data: results, degraded: ctx.degraded };  // 降级标记（SCN-NODE-690）
  };
}
// 声明示例
const homeAgg = createAggregator([
  { key: 'user', call: getUser, criticality: 'must' },
  { key: 'orders', call: getOrders, dependsOn: ['user'], criticality: 'should',
    fallback: [], schema: 'mobile' },                  // 依赖 user 结果 + 端裁剪
  { key: 'recommend', call: getRec, criticality: 'may', fallback: [] },
]);
```

**评分点**:
- 依赖拓扑调度（dependsOn 分批——串行依赖/并行独立）。
- 上游结果注入（依赖链数据传递）。
- 端裁剪 schema 化（SCN-NODE-712）+ criticality 三级降级（SCN-NODE-729）。
- must 失败快速终止（abort 预算节省）。
