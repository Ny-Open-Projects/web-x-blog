---
title: [NODE-467] Node 服务的运行时依赖健康度（DB/Redis/下游）监控如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-467：运行时依赖健康度监控
**答**:
- 视角：服务视角看每个依赖的"健康画像"——不只依赖方自己的监控，还要从我的服务侧度量依赖对我的服务质量（对齐 SLA 契约）。
- 画像指标（按依赖分桶）：可用性（连接成功率）、延迟（P95）、错误类型分布（超时/拒绝/5xx——错误类型决定处理策略）、饱和信号（连接池等待 NODE-332/Redis 慢命令/下游 429）。
- 告警设计：依赖劣化早期信号（P95 上升/错误类型漂移——比全挂早发现）、依赖与我共同故障 vs 依赖单方故障的区分（我调用失败率升 but 依赖自身监控正常 → 我的问题：连接池/超时配置）。
- 与处置联动：依赖画像直接挂接降级策略（NODE-390 降级声明引用健康度——Redis 健康分 < 阈值自动降级）、熔断器状态可视化（半开探测中）。
- 供应商 SLA 对账：依赖方承诺 SLA vs 实测月报（违约记录——容量与商务谈判依据 NODE-436）。
```javascript
// 依赖健康分（按依赖维度）
function depHealth(dep, window = '5m') {
  const m = metrics.of(dep, window);
  return { avail: m.connectOk / m.connectTotal,
           p95: m.durationP95, errMix: topErrorTypes(m.errors),
           score: m.avail * 0.6 + (m.durationP95 < budget(dep) ? 0.4 : 0.2) };
}
// 降级联动：if (depHealth('redis').score < 0.6) degradeRegistry.redis.degradeWhen = true;
```
