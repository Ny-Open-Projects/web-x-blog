---
title: [OPS-054] dev/test/staging/prod 多环境多分支流水线怎么设计？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-054：dev/test/staging/prod 多环境多分支流水线怎么设计？
**答**：
- 分支模型与环境映射：MR → dev 自测，main 常驻 → 自动部署 test，tag/release 分支 → staging 验证 → 生产手动审批。
- 核心纪律：环境只进不退（代码只能向高环境晋升），同一构建产物逐环境晋升，绝不"每个环境重新构建"（避免环境间产物不一致）。
- 环境间差异只体现在配置（ConfigMap/env），不体现在构建产物里。
- 每个环境有独立 Ingress 域名与数据隔离（staging 用脱敏数据），防止误打生产库。

```yaml
# .github/workflows/promote.yml：按分支自动晋升环境
name: promote
on:
  push:
    branches: [main, release/*]      # main -> test；release/* -> staging+prod
  workflow_dispatch:
    inputs:
      env: { description: target env, required: true, type: choice,
             options: [dev, test, staging, production] }

jobs:
  build-once:
    runs-on: ubuntu-latest
    outputs: { version: "${{ steps.v.outputs.ver }}" }
    steps:
      - uses: actions/checkout@v4
      - run: pnpm install --frozen-lockfile && pnpm build
      - id: v
        run: echo "ver=$(git rev-parse --short HEAD)" >> $GITHUB_OUTPUT
      - uses: actions/upload-artifact@v4
        with: { name: dist, path: dist }

  deploy-test:
    needs: build-once
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment: test
    steps: { run: ./scripts/deploy.sh test "${{ needs.build-once.outputs.version }}" }

  deploy-staging:
    needs: build-once
    if: startsWith(github.ref, 'refs/heads/release/')
    runs-on: ubuntu-latest
    environment: staging
    steps: { run: ./scripts/deploy.sh staging "${{ needs.build-once.outputs.version }}" }

  deploy-production:
    needs: [build-once, deploy-staging]
    if: startsWith(github.ref, 'refs/heads/release/')
    runs-on: ubuntu-latest
    environment: production          # 受保护环境：需审批 + 仅允许 release/* 分支
    steps:
      - run: ./scripts/deploy.sh production "${{ needs.build-once.outputs.version }}"
      - run: node scripts/smoke.js
```
