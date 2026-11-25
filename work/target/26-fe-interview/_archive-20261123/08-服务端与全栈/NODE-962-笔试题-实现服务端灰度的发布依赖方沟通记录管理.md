---
title: [NODE-962] 笔试题——实现依赖方沟通记录管理（通知/确认/反馈闭环）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-962：手写沟通记录

**需求与边界**：
- 需求：沟通记录（SCN-OPS-245/962）——① 沟通记录模型（通知/确认/反馈——三态，SCN-OPS-245）；② 记录的检索（按消费方/发布——SCN-OPS-248）；③ 记录的完整性（SCN-OPS-289）；④ 记录的消费（复盘——SCN-OPS-248）。
- 边界：① 记录的 append-only（SCN-NODE-775）；② 记录的脱敏（SCN-NODE-698）；③ 记录的保留期（SCN-FIN-625）。

**答**：
```javascript
async function communicationLog(releaseId) {
  const entries = await commLog(releaseId);            // 三态（SCN-OPS-245）
  const complete = entries.every(e =>
    ['notified', 'acked', 'feedback'].filter(s => entries.some(x => x.consumer === e.consumer && x.stage === s)));
  return { entries, complete,
    gaps: !complete ? missingConsumers(entries) : [],   // 缺口（SCN-OPS-289）
    retention: '90d' };                                 // 保留期（SCN-FIN-625）
}
```

**评分点**:
- 三态沟通模型（SCN-OPS-245）。
- 完整性校验（SCN-OPS-289）。
- append-only + 保留期（SCN-NODE-775/FIN-625）。
