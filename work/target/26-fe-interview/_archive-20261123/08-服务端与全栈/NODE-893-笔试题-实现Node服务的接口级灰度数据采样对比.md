---
title: [NODE-893] 笔试题——实现接口级灰度数据采样对比（A/B 数据分流统计）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-893：手写采样对比

**需求与边界**：
- 需求：灰度数据对比（SCN-OPS-203/293）——① 双组数据分流统计（灰度桶维度聚合——SCN-OPS-216 标记）；② SRM 检测（SCN-OPS-293 偏斜）；③ 显著性判定（样本量——SCN-OPS-203）；④ 数据口径版本（SCN-SLA-710）。
- 边界：① 聚合统计的分位（t-digest——SCN-SLA-739）；② 分组维度对齐（端/地域分层——SCN-OPS-239）；③ 结果的可复核（SCN-OPS-284 预注册）。

**答**：
```javascript
async function grayDataCompare(metric, { bucketA, bucketB, prereg }) {
  const a = await metrics.aggregate(metric, { gray: bucketA, digest: TDigest });   // t-digest（SCN-SLA-739）
  const b = await metrics.aggregate(metric, { gray: bucketB });
  const srm = chiSquareSF([a.count, b.count], [prereg.expectedA, prereg.expectedB]);   // SRM（SCN-OPS-293）
  if (srm.skewed) return { verdict: 'SRM_SKEWED', note: '分流偏斜——数据不可信' };
  const sig = significance(a, b, prereg);              // 预注册口径（SCN-OPS-284）
  return { a: a.p50, b: b.p50, delta: a.p50 - b.p50,
    significant: sig.confident, verdict: sig.confident ? sig.result : 'INSUFFICIENT' };   // SCN-OPS-203
}
```

**评分点**:
- SRM 检测（SCN-OPS-293 分流偏斜）。
- 预注册口径（SCN-OPS-284）。
- t-digest 聚合（SCN-SLA-739）。
- 样本量判定（SCN-OPS-203）。
