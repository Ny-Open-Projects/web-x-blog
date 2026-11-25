---
title: [NODE-1011] 笔试题——实现 SLA 违约影响面量化（违约的用户/请求量）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-1011：手写影响面量化

**需求与边界**：
- 需求：违约影响面（SCN-联想-716/1011）——① 违约窗口量化（受影响请求数/用户数——SCN-联想-716 影响面）；② 采样还原（SCN-SLA-724 加权）；③ 影响面的分级（金额/用户等级——SCN-SLA-993）；④ 影响面的消费（补偿/SLA 处置——SCN-SLA-963）。
- 边界：① 采样的还原（SCN-SLA-724）；② 分级（SCN-SLA-993）；③ 消费（SCN-SLA-963）。

**答**：
```javascript
async function breachImpact(breach) {
  const affected = await metrics.sampleRestore(breach.window, { rate: breach.sampleRate });   // 采样还原（SCN-SLA-724）
  return {
    requests: affected.count / breach.sampleRate,      // 加权还原
    users: affected.uniqueUsers / breach.sampleRate,
    tier: severityOf(affected, { vipCount: affected.vipUsers }),   // 分级（SCN-SLA-993）
    action: breach.slaTier === 'gold' ? '立即补偿' : '标准补偿流程',   // 消费（SCN-SLA-963）
  };
}
```

**评分点**:
- 采样还原量化（SCN-SLA-724）。
- 分级（SCN-SLA-993）。
- 消费（SCN-SLA-963）。
