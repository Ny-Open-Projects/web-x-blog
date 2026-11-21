---
title: [RBL-254] monorepo 的 PR 级预览流水线怎么编排
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-254：monorepo 的 PR 级预览流水线怎么编排

**答**:
- 需求：PR 只构建/测试受影响应用 + 部署预览环境——affected 计算是核心；多应用 monorepo 全量 CI 不可持续
- 流水线：affected apps → 动态生成 CI job（矩阵）→ build with remote cache → deploy preview（per-PR URL）→ 评论部署链接与产物 diff
- 资源控制：预览环境自动回收（PR 关闭/超 7 天）；并发预览配额（避免分支爆炸）
- 产物关联：预览部署带 commit sha 与 affected 集合标记——QA 反馈能精确关联代码版本

```yaml
# GitHub Actions 动态矩阵示意
jobs:
  detect:
    outputs: { apps: ${{ steps.affected.outputs.apps }} }
  build:
    needs: detect
    strategy: { matrix: { app: ${{ fromJSON(needs.detect.outputs.apps) }} } }
    steps:
      - run: turbo build --filter=${{ matrix.app }}
      - run: deploy preview --alias=pr-${{ github.event.number }}-${{ matrix.app }}
```
