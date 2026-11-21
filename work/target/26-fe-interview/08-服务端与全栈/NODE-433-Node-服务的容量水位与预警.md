---
title: [NODE-433] Node 服务的容量水位（headroom）预警机制如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-433：容量水位与预警
**答**:
- 容量水位定义：当前峰值流量 ÷ 当前配置容量，目标 headroom ≥ 40%（留故障与突发余量）；水位不是 CPU 使用率（那是瞬时值），而是"再涨 X% 就要扩容"的结构性指标。
- 水位维度：QPS 水位（压测容量 vs 峰值）、连接水位（DB/Redis 连接余量 NODE-405）、配额水位（下游配额/第三方 API）、带宽水位（CDN/负载均衡）。
- 预警机制：水位持续下降趋势（周环比）提前预警（业务增长快于扩容）；水位 < 30% 进扩容评审流程；水位 < 20% 触发紧急扩容预案。
- 数据来源自动化：压测结果登记（版本化——性能随代码变化，NODE-409 升级后重测）、峰值流量取近 4 周峰值（防大促数据失真，大促单独建模）。
- 与弹性联动：HPA max（NODE-375）按"max 配置下水位"评估——HPA 打满时水位 = 100%，需要调 max 或优化性能。
```javascript
function headroom({ peakQps, capacityPerReplica, replicas, maxReplicas }) {
  const cap = capacityPerReplica * replicas;
  const capMax = capacityPerReplica * maxReplicas;
  return { current: cap / peakQps,               // 当前水位
           withHpa: capMax / peakQps,            // HPA 打满水位
           action: cap / peakQps < 1.4 ? '扩容评审' : 'ok' };
}
```
