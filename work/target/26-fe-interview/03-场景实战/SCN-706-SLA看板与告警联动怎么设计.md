---
title: [SCN-706] SLA 看板与告警的联动怎么设计？怎么避免「看板红了没人管」？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-706：SLA 看板与告警联动怎么设计？
**答**：
- 同源不同视角：告警是「推送驱动」（burn rate 超标推给 oncall），看板是「拉取浏览」（值班巡检/复盘用）——数据同源（同一指标仓库），避免两套口径打架。
- 告警状态上板：看板每个指标旁显示当前告警状态（触发中/已确认/静默中），已确认的告警在板上标绿（表示有人在管）。
- 闭环动作：看板上直接「认领告警」（写 oncall 认领记录）+ 关联事故单链接；处理完自动解锁。
- 静默联动：发版静默窗口（发布后 15 分钟该指标静默），看板显示静默标记，防止发布期误告警也防止「发布背锅」。
- 追问钩子：为什么告警确认状态要回写看板——看板红着但告警没确认 = 流程断点，值班体系的核心是每个红都有 owner。

```javascript
const alertBoardLink = {
  metricAlertState: async (metricKey) => {
    const alerts = await alertStore.query({ metricKey, state: 'FIRING' });
    return alerts.map(a => ({
      ...a,
      claimed: a.claimedBy,                          // 已认领 → 板上绿色
      silenced: a.silenceUntil > Date.now(),         // 发布静默窗口
      incidentUrl: a.incidentId ? `/incident/${a.incidentId}` : null,
    }));
  },
  claim: (alertId, user) =>
    alertStore.claim(alertId, user, { ts: Date.now() }),   // 认领记录可审计
};
```
