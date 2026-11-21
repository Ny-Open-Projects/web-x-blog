---
title: [ARC-026] Monorepo 的 CI 策略如何设计（增量构建/测试）？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-026：Monorepo 的 CI 策略如何设计（增量构建/测试）？
**答**：
- 三层增量：PR 只跑 affected 包 → 远程缓存命中跳过重复任务 → main 全量校验兜底。
- 发布与 CI 分离：CI 校验，main 上的版本机器人负责发版（changesets action）。
- 必须缓存 pnpm store + turbo 远程缓存，否则增量收益被安装时间吃掉。

```yaml
# .github/workflows/ci.yml —— Monorepo 增量 CI
on: { pull_request: {}, push: { branches: [main] } }
jobs:
  ci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }        # affected 需要 git 历史
      - uses: pnpm/action-setup@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: pnpm }
      - run: pnpm install --frozen-lockfile
      - name: Build & Test (affected only)
        run: |
          if [ "${{ github.event_name }}" = "pull_request" ]; then
            pnpm turbo build test lint --affected    # PR：只跑受影响包
          else
            pnpm turbo build test lint               # main：全量兜底
          fi
      - uses: dtinth/setup-github-actions-caching-for-turbo@v1  # turbo 远程缓存
```
