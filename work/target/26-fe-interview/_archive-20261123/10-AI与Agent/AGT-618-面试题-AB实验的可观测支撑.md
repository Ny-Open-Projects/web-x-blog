---
title: [AGT-618] AI 功能的 A/B 实验，可观测要额外提供什么（与普通功能实验的区别）？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-618：AI 功能的 A/B 实验，可观测要额外提供什么（与普通功能实验的区别）

**答**：
- 普通实验看转化率，AI 实验还要看「质量分布」：不是均值达标就好，要看分布（P90 满意度/差评率长尾），新提示词可能均值持平但差评翻倍。
- 分流完整性校验：实验组/对照组样本量、SRM 检测（分流比偏离配置告警）、污染检测（同用户跨组——AI 会话级粘性被破坏）。
- 实验事件全链路带分组标签：每条 trace/日志/metric 都带 exp+group，否则离线分析时无法归因。

```javascript
function experimentGuard(exp, window) {
  const { treat, ctrl } = window.groups;
  const srm = Math.abs(treat / (treat + ctrl) - exp.ratio) > 0.02;
  const polluted = window.crossUsers > 0;           // 跨组用户
  return { srmAlarm: srm, pollution: polluted,
    qualityDist: { p90Sat: pct(window.sat, 0.9),
      dislikeTail: pct(window.dislike, 0.99) } };   // 分布而非均值
}
```

