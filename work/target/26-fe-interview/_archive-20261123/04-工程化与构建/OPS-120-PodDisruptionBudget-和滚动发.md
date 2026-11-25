---
title: [OPS-120] PodDisruptionBudget 和滚动发布的 maxSurge/maxUnavailable 怎么设计？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-120：PodDisruptionBudget 和滚动发布的 maxSurge/maxUnavailable 怎么设计？
**答**：
- maxSurge 控制更新过程中最多多起几个 Pod（资源峰值），maxUnavailable 控制最多允许几个不可用副本；两者共同决定发布速度与容量曲线。
- 前端 SSR 服务推荐 maxUnavailable: 0 + maxSurge: 1：发布全程容量不降，速度慢一点但最平滑；能接受轻微降容可用 surge 25% + unavailable 25% 加速。
- PDB 管的是"自愿驱逐"（节点维护、drain）：保证驱逐时最少可用副本，避免发布没出事、节点维护把服务打挂。
- PDB 不拦截 Deployment 滚动更新，两者是互补关系，不要混淆。
- replicas 少于 3 的服务配 PDB 意义有限（minAvailable 2 + replicas 2 会阻塞一切驱逐），先把副本数提上来。

```yaml
# PDB + 滚动发布参数：发布平滑与节点维护保护双保险
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: web-frontend-pdb
  namespace: web-prod
spec:
  minAvailable: 2          # 节点 drain 等自愿驱逐时，至少保留 2 个可用副本
  selector:
    matchLabels: { app: web-frontend }
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-frontend
  namespace: web-prod
spec:
  replicas: 4
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1          # 更新中最多多起 1 个新 Pod，控制资源峰值
      maxUnavailable: 0    # 全程不允许可用副本下降，发布期间容量不缩水
  template:
    spec:
      containers:
        - name: web
          image: registry.example.com/web-frontend:1.42.0
```
