---
title: [NODE-850] 笔试题——实现灰度实例指标隔离统计（per 版本切片）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-850：手写指标隔离

**需求与边界**：
- 需求：版本维度指标（SCN-OPS-850/231）——① 指标按版本切片（version label——SCN-OPS-231 样本侧版本）；② 版本聚合统计（canary vs stable 对比——SCN-NODE-798）；③ 版本残留监控（SCN-OPS-301）；④ 指标标签基数控制（label 组合爆炸——SCN-联想-850 约束）。
- 边界：① label 基数治理（version label 基数 = 活跃版本数——上限约束，SCN-OPS-256 版本堆积）；② 指标采集的版本注入（buildinfo——SCN-ENG-309）；③ 聚合的对账（版本流量占比 = 100%——完整性）。

**答**：
```javascript
// 指标注入版本 label（SCN-OPS-231）
metrics.push('http_requests', 1, { version: BUILD.commit.slice(0, 8), ...dims });
// 版本对比（SCN-NODE-798）
function versionCompare(a, b, metric) {
  const ca = metrics.slice(metric, { version: a }), cb = metrics.slice(metric, { version: b });
  return { a: ca.p50, b: cb.p50, delta: ca.p50 - cb.p50,
    significant: ca.samples > 100 && cb.samples > 100 };   // 样本下限（SCN-OPS-203）
}
// label 基数治理（SCN-OPS-256）
const activeVersions = [...new Set(metrics.labels('version'))];
if (activeVersions.length > 5) warn('版本 label 基数超 5——SCN-OPS-256 堆积治理');
// 流量占比完整性
assert(sum(versionPct) === 100);                       // 占比 100%（SCN-OPS-850）
```

**评分点**:
- 版本 label 注入（样本侧版本——SCN-OPS-231）。
- 版本对比带样本下限（SCN-OPS-203）。
- label 基数治理（版本堆积——SCN-OPS-256）。
- 流量占比完整性校验（100%）。
