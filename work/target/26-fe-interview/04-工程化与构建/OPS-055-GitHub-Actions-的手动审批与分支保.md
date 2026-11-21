---
title: [OPS-055] GitHub Actions 的手动审批与分支保护怎么配置？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-055：GitHub Actions 的手动审批与分支保护怎么配置？
**答**：
- Actions 用 environment 承载审批：给 environment（如 production）配置 required reviewers，deploy job 引用后进入时暂停等审批。
- 分支保护双保险：main 禁止直推、要求 PR + CI 通过 + code review；environment 限制 deployment_branch_policy 只允许指定分支部署。
- 审批记录自动留痕（谁在何时批准了哪个 run），满足审计要求。
- 紧急修复场景配 bypass 权限要克制，事后必须补 review。

```yaml
# .github/workflows/deploy-prod.yml（配合仓库 Settings 的环境与分支保护）
name: deploy-prod
on:
  workflow_dispatch:            # 只允许手动触发生产发布
    inputs:
      version:
        description: git sha or tag to deploy
        required: true

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: production          # 该环境配置 required reviewers，进入即暂停审批
      url: https://www.example.com
    steps:
      - uses: actions/checkout@v4
        with: { ref: "${{ inputs.version }}" }   # 只部署审查过的 commit
      - run: pnpm install --frozen-lockfile && pnpm build
      - run: ./scripts/deploy.sh production
      - run: node scripts/smoke.js

# 仓库设置（Settings -> Environments -> production）：
#   - Required reviewers: release-manager, fe-oncall（至少 1 人审批）
#   - Deployment branches: 仅 release/* 与 hotfix/*
# 分支保护（Settings -> Branches -> main）：
#   - require pull request + 1 approve
#   - require status checks: lint, test, build 全绿
#   - 禁止 force push 与直接 push
```
