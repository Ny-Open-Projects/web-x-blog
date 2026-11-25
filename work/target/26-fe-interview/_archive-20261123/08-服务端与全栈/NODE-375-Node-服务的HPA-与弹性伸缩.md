---
title: [NODE-375] Node 服务的 HPA 与弹性伸缩策略如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-375：Node 服务的 HPA 与弹性伸缩
**答**:
- HPA 指标选择：CPU 利用率（通用但滞后——突发流量时扩容慢）、QPS/连接数（自定义指标更贴合容量模型）、队列 lag（消费类服务按积压扩容）。组合：CPU + 自定义指标双触发取最大。
- 弹性参数：min/max 副本（min ≥ 2 保可用性，max 按预算）、扩容行为（scaleUp 快：秒级反应突发，scaleDown 慢 + stabilizationWindow 防抖动——缩容过快导致连接迁移风暴）。
- 冷启动治理：Node 启动快（秒级），但预热（缓存回填/连接建立）要几十秒——readiness 探针延迟 ready，扩容后流量平滑进入；预测性扩容（大促前定时扩容，ARC-446）优于被动响应。
- 依赖联动：扩容 Pod 数增加 → DB 连接池总连接翻倍（NODE-332）——maxPoolSize × 副本数 ≤ DB 上限，或走 PgBouncer；下游服务同样需要容量余量（压测放大系数）。
- 收缩保护：夜间低谷缩容到 min；有状态任务（长请求/长连接 WS）节点缩容需 drain（NODE-346）。
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
spec:
  minReplicas: 3
  maxReplicas: 30
  metrics:
    - type: Resource
      resource: { name: cpu, target: { type: Utilization, averageUtilization: 65 } }
    - type: Pods
      pods: { metric: { name: http_qps }, target: { type: AverageValue, averageValue: 300 } }
  behavior:
    scaleDown: { stabilizationWindowSeconds: 300 }   # 缩容防抖 5 分钟
```
