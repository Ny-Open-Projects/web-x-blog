---
title: [OPS-125] GitOps（ArgoCD）与 CI/CD 有什么区别？前端团队怎么落地？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-125：GitOps（ArgoCD）与 CI/CD 有什么区别？前端团队怎么落地？
**答**：
- CI/CD 是"推"模式：流水线拿着凭证往集群里部署；GitOps 是"拉"模式：集群侧控制器持续比对 Git 声明与实际状态，Git 仓库成为唯一事实源。
- 收益：漂移自愈（有人手改集群自动纠正）、变更全在 Git 可审计可回滚（git revert 即回滚）、凭证不外泄。
- 落地分工：CI 负责构建测试并推送新镜像 tag 到部署仓库，ArgoCD 监听部署仓库自动同步；发布 = 一次 git commit。
- 部署仓库（manifests）与应用代码仓库分离，PR 评审就是生产变更评审；灰度权重调整也是改 Git。
- selfHeal+prune 开启前先在非生产验证，防止误删与意外纠正引发事故。

```yaml
# ArgoCD Application：web-frontend 生产环境声明
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: web-frontend-prod
  namespace: argocd
spec:
  project: frontend
  source:
    repoURL: https://git.example.com/platform/deploy-frontend.git   # 部署仓库：与代码仓库分离
    targetRevision: main
    path: overlays/prod                 # kustomize overlay 或 helm values 目录
  destination:
    server: https://kubernetes.default.svc
    namespace: web-prod
  syncPolicy:
    automated:
      prune: true          # Git 中删除的资源，集群同步删除
      selfHeal: true       # 有人绕过 Git 手改集群 → 自动纠正回 Git 声明（防漂移）
    syncOptions: ["CreateNamespace=true"]
  revisionHistoryLimit: 10  # 保留同步历史，ArgoCD 界面可一键回滚到任一 revision
```
