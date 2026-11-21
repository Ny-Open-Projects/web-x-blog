---
title: [OPS-124] Helm 怎么管理前端应用？环境差异怎么收敛？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-124：Helm 怎么管理前端应用？环境差异怎么收敛？
**答**：
- 把 Deployment/Service/Ingress/HPA 模板化，环境差异（副本数、域名、灰度注解、资源）全部收敛到 values-{env}.yaml，模板零硬编码。
- image.tag 是独立参数由 CI 传入，禁止把镜像 tag 写死在 values 里（否则发布与配置变更纠缠）。
- 升级用 helm upgrade --install --atomic：失败自动回滚到上一 release；渲染结果先 helm template + kubectl diff 预检。
- helm history/rollback 是应用级回滚手段，与产物回滚（切版本目录）互补。
- values 变更与镜像升级分开提交，让"配置变更"和"版本发布"在审计里是两类事件（OPS-142）。

```bash
# Helm 管理前端应用：环境差异收敛到 values，镜像 tag 独立传参
# 目录结构：charts/web-frontend/{Chart.yaml, templates/}, values-{dev,staging,prod}.yaml

# 1. 预检渲染：模板产物与集群 diff，确认变更面
helm template web-frontend ./charts/web-frontend \
  -f charts/web-frontend/values-prod.yaml --set image.tag=1.42.0 \
  | kubectl diff -f - || true

# 2. 安装/升级：--atomic 失败自动回滚上一 release
helm upgrade --install web-frontend ./charts/web-frontend \
  -n web-prod \
  -f charts/web-frontend/values-prod.yaml \
  --set image.tag=1.42.0 \
  --atomic --wait --timeout 3m

# 3. 历史与回滚（应用级回滚，与产物级回滚互补）
helm history web-frontend -n web-prod
helm rollback web-frontend 12 -n web-prod --wait

# values-prod.yaml 关键片段（模板中全部走 .Values，无硬编码）：
#   replicaCount: 4
#   ingress: { host: www.example.com, canaryWeight: 0 }
#   resources: { requests: { cpu: 500m, memory: 512Mi }, limits: { memory: 512Mi } }
```
