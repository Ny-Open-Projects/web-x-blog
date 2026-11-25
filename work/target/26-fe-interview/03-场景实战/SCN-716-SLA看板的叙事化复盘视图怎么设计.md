---
title: [SCN-716] SLA 看板的叙事化复盘视图（事故时间线自动生成）怎么设计？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-716：叙事化复盘视图怎么设计？
**答**：
- 事故视图自动组装：检测到 SLO 违约事件后，自动汇聚——指标曲线 + 同时段变更集（发版/配置）+ 告警时间线 + 值班动作，生成时间线视图；复盘会直接用它，省去人肉拼图。
- 关键点标注：违约开始/影响峰值/恢复时刻三个锚点自动计算（变点检测辅助），人工可修正。
- 影响面量化：受影响请求数/用户数估算（基于采样率还原），恢复时长自动计算。
- 叙事模板：时间线上方一句自动生成摘要（「11-14 14:20 签约页 P95 超标 23 分钟，疑似 14:15 发布引起，14:43 回滚恢复」），复盘时人工校准。
- 追问钩子：自动归因（「疑似发布引起」）怎么防止误导——用「候选原因」措辞 + 置信度，并列出排除项，最终结论必须人工确认。

```javascript
async function incidentNarrative(sloBreach) {
  const [changes, alerts, impact] = await Promise.all([
    changesets.in(breach.window),                    // 发版/配置变更
    alerts.timeline(breach.window),
    estimateImpact(breach),                          // 影响请求数/用户数
  ]);
  const anchors = {
    start: breach.start, peak: detectPeak(breach.series), end: breach.end,
  };
  const candidates = rankCauses(changes, breach.start);   // 候选原因（含置信度）
  return {
    anchors, impact, changes, alerts,
    summary: autoSummary(anchors, candidates, impact),    // 措辞：「疑似」「候选」
    humanConfirmed: false,                                // 人工校准标记
  };
}
```
