---
title: [NODE-956] 笔试题——实现依赖方满意度调查（发布质量的定性度量）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-956：手写满意度调查

**需求与边界**：
- 需求：满意度调查（SCN-OPS-956/227）——① 调查设计（维度：通知时效/发布质量/沟通——SCN-OPS-227 善后）；② 调查触发（发布后——SCN-OPS-227）；③ 结果聚合（满意度趋势——SCN-OPS-956）；④ 结果的消费（改进项——SCN-OPS-227）。
- 边界：① 调查的匿名（SCN-OPS-956 心理安全）；② 调查的频率（季度——SCN-OPS-956）；③ 结果的闭环（SCN-OPS-227）。

**答**：
```javascript
async function satisfactionSurvey(consumers, release) {
  const dimensions = ['notify-timeliness', 'release-quality', 'communication'];
  const responses = await survey.collect(consumers, { dimensions, anonymous: true });   // 匿名（SCN-OPS-956）
  const trend = satisfactionTrend(dimensions);         // 趋势
  const lows = dimensions.filter(d => avg(responses.map(r => r[d])) < 3);
  return { trend, lows, actions: lows.map(d => improvementItem(d)) };   // 改进项（SCN-OPS-227 闭环）
}
```

**评分点**:
- 调查维度（SCN-OPS-227 善后）。
- 匿名设计（心理安全——SCN-OPS-956）。
- 趋势 + 低分维度改进项（SCN-OPS-227 闭环）。
