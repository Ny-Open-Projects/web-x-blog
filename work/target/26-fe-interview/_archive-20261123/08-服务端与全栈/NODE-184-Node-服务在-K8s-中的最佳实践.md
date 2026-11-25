---
title: [NODE-184] Node 服务在 K8s 中的最佳实践？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-184：Node 服务在 K8s 中的最佳实践？
**答**：
- 探针分工：readiness（依赖就绪才接流量）+ liveness（条件要宽，误判引发重启风暴）；`terminationGracePeriodSeconds` 对齐优雅退出（NODE-060）。
- **preStop sleep 5s** 是关键细节：等 endpoint 摘除传播完成再停进程，滚动更新零 502。
- 资源：CPU limit 会限流（CFS throttling），Node 服务建议只设 request 或放宽 limit；内存 limit 对齐 heap 上限 + 余量（NODE-082）。
- 滚动策略：`maxUnavailable: 0` 保吞吐；环境变量注入 `UV_THREADPOOL_SIZE` 等运行时参数。

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: bff
spec:
  replicas: 4
  strategy:
    rollingUpdate: { maxSurge: 1, maxUnavailable: 0 }   # 滚动不缩容
  template:
    spec:
      terminationGracePeriodSeconds: 30
      containers:
        - name: bff
          image: registry/bff:1.8.0
          resources:
            requests: { cpu: "500m", memory: 512Mi }
            limits: { memory: 1Gi }            # 不设 CPU limit，避免 CFS 限流
          env: [{ name: UV_THREADPOOL_SIZE, value: "8" }]
          readinessProbe: { httpGet: { path: /readyz, port: 3000 }, periodSeconds: 5 }
          livenessProbe:
            httpGet: { path: /healthz, port: 3000 }
            periodSeconds: 10
            failureThreshold: 3                 # liveness 条件要宽，防重启风暴
          lifecycle:
            preStop:
              exec: { command: ["sh", "-c", "sleep 5"] }  # 等 endpoint 摘除生效
```
