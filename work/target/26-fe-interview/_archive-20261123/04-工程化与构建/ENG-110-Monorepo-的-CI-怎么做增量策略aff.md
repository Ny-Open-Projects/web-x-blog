---
title: [ENG-110] Monorepo 的 CI 怎么做增量策略？affected 怎么计算？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-110：Monorepo 的 CI 怎么做增量策略？affected 怎么计算？
**答**：
- 原理：根据本次 diff 改了哪些包，结合依赖图算出"受影响包集合"，只构建/测试这些包。
- Turborepo：turbo run build test --affected，基于 git diff 自动判定，配合远程缓存效果最佳。
- 无 Turborepo 时用 git 估算：diff 路径前缀映射到包名，再手动补依赖闭包（上游变下游也要跑）。
- CI 提速预期：改动集中在单包时，流水线时长从"全仓构建"降到"单包构建"，是大仓库 CI 的分水岭。

```bash
# Turborepo：自动计算受影响包，只跑受影响范围
pnpm turbo run build test --affected

# 无 Turborepo 的 git 估算：路径前缀映射到包
CHANGED=$(git diff --name-only origin/main...HEAD | cut -d/ -f1-2 | sort -u)
echo "$CHANGED"
if echo "$CHANGED" | grep -q '^packages/ui'; then
  pnpm --filter @myorg/ui... build   # 注意 ... 后缀：连同依赖它的包一起构建
fi
```
