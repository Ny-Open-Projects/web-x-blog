---
title: [ENG-133] CI 中构建产物差异报告 size diff bot 怎么完整实现？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-133：CI 中构建产物差异报告 size diff bot 怎么完整实现？
**答**：
- 体积回归是温水煮青蛙：单次 PR 看不出来，累计三个月 bundle 翻倍，必须有机器盯。
- CI 在 PR 构建产物后与基线（默认分支最近一次构建归档）做逐文件 diff，生成 markdown 表评论到 PR。
- 阈值两层：单文件超 10% 告警评论，总体超 2% 走 gate 阻断合并（维护者可带 label 豁免）。
- 基线维护：main 合入后异步更新基线文件进仓库或制品库，保证 diff 永远对着最近可发布版本。

```yaml
# .github/workflows/size-diff.yml —— PR 体积差异报告完整流水线
name: size-diff
on: pull_request
permissions:
  pull-requests: write
jobs:
  size-diff:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: pnpm }
      - run: pnpm install --frozen-lockfile && pnpm build

      - name: 生成与基线的差异报告
        run: node scripts/size-report.mjs dist --baseline ./size-baseline.json --out size-diff.md

      - name: 评论到 PR sticky 防刷屏
        uses: marocchino/sticky-pull-request-comment@v2
        with: { header: size-diff, path: size-diff.md }

      - name: 卡口 单文件 10% 总体 2%
        run: node scripts/size-gate.mjs size-diff.md --single-file 10 --total 2
```
