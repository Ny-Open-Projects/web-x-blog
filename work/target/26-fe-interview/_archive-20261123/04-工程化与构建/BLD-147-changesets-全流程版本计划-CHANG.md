---
title: [BLD-147] changesets 全流程：版本计划、CHANGELOG、多包联动发版怎么跑？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-147：changesets 全流程：版本计划、CHANGELOG、多包联动发版怎么跑？
**答**：
- 流程四步：开发者 `pnpm changeset`（交互式选包、选 semver 级别、写摘要）→ 生成 `.changeset/*.md` 随 PR 提交 → 合并到 main 后 CI 跑 `changeset version`（消费 md 更新各包 version + CHANGELOG + **内部依赖联动 bump**）→ `changeset publish`（CI 手动触发发布）。
- 多包联动：A 依赖 B 且 B 升 minor，changesets 自动把 A 升 patch 并把 `workspace:*` 改写为真实版本号——monorepo 发版的正确姿势（对比 lerna 固定/独立模式）。
- GitHub Actions 标准玩法：**changesets/action** 两步——version PR（聚合所有待发 changeset 成一个 PR）+ 人工 approve 后 publish；npm token 用 `NPM_TOKEN` secret + provenance（`NPM_CONFIG_PROVENANCE: true`）。
- 预发布：`changeset pre enter beta` 进入 prerelease 模式，包版本走 `1.0.0-beta.x` 递增，`pre exit` 回正式。

```json
// .changeset/config.json：核心策略配置
{
  "$schema": "https://unpkg.com/@changesets/config/schema.json",
  "changelog": ["@changesets/changelog-github", { "repo": "org/repo" }],
  "commit": false,                       // version 产生的变更由 action 统一提交
  "access": "public",
  "baseBranch": "main",
  "updateInternalDependents": "always",  // 内部依赖变化必联动 bump（比默认 always 语义更清晰）
  "ignore": ["@repo/e2e"]                // 不发布的包
}
```

```yaml
# .github/workflows/release.yml：changesets 官方 action 的生产配置
name: release
on:
  push:
    branches: [main]
concurrency: { group: release, cancel-in-progress: false }
jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }
      - uses: pnpm/action-setup@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: pnpm, registry-url: 'https://registry.npmjs.org' }
      - run: pnpm install --frozen-lockfile
      - uses: changesets/action@v1
        with:
          version: pnpm changeset version      # 消费 .changeset/*.md → 版本+CHANGELOG
          publish: pnpm build && pnpm changeset publish
          title: 'chore: version packages'
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
          NPM_CONFIG_PROVENANCE: true          # npm provenance：发布与源码构建可追溯
```
