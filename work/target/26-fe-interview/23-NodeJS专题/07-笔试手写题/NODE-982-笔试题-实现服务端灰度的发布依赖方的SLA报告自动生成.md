---
title: [NODE-982] 笔试题——实现 SLA 报告自动生成（月度报告）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-982：手写 SLA 报告

**需求与边界**：
- 需求：SLA 报告（SCN-OPS-728/982）——① 报告生成（月度/周度——SCN-OPS-728）；② 数据快照（SCN-OPS-728）；③ 报告的分发（SCN-OPS-728）；④ 报告的归档（SCN-OPS-248）。
- 边界：① 快照的固化（SCN-OPS-728 可复核）；② 报告的权限（SCN-OPS-714）；③ 报告的摘要（SCN-SLA-708）。

**答**：
```javascript
schedule('0 9 1 * *', async () => {                    // 月度（SCN-OPS-728）
  for (const consumer of slaConsumers()) {
    const snap = await snapshotData(consumer, { range: lastMonth() });   // 快照固化（SCN-OPS-728）
    const pdf = await renderReport(snap, { template: 'sla-monthly',
      audience: boardACL(consumer) });                 // 权限（SCN-OPS-714）
    await send({ to: consumer.ownerRole, attach: pdf,
      meta: { dataRev: snap.id, calVer: snap.calVer } });   // 可复核（SCN-OPS-284）
    await archiveReport(pdf, snap);                    // 归档（SCN-OPS-248）
  }
});
```

**评分点**:
- 快照固化 + 可复核（SCN-OPS-728/284）。
- 权限（SCN-OPS-714）。
- 归档（SCN-OPS-248）。
