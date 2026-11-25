---
title: [OPS-119] 前端 SSR/BFF 服务怎么做 HPA 弹性伸缩？指标怎么选？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-119：前端 SSR/BFF 服务怎么做 HPA 弹性伸缩？指标怎么选？
**答**：
- CPU 利用率是最简单的指标，但 Node 事件循环模型下 CPU 与并发不完全相关，建议叠加每 Pod 并发请求数（http_requests_inflight）双指标。
- minReplicas 至少 3：抗单节点故障，同时保证滚动更新期间容量不下探。
- 缩容要防抖：stabilizationWindowSeconds 给 5 分钟稳定窗，限制缩容速率，避免流量谷底反复扩缩。
- 扩容比缩容激进（秒级扩、分钟级缩），突发流量下 CPU 指标有采集延迟，可配合定时伸缩应对已知峰值（大促预热）。
- HPA 只管"Pod 数"，单 Pod 资源上限由 requests/limits 决定（OPS-123），两层要一起规划。

```yaml
# web-ssr 服务的 HPA：CPU + 并发双指标，扩缩速率不对称
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: web-ssr-hpa
  namespace: web-prod
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: web-ssr
  minReplicas: 3            # 抗单节点故障 + 滚动更新不掉底
  maxReplicas: 20
  metrics:
    - type: Resource
      resource:
        name: cpu
        target: { type: Utilization, averageUtilization: 65 }
    - type: Pods
      pods:
        metric:
          name: http_requests_inflight    # 需要 prometheus-adapter 注册自定义指标
        target: { type: AverageValue, averageValue: "200" }
  behavior:
    scaleUp:                    # 扩容激进：30 秒内可翻倍
      policies: [{ type: Percent, value: 100, periodSeconds: 30 }]
    scaleDown:                  # 缩容保守：5 分钟稳定窗，每次最多收 25%
      stabilizationWindowSeconds: 300
      policies: [{ type: Percent, value: 25, periodSeconds: 60 }]
```
