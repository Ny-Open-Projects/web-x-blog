---
title: [NODE-790] 笔试题——实现服务端监控大屏数据聚合（值班视图）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-790：手写监控聚合

**需求与边界**：
- 需求：值班大屏数据层（SCN-NODE-647/704）——① 多源聚合（QPS/延迟/错误率/池水位/队列积压——SCN-NODE-704 诊断）；② 对比基线（同比昨天/同时段——SCN-SLA-708）；③ 告警联动（活跃告警 + 未认领——SCN-SLA-707）；④ 快速下钻（点击指标 → 明细——SCN-SLA-705 联动）。
- 边界：① 分钟级聚合（实时层——SCN-SLA-711 分级）；② 大屏数据缓存（30s——SCN-SLA-711）；③ 基线动态（同时段历史——SCN-OPS-304）。

**答**：
```javascript
async function oncallDashboard(instanceIds) {
  const [qps, latency, errors, pools, queues, alerts] = await Promise.all([
    metrics.sum('http_requests', { window: '1m', by: 'instance' }),
    metrics.percentile('http_duration', { p: 99, window: '1m' }),
    metrics.rate('http_errors', { window: '5m' }),
    poolStatsAll(instanceIds),                        // SCN-NODE-726 池水位
    queueDepthsAll(),                                 // SCN-NODE-693 积压
    alertsStore.query({ state: 'FIRING', unclaimed: true }),   // SCN-SLA-707 告警联动
  ]);
  const baseline = await dynamicBaseline(metrics, now());   // SCN-OPS-304 动态基线
  return {
    qps, latencyP99: latency, errorRate: errors,
    anomalies: diffVsBaseline({ qps, latency, errors }, baseline),   // 基线对比
    pools, queues, alerts,
    drill: (metric) => detailUrl(metric),              // 下钻链接（SCN-SLA-705）
  };
}
```

**评分点**:
- 多源并行聚合（单请求全貌——SCN-NODE-704 一键诊断）。
- 动态基线对比（SCN-OPS-304 同时段）。
- 告警联动（FIRING + 未认领——SCN-SLA-707 值班视图）。
- 下钻 URL（看板是排障入口——SCN-SLA-705）。
