---
title: [SCN-731] SLA 看板自身的性能与健康（看板挂了谁看着看板）怎么监控？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-731：看板自身健康怎么监控？
**答**：
- 看板自监控：查询 API 可用性/P95、数据管道延迟（最新数据时间戳滞后）、SDK 上报量突降（上游故障信号）——看板自身是关键基础设施，按内部 SLA 管理。
- 看板挂了的兜底：主看板不可用时自动切换备用通道（静态核心指标页/IM 机器人定时播报核心数字）——值班不能「因为看板挂了失明」。
- 管道健康对账：上报量 vs 业务流量基线（上报量骤降 50% 可能是 SDK 故障而非业务正常），偏差告警。
- 部署独立：看板前端与数据管道独立部署、独立告警，避免「管道故障导致看板同时挂」的双盲。
- 追问钩子：怎么发现「数据悄悄停了」——对账任务：RUM 上报量/分钟 vs 网关实际业务 QPS 的比值基线，比值突变即管道异常，比等看板空白更早发现。

```javascript
const boardHealth = {
  selfSLA: { apiP95: 1000, availability: 0.999 },
  pipeline: {
    lag: (lastTs) => Date.now() - lastTs,            // 数据滞后
    ratioBaseline: (rumQps, gwQps) => rumQps / gwQps,   // 上报比基线（突降=SDK 故障）
    alert: (ratio) => ratio < 0.5 || ratio > 2,
  },
  fallback: async () => imBot.broadcast(coreMetricsSnapshot()),   // IM 兜底播报
};
```
