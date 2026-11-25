---
title: [OPS-121] Nginx Ingress 的 canary 灰度 annotation 怎么用？canary-weight 的局限是什么？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-121：Nginx Ingress 的 canary 灰度 annotation 怎么用？canary-weight 的局限是什么？
**答**：
- 机制：同一 host 建两个 Ingress，canary Ingress 打上 canary: "true" 注解，控制器先匹配 canary 规则再走主规则。
- 三种灰度维度可叠加：canary-weight（按比例）、canary-by-header（按请求头，内白名单定向）、canary-by-cookie（按用户 cookie，体验一致）。
- weight 的局限：按请求近似分流，不是按用户粘性——同一用户可能一会儿新一会儿旧；需要粘性就用 header/cookie 或入口层分桶（OPS-107）。
- 灰度版本与新版本 Service 对应，指标按版本 label 归因到看板。
- 放量 = 改 annotation 数值，变更留痕由 GitOps（OPS-125）或发布平台记录。

```yaml
# Nginx Ingress 金丝雀：主 Ingress 稳定版 + canary Ingress 按权重 10% 分流
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web-stable
  namespace: web-prod
spec:
  ingressClassName: nginx
  rules:
    - host: www.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: web-stable-svc
                port: { number: 80 }
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web-canary
  namespace: web-prod
  annotations:
    nginx.ingress.kubernetes.io/canary: "true"
    nginx.ingress.kubernetes.io/canary-weight: "10"      # 约 10% 流量进新版本
    # 需要用户粘性时改用（与 weight 互斥组合）：
    # nginx.ingress.kubernetes.io/canary-by-header: "X-Gray"
    # nginx.ingress.kubernetes.io/canary-by-header-value: "beta"
spec:
  ingressClassName: nginx
  rules:
    - host: www.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: web-canary-svc
                port: { number: 80 }
```
