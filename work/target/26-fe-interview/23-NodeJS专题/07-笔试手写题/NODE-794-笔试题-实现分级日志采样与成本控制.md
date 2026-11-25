---
title: [NODE-794] 笔试题——实现日志采样与成本控制（分层 + 聚合降本）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-794：手写日志采样

**需求与边界**：
- 需求：日志成本控制（SCN-NODE-646/741）——① 分层采样（错误全量/慢请求全量/正常采样——SCN-SLA-724）；② 聚合压缩（同类日志聚合——「access ×1000」摘要日志，SCN-联想-320 降噪）；③ 动态采样率（QPS 过载自动降采样——保护自身，SCN-NODE-585 限流配合）；④ 冷热分层存储（近期热查/历史冷存——成本）。
- 边界：① 关键路径日志不采样（支付回调——SCN-NODE-683 全量）；② 采样标签（采样率随日志记录——还原时加权，SCN-SLA-724）；③ 降采样的监控可见性（当前采样率上报——运营知道数据的代表性）。

**答**：
```javascript
class SampledLogger {
  sample(event) {
    if (event.always) return 1;                        // 关键路径全量（SCN-NODE-683）
    if (overloaded()) return this.dynamicRate;         // 过载降采样（SCN-NODE-585）
    return event.slow || event.error ? 1 : this.baseRate;   // 分层（SCN-SLA-724）
  }
  write(event) {
    const rate = this.sample(event);
    if (Math.random() > rate) { this.aggregator.count(event.fingerprint); return; }   // 聚合计数
    logger.info({ ...event, sampleRate: rate }, event.msg);   // 采样率随日志（还原加权）
  }
  flushAggregates() {                                  // 聚合摘要（SCN-联想-320）
    this.aggregator.forEach((count, fp) =>
      logger.info({ fingerprint: fp, count, sampleRate: 0 }, 'AGGREGATED'));
  }
}
```

**评分点**:
- 分层采样（错误/慢全量 + 正常采样——SCN-SLA-724）。
- 聚合摘要（同类计数——SCN-联想-320 降噪）。
- 过载动态降采样（自我保护——SCN-NODE-585）。
- 采样率随日志记录（还原加权——统计诚实性）。
