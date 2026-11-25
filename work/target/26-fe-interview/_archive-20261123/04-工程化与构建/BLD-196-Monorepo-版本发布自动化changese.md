---
title: [BLD-196] Monorepo 版本发布自动化：changesets + turbo + CI 完整实例。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-196：Monorepo 版本发布自动化：changesets + turbo + CI 完整实例。
**答**：
- 编排：PR 阶段 `changeset` 文件收集意图 → 合并后 `changesets/action` 生成 version PR（联动内部依赖 bump，BLD-147）→ version PR 合并后 publish 阶段**先 turbo 按拓扑构建受影响包**再逐包 `changeset publish`。
- 关键组合点：发布前必须保证产物新鲜——`turbo build --filter=$CHANGED_PACKAGES` 只构建有版本变更的包（用 `changeset status --json` 或 git diff 判定），避免全仓构建。
- npm 侧：`publishConfig` 指向公开 registry、provenance 开启、tag 策略（beta 通道用 `changeset pre`）。
- 失败恢复：publish 中途失败（网络）→ `changeset publish` 幂等（已发布的包自动跳过），重跑即可；CI 用 concurrency 锁防并发发布。

```yaml
# .github/workflows/monorepo-release.yml：changesets + turbo 完整编排
name: release
on: { push: { branches: [main] } }
concurrency: { group: release-${{ github.ref }}, cancel-in-progress: false }
jobs:
  version-or-publish:
    runs-on: ubuntu-latest
    permissions: { contents: write, pull-requests: write, id-token: write }
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }
      - uses: pnpm/action-setup@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: pnpm, registry-url: 'https://registry.npmjs.org' }
      - run: pnpm install --frozen-lockfile
      - id: changesets
        uses: changesets/action@v1
        with:
          version: pnpm changeset version
          publish: pnpm release:publish            # 见 package.json
          title: 'chore: version packages'
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
          NPM_CONFIG_PROVENANCE: 'true'
```

```json
// package.json（根）：publish 编排——先拓扑构建变更包，再发布
{
  "scripts": {
    "release:publish": "pnpm build:changed && pnpm changeset publish",
    "build:changed": "turbo run build --filter=$(node scripts/changed-pkgs.js)"
  }
}
```

```javascript
// scripts/changed-pkgs.js：从 changeset 状态提取需构建的包（--filter 参数）
const { execSync } = require('child_process');
const status = JSON.parse(execSync('pnpm changeset status --output=-', { encoding: 'utf8' }));
const names = [...new Set(status.releases.map((r) => r.name))];
// 转成 turbo filter：包本身 + 其依赖闭包（依赖也要最新构建）
const filter = names.map((n) => `--filter=${n}...`).join(' ');
console.log(filter || '--filter=[]');   // 无变更时空集（changeset publish 自会跳过）
// 幂等性：changeset publish 对已发布版本自动跳过 → CI 重跑安全
```
