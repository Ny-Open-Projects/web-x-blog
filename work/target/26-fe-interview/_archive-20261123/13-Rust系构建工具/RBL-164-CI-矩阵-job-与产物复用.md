---
title: [RBL-164] CI 矩阵拆 job：构建/测试/多环境怎么编排
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-164：CI 矩阵拆 job：构建/测试/多环境怎么编排

**答**：
- 拆分维度：职责拆（build/lint/test 并行 job）+ 数据拆（测试 shard 矩阵）+ 环境拆（Node 版本/OS 矩阵）。职责拆是收益最大且零风险的。
- job 间产物传递：build job 的 dist 通过 artifact upload，test job download——测试 job 不再重复构建；用 needs 表达依赖链。
- 防雪崩：needs + fail-fast 控制策略；build 失败时下游测试不启动省机器时。
- 代价核算：每个 job 的 runner 启动 + checkout + install 开销（约 1~3 分钟），拆太碎反而变慢；优先合并轻任务（lint+typecheck 一个 job 并行跑）。
- 追问钩子：矩阵配合缓存的 key 要含矩阵维度（node-version、shard index），否则 job 互相覆盖缓存。

```yaml
# GitHub Actions 矩阵编排
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pnpm install --frozen-lockfile && pnpm --filter @app/web build
      - uses: actions/upload-artifact@v4
        with: { name: dist, path: apps/web/dist }
  test:
    needs: build
    strategy:
      fail-fast: false
      matrix: { shard: [1, 2, 3, 4] }
    steps:
      - uses: actions/checkout@v4
      - uses: actions/download-artifact@v4
        with: { name: dist, path: apps/web/dist }   # 复用产物，不重复构建
      - run: vitest run --shard=${{ matrix.shard }}/4
```
