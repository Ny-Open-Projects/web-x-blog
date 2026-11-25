---
title: [OPS-045] K8s 滚动更新与就绪探针如何配合保证发布无损？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-045：K8s 滚动更新与就绪探针如何配合保证发布无损？
**答**：
- 没有 readinessProbe 时，新 Pod 启动瞬间 nginx 可能还没监听，Service 就把流量打过去造成 502；readiness 通过前 Pod 不进 endpoints。
- readiness 探 /healthz（业务自检），liveness 探活失败会重启容器（别把依赖下游的检查放 liveness，避免雪崩）。
- strategy.rollingUpdate 的 maxUnavailable/maxSurge 控制"最少保几个可用、最多多起几个"，发布期间容量不掉。
- minReadySeconds + progressDeadlineSeconds：新 Pod 起来观察 N 秒无异常才算 ready，更新卡死自动标记失败并停止。

```yaml
# 滚动更新无损发布的关键配置
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-mall
spec:
  replicas: 4
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 0     # 发布期间可用副本数绝不减少
      maxSurge: 1           # 最多多起 1 个新 Pod，控制资源峰值
  minReadySeconds: 10       # 新 Pod ready 后再观察 10s 才继续
  progressDeadlineSeconds: 300   # 5 分钟没滚完判定发布失败
  selector: { matchLabels: { app: web-mall } }
  template:
    metadata: { labels: { app: web-mall } }
    spec:
      terminationGracePeriodSeconds: 30
      containers:
        - name: nginx
          image: registry.example.com/web-mall:v2026.11.01-abc1234
          readinessProbe:          # 不过 ready 的 Pod 不接流量
            httpGet: { path: /healthz, port: 80 }
            initialDelaySeconds: 2
            periodSeconds: 5
          livenessProbe:           # 挂了自动重启
            httpGet: { path: /healthz, port: 80 }
            initialDelaySeconds: 10
            periodSeconds: 10
          lifecycle:
            preStop:               # 收到终止信号先 sleep，等 LB 摘流再退出
              exec: { command: ["sh", "-c", "sleep 5"] }
```
