---
title: [ARC-023] Nx 的 affected 思想是什么？如何只构建受影响的包？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-023：Nx 的 affected 思想是什么？如何只构建受影响的包？
**答**：
- affected = 基于 git diff 找出本次变更的文件 → 映射到所属包 → 结合依赖图做闭包传播，得到"真正受影响的包集合"。
- 它的价值是把 CI 从"每次全量"变成"按图增量"，包越多收益越大。
- Turborepo 用 `--filter=...[origin/main]` 表达同样思想，核心都是"变更感知 + 依赖图闭包"。

```bash
# Nx：只测试受 origin/main 变化影响的包
nx affected:test --base=origin/main --parallel=3

# 等价的 pnpm + Turborepo 写法：从 main 分叉以来有改动的包及其下游
pnpm --filter "...[origin/main]" test
turbo run build test --filter=...[origin/main]

# 排查受影响集合（dry run，面试常问：如何验证 filter 写对了）
pnpm -r --filter "...[origin/main]" exec pwd
```
