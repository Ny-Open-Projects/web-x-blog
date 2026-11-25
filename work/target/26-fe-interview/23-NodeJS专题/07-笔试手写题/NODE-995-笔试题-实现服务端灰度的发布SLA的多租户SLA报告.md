---
title: [NODE-995] 笔试题——实现租户 SLA 报告（分层报告生成）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-995：手写租户报告

**需求与边界**：
- 需求：租户报告（SCN-SLA-982/995）——① 分层报告生成（SCN-SLA-982 快照）；② 分层报告的权限（SCN-OPS-714）；③ 报告的归档（SCN-OPS-248）；④ 报告的分发（SCN-OPS-612）。
- 边界：① 分层的口径（SCN-SLA-710）；② 报告的可复核（SCN-OPS-284）；③ 报告的摘要（SCN-SLA-708）。

**答**：
```javascript
schedule('0 9 1 * *', async () => {
  for (const tier of Object.keys(TENANT_TIERS)) {
    for (const t of tenantsOf(tier)) {
      const snap = await snapshotData(t, { range: lastMonth() });   // 快照（SCN-OPS-728）
      const pdf = await renderReport(snap, { template: `sla-${tier}`,   // 分层模板
        audience: boardACL(t) });                        // 权限（SCN-OPS-714）
      await send({ to: t.ownerRole, attach: pdf });
      await archiveReport(pdf, snap);                    // 归档（SCN-OPS-248）
    }
  }
});
```

**评分点**:
- 分层模板 + 快照（SCN-SLA-982/710）。
- 权限 + 归档（SCN-OPS-714/248）。
- 分发（SCN-OPS-612）。
