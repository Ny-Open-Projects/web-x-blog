---
title: [OPS-123] 资源 requests/limits 怎么定？与 QoS 等级什么关系？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-123：资源 requests/limits 怎么定？与 QoS 等级什么关系？
**答**：
- requests 是调度依据（节点按 requests 容纳 Pod），limits 是运行上限；requests=limits 的容器是 Guaranteed 级，最不容易被驱逐。
- Node 服务是内存敏感型：limits.memory 低于真实峰值会被 OOMKill，建议内存 requests=limits（Guaranteed），按压测 P99 × 1.3 设定。
- CPU limit 会造成 throttle：SSR 高并发时 CPU 被限流表现为延迟飙升而非报错，纯静态容器与 Node 服务常只设 CPU request 不设 limit。
- BestEffort（都不设）与 Burstable 的 Pod 在节点资源紧张时先被驱逐——生产服务至少 Burstable，核心服务 Guaranteed。
- requests 定太小会让节点超卖导致 CPU 争抢，监控 throttling 与 OOM 事件反推调整。

```yaml
# 资源配置与 QoS：Node 服务内存 Guaranteed、CPU 不设 limit
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-ssr
  namespace: web-prod
spec:
  template:
    spec:
      containers:
        - name: web
          image: registry.example.com/web-ssr:1.42.0
          resources:
            requests:
              cpu: "500m"
              memory: 512Mi
            limits:
              memory: 512Mi       # 内存 requests=limits → Guaranteed 级，驱逐最后梯队
              # CPU 故意不设 limit：SSR 并发尖峰被 throttle 的表现是延迟飙升，比报错更难排查
          # 纯静态 nginx 容器：Burstable 即可（request cpu 100m / mem 64Mi）
```
