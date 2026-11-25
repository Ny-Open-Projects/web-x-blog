---
title: [NODE-729] 笔试题——实现 BFF 部分成功聚合器（criticality 分级）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-729：手写部分成功聚合

**需求与边界**：
- 需求：多下游聚合（SCN-NODE-644）——① 下游声明 criticality（must/should/may）；② must 失败 → 整体失败（快速——不等其他）；③ should 失败 → 降级值；④ may 失败 → 忽略；⑤ 聚合结果带降级标记（SCN-NODE-690）。
- 边界：① must 失败快速中断（AbortController 取消其余——预算省，SCN-NODE-728）；② 降级值声明式（每个 should 下游配置 fallback）；③ 降级详情输出（哪些降级了——前端/运营可见）。

**答**：
```javascript
function aggregator(defs) {
  return async (ctx) => {
    const abort = new AbortController();
    const results = await Promise.allSettled(defs.map(d =>
      d.call(ctx, { signal: abort.signal })
        .catch(e => {
          if (d.criticality === 'must') abort.abort();          // must 失败取消其余（省预算）
          if (d.criticality === 'must') throw e;
          return d.fallback ?? null;                            // should 降级/may 忽略
        })));
    const out = {}, degraded = [];
    let hardFail = null;
    results.forEach((r, i) => {
      const d = defs[i];
      if (r.status === 'fulfilled') out[d.key] = r.value;
      else if (d.criticality === 'must') hardFail = r.reason;
      else { out[d.key] = d.fallback ?? null; degraded.push(d.key); }   // 降级收集
    });
    if (hardFail) throw hardFail;                      // must 失败 → 整体失败
    return { data: out, degraded,                      // 降级标记（SCN-NODE-690）
      headers: { 'X-Degraded': degraded.join(',') } };
  };
}
```

**评分点**:
- criticality 三级（must/should/may——SCN-NODE-644 语义化）。
- must 失败 abort 取消其余（预算节省——SCN-NODE-728 deadline 配合）。
- should/may 降级声明式（fallback 配置）。
- 降级标记输出（header + body 双通道——SCN-NODE-690 可见性）。
