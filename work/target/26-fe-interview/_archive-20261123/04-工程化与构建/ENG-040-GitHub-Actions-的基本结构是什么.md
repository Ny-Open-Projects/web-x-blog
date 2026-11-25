---
title: [ENG-040] GitHub Actions 的基本结构是什么？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-040：GitHub Actions 的基本结构是什么？
**答**：
- workflow 文件放在 .github/workflows/ 下，用 YAML 描述：name、on 触发条件、jobs、steps。
- job 是调度与容错的最小单元，默认并行；step 是步骤，可以是 uses 复用 action 或 run 执行命令。
- 常用触发：push、pull_request、release、schedule、workflow_dispatch（手动）。
- 缓存依赖用 setup-node 的 cache 参数，基于 lockfile hash 命中。

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm
      - run: npm ci
      - run: npm run build
```
