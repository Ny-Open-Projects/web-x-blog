---
title: [NODE-924] 笔试题——实现多服务协同放量（依赖服务的灰度联动）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-924：手写协同放量

**需求与边界**：
- 需求：多服务协同（SCN-OPS-254/924）——① 依赖服务的灰度联动（上游灰度依赖下游 canary——SCN-NODE-844 DAG）；② 协同放量节奏（依赖先行——SCN-OPS-251 拓扑）；③ 联动摘流（依赖摘流 → 上游回 stable——SCN-NODE-820）；④ 联动审计（SCN-OPS-273）。
- 边界：① 协同的 DAG（发布计划拓扑——SCN-OPS-291）；② 联动的判定（依赖灰度健康——SCN-NODE-798）；③ 协同的演练（SCN-OPS-281）。

**答**：
```javascript
async function coordinatedRamp(plan) {                 // 发布计划拓扑（SCN-OPS-251）
  for (const batch of topoBatches(plan.services)) {    // SCN-BLD-324
    await Promise.all(batch.map(svc => grayRamp(svc)));   // 并行放量
    const health = await Promise.all(batch.map(svc => canarySentinel(svc).evaluate()));   // SCN-NODE-798
    if (health.some(h => h.fails)) {                   // 联动摘流（SCN-NODE-820）
      batch.forEach(svc => unroute(svc));
      break;
    }
    audit({ batch: batch.map(s => s.app), health });   // 审计（SCN-OPS-273）
  }
}
```

**评分点**:
- 拓扑批次协同（SCN-OPS-251/BLD-324）。
- 联动摘流（依赖失败 → 上游回 stable——SCN-NODE-820）。
- 哨兵联动判定（SCN-NODE-798）。
- 审计（SCN-OPS-273）。
