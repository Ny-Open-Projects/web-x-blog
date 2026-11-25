---
title: [ARC-362] 前端基建：CI 构建缓存体系如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-362：前端基建：CI 构建缓存体系如何设计？
**答**：
- CI 提速的本质是"复用一切确定性产物"：依赖缓存、构建产物缓存、测试分片结果、lint 缓存；正确性前提是输入指纹（lockfile + 源码哈希）完全一致。
- 分层缓存：npm/pnpm store 按锁文件哈希缓存（命中率高、收益大）；Turborepo/Nx 远端任务缓存按任务输入签名；产物缓存供部署复用。
- 缓存失效策略：默认保守（任何输入变更即失效），避免脏产物；定时全量构建兜底（每周强制绕过缓存）。
- 远端缓存的安全：缓存投毒风险——只允许 CI 写入，PR 产物与主道产物隔离；签名校验。
- 度量：缓存命中率、任务平均耗时、P95 CI 时长；命中率达 80% 以上才算体系建成。
```yaml
# GitHub Actions 缓存示例
- uses: actions/setup-node@v4
  with: { node-version: 20 }
- uses: actions/cache@v4
  with:
    path: ~/.pnpm-store
    key: pnpm-${{ hashFiles('pnpm-lock.yaml') }}   # 锁文件指纹
- run: pnpm install --frozen-lockfile
- run: pnpm turbo build --cache-dir=.turbo --api=remote  # 远端任务缓存
```
