---
title: [XP-354] 跨端 A/B 实验的统一框架
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-354：跨端 A/B 实验的统一框架

**答**：
- 统一：实验分流（uid hash 稳定）各端一致（同 uid 同组）；指标采集统一 schema。
- 坑：端实现差异引入实验偏差（一端有 bug 拉低组均值）——分端子实验分析。
- 安全：实验开关与降级开关解耦（实验可一键停止）。

```javascript
// 跨端分流
function assign(uid, expId, buckets = 2) {
  const h = hash(`${expId}:${uid}`);                 // 稳定哈希
  return h % buckets;                                // 各端结果一致
}
function splitEndAnalysis(results) {
  return Object.entries(groupBy(results, 'end')).map(([end, rows]) =>
    ({ end, cvr: rows.filter(r => r.converted).length / rows.length }));
}
```
