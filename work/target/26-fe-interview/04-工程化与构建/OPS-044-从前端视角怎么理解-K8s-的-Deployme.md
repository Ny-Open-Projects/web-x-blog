---
title: [OPS-044] 从前端视角怎么理解 K8s 的 Deployment、Service、Ingress、HPA？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-044：从前端视角怎么理解 K8s 的 Deployment、Service、Ingress、HPA？
**答**：
- Deployment：声明"我要 3 个 nginx 容器跑这个镜像"，负责副本数与滚动更新；前端应用无状态，天然适配。
- Service：一组 Pod 的稳定虚拟 IP 与负载均衡，Pod 重建 IP 会变，Service 名字不变，集群内用 Service 名互访。
- Ingress：七层入口，按域名/路径把外部流量路由到 Service，等价于外面的 Nginx 配置，是发布与灰度的流量开关。
- HPA：根据 CPU/内存/自定义指标自动扩缩副本数，大促前手工扩容+HPA 兜底。

```yaml
# 前端应用的最小 K8s 全家桶：Deployment + Service + Ingress
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-mall
  labels: { app: web-mall }
spec:
  replicas: 3
  selector: { matchLabels: { app: web-mall } }
  template:
    metadata: { labels: { app: web-mall } }
    spec:
      containers:
        - name: nginx
          image: registry.example.com/web-mall:v2026.11.01-abc1234
          ports: [{ containerPort: 80 }]
          resources:
            requests: { cpu: 100m, memory: 64Mi }
            limits:   { cpu: 500m, memory: 256Mi }
---
apiVersion: v1
kind: Service
metadata:
  name: web-mall-svc
spec:
  selector: { app: web-mall }
  ports: [{ port: 80, targetPort: 80 }]
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web-mall-ingress
  annotations:
    nginx.ingress.kubernetes.io/limit-rps: "100"   # Ingress 层限流
spec:
  rules:
    - host: www.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend: { service: { name: web-mall-svc, port: { number: 80 } } }
```
