---
title: [BLD-096] CI 中的构建优化有哪些手段？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-096：CI 中的构建优化有哪些手段？
**答**：
- 依赖安装：frozen-lockfile + 包管理器全局缓存（setup-node/pnpm cache）+ 内网镜像；避免每次全量解析。
- 构建缓存：webpack cache/filesystem 目录、Vite node_modules/.vite、turbo 远程缓存按输入 hash 复用；缓存目录必须显式声明（CI 机器是干净容器）。
- 并发：独立包并行构建（turbo --parallel）、多 shard 测试与构建拆分、大 monorepo 用 affected（只构建变更包）。
- 增量与条件：按变更路径决定是否构建（nx affected / git diff --name-only）；node_modules 不在 docker 层反复重装（多阶段构建 + 层缓存）。

```yaml
# .github/workflows/ci.yml：缓存与增量要点
name: ci
on: [pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }               # 需要 diff 基线
      - uses: actions/setup-node@v4
        with: { node-version: 20 }
      - name: 恢复构建缓存（webpack/vite 通用）
        uses: actions/cache@v4
        with:
          path: |
            node_modules/.cache
            node_modules/.vite
          key: build-${{ runner.os }}-${{ hashFiles('pnpm-lock.yaml', 'webpack.config.js') }}
          restore-keys: build-${{ runner.os }}-
      - run: npm ci
      - name: 增量判断 只有前端目录变更才构建
        run: |
          if git diff --quiet origin/main --name-only -- frontend/; then
            echo "无前端变更 跳过构建"; exit 0;
          fi
          npm run build
      - name: turbo 远程缓存（monorepo）
        run: npx turbo build --api-url=$TURBO_API --team=$TURBO_TEAM --token=$TURBO_TOKEN
```
