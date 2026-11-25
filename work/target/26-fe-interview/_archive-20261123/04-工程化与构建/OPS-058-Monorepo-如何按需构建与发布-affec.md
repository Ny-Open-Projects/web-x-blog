---
title: [OPS-058] Monorepo 如何按需构建与发布（affected）？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-058：Monorepo 如何按需构建与发布（affected）？
**答**：
- 全量构建慢：每次 push 只构建受影响的包（affected），Turborepo/Nx 基于 DAG 依赖图 + git diff 计算。
- Turborepo：`--filter=...[origin/main]` 表示"main 基线以来受影响的包及其依赖"；远端缓存进一步让无变更的包零构建。
- 发布用 changesets/pnpm filter 圈定要发版本的包，CI 逐包发布。
- 陷阱：affected 的基线选择（merge base）在 MR 与 main 上不同，要统一约定；构建输出必须可校验（hash inputs），否则缓存误命中会出脏产物。

```bash
#!/usr/bin/env bash
# monorepo_release.sh：按需构建 + 按需发布
set -euo pipefail

BASE="${BASE:-origin/main}"          # CI 里设为 merge base

# 1. 查看 affected 范围（先看再构建）
npx turbo run build --dry=json --filter="...[${BASE}]" > /tmp/affected.json
echo "== affected packages =="
jq -r '.tasks[].taskId' /tmp/affected.json | sort -u

# 2. 只构建受影响的包（远端缓存命中则秒完成）
npx turbo run build lint test \
  --filter="...[${BASE}]" \
  --cache-dir=.turbo/cache

# 3. 按需发布：changesets 产出的版本变更包
if [ -f ".changeset/pending" ] || ls .changeset/*.md >/dev/null 2>&1; then
  npx changeset publish              # 发布所有有新版本的包
  git push --follow-tags
fi

# 4. 部署：只部署真正变更的应用
APPS=$(jq -r '.tasks[].taskId' /tmp/affected.json \
  | grep '^web-mall#' | cut -d'#' -f2 || true)
[ -n "$APPS" ] && ./scripts/deploy.sh production "$APPS" \
  || echo "web-mall 未变更，跳过部署"
```

---

## 七、环境与配置（OPS-059 ~ OPS-066）

环境与配置回答"代码怎么在多环境间无损流动"。核心原则：一份构建产物 + 多份配置；环境差异全部配置化；敏感信息永不落代码库。
