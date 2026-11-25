---
title: [AGT-313] 舆情分析 Agent——多源聚合与敏感输出的处理？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-313：舆情监测/分析 Agent 的多源聚合与输出安全怎么设计？

**答**:
- 管线：多源采集（社交/新闻/论坛，合规爬取 AGT-115 原则）→ 降噪去重（同源转载合并）→ 情感与主题聚类（LLM 打标+程序聚类）→ 事件演化追踪（同一事件跨时间线关联）→ 报告生成（摘要+数据+来源）。
- 输出敏感性：舆情报告直接影响公关决策——结论必须"数据说话"（每条结论附样本量/来源分布/置信度），不确定趋势标注"需持续观察"而非断言；情绪比例类数字走程序统计（AGT-267）。
- 内容风险：分析中引用的原帖可能含违规内容——引用做净化摘要而非原文粘贴；报告输出再过内容安全审核（双重保障）。
- 误报治理：水军/刷量干扰情感数据——来源可信度分级（账号年龄/互动真实性），水军内容降权并标注；误报案例进回归集。

```javascript
async function opinionReport(topic, window) {
  const raw = await collect(topic, window);          // 合规采集
  const dedup = dedupe(raw, { trust: sourceTrust }); // 去重+降权
  const stats = programStats(dedup);                 // 程序统计
  const report = await llm(`结论必须引用 stats 数字，
    不确定趋势标"持续观察"`, { topic, stats,
    samples: sanitize(summaries(dedup)) });
  return audit(report);                              // 内容安全二审
}
```
