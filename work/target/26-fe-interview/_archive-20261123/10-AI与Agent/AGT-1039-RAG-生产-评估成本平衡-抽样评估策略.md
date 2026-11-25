---
title: [1039] 评估集 5000 条跑一次太贵，抽样评估怎么设计
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 抽样]
type: 面试题
---

## 1039：评估集 5000 条跑一次太贵，抽样评估怎么设计

**答**：
- 抽样评估三层：全量低频（月度，改动大时）、核心高频（每日/每提交，200 条分层抽样——按意图 × 难度配额抽，保证代表性）、探针极高频（金丝雀 50 条）。
- 分层抽样是关键：随机抽样会让高频意图淹没低危场景，按「意图 × 难度」格子配额抽，每格保底样本量。
- 增量评估：只跑「改动可能影响的意图」相关格子（改了检索融合权重就跑检索敏感的格子），成本再降一半。
- 追问钩子：抽样评估的置信度够吗？——200 条分层样本对「主要意图」的指标置信区间足够（±5%），对长尾意图不够——所以长尾场景靠低频全量补齐，两层互补。

```ts
function stratifiedSample(evalSet, n = 200) {
  const cells = groupBy(evalSet, c => c.intent + '|' + c.hard);
  const quota = Math.ceil(n / Object.keys(cells).length);
  return Object.values(cells).flatMap(g =>
    sample(g, Math.min(quota, Math.max(2, Math.round(g.length / evalSet.length * n)))));
}
```
