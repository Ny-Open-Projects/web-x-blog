---
title: [MFW-159] 元框架应用的 CI/CD 流水线怎么设计（预览环境 + 灰度）？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-159：元框架应用的 CI/CD 流水线怎么设计（预览环境 + 灰度）？
**答**：
- 流水线五段：lint/typecheck（快失败）→ 单测 + 构建缓存 → **预览环境**（每个 PR 一个独立 URL，Vercel Preview / K8s 动态命名空间）→ 合并主干 → 生产发布（蓝绿/金丝雀）。
- 预览环境要点：私有依赖 token、种子数据、后端 mock/staging 域名注入；预览 URL 自动评论回 PR，方便产品/测试验收。
- 灰度发布：按流量比例（Nginx/K8s Ingress 权重）或按用户（cookie/uid 哈希，同用户稳定同版本）；配套指标看板（错误率、Web Vitals）与一键回滚。
- 发布产物版本化：镜像 tag 用 commit sha（不可变），静态资源指纹上传 CDN；「回滚 = 切回旧镜像 tag」而不是重新构建。
- 安全卡口：依赖审计（npm audit/renovate）、构建产物扫描、secrets 不进日志。

```yaml
# .github/workflows/deploy.yml 核心（伪流水线）
# on: pull_request
# jobs:
#   ci:
#     steps:
#       - run: npm ci --cache .npm       # 缓存依赖
#       - run: npm run lint && npm run typecheck
#       - run: npm test -- --coverage
#       - run: npm run build             # 构建即验证
#   preview:
#     needs: ci
#     steps:
#       - run: ./scripts/deploy-preview.sh ${{ github.event.number }}   # PR 号命名空间
#       - uses: ./.github/actions/pr-comment             # 回评预览 URL

# 生产（合并后）：
#   deploy-prod:
#     steps:
#       - run: docker build -t reg/app:${{ github.sha }} .
#       - run: kubectl set image deploy/app app=reg/app:${{ github.sha }}
#       - run: kubectl rollout status deploy/app --timeout=120s  # 灰度滚动 + 自动失败回滚
#       # 金丝雀：argocd rollouts 或 istio 按 uid 哈希 5% -> 25% -> 100%
```
