---
title: [PER-786] 手写一个 WebView 池监控大盘数据聚合器：命中率、等待队列与创建耗时三维数据聚合
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-786：手写一个 WebView 池监控大盘数据聚合器：命中率、等待队列与创建耗时三维数据聚合

**答**：
- 需求：输入 acquire 事件流（命中热池/走冷池/排队/失败），按时间窗聚合出：热池命中率、平均等待时长、平均创建耗时、失败率；输出分钟粒度序列供大盘消费。
- 边界：事件乱序（按时间戳排序后聚合）；空窗分钟也要输出零值序列（大盘连续性）；样本数小于阈值的分钟标记 low-confidence。
- 评分点：窗口聚合正确性（含空窗补零）；low-confidence 标记。

```javascript
function aggregatePool(events, { bucketMs = 60000, minSample = 5 } = {}) {
  events.sort((a, b) => a.t - b.t);
  const start = Math.floor(events[0].t / bucketMs) * bucketMs;
  const end = Math.floor(events[events.length - 1].t / bucketMs) * bucketMs;
  const out = [];
  for (let t = start; t <= end; t += bucketMs) {          // 空窗也补零
    const es = events.filter(e => e.t >= t && e.t < t + bucketMs);
    const hit = es.filter(e => e.kind === 'hot').length;
    const waits = es.map(e => e.waitMs || 0);
    const creates = es.filter(e => e.createMs != null).map(e => e.createMs);
    const fail = es.filter(e => e.kind === 'fail').length;
    out.push({
      t, total: es.length, hitRate: es.length ? hit / es.length : 0,
      waitP75: p75(waits), createP75: p75(creates),
      failRate: es.length ? fail / es.length : 0,
      low: es.length < minSample,                         // 样本不足标记
    });
  }
  return out;
}
function p75(arr) { if (!arr.length) return null; const s = [...arr].sort((a, b) => a - b); return s[Math.floor(s.length * 0.75)]; }
```
