---
title: [OPS-050] GitHub Actions 完整 workflow 怎么写（矩阵构建、缓存、产物、部署）？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-050：GitHub Actions 完整 workflow 怎么写（矩阵构建、缓存、产物、部署）？
**答**：
- 结构上按 job 拆分：test（矩阵跑多 Node 版本）→ build（上传 artifact）→ deploy（仅 main，下载 artifact 后 rsync/SSH 部署），job 间用 needs 串联。
- 缓存两层：pnpm store（actions/cache）与构建产物缓存；用 concurrency 取消同分支过期运行，省 runner。
- 生产凭证全部走 Secrets，部署用最小权限 SSH key；并发部署用 concurrency group 串行化。
- 发布信息（sha、run id）注入产物版本号，保证"线上版本 ↔ 构建记录"可追溯。

```yaml
# .github/workflows/release.yml
name: release
on:
  push:
    branches: [main]

concurrency:                       # 同分支只保留最新一次运行
  group: release-${{ github.ref }}
  cancel-in-progress: true

env: { PNPM_VERSION: "9" }

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix: { node: ["20", "22"] }   # 矩阵：多 Node 版本兼容验证
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
        with: { version: 9 }
      - uses: actions/setup-node@v4
        with: { node-version: "${{ matrix.node }}", cache: pnpm }
      - run: pnpm install --frozen-lockfile
      - run: pnpm lint && pnpm test --coverage

  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
        with: { version: 9 }
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: pnpm }
      - run: pnpm install --frozen-lockfile
      - run: pnpm build
        env:
          VITE_APP_VERSION: ${{ github.sha }}
      - uses: actions/upload-artifact@v4     # 产物在 job 间传递并留档
        with:
          name: dist-${{ github.sha }}
          path: dist/
          retention-days: 30

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment: production                  # 关联保护环境（审批/限制分支）
    steps:
      - uses: actions/download-artifact@v4
        with: { name: dist-${{ github.sha }}, path: dist }
      - name: Deploy to production
        env: { SSH_KEY: "${{ secrets.DEPLOY_KEY }}" }
        run: |
          echo "$SSH_KEY" > /tmp/k && chmod 600 /tmp/k
          rsync -azc -e "ssh -i /tmp/k -o StrictHostKeyChecking=yes" \
            dist/ deploy@web01:/data/web/mall/releases/${GITHUB_SHA::8}/
          ssh -i /tmp/k deploy@web01 \
            "ln -sfn /data/web/mall/releases/${GITHUB_SHA::8} /data/web/mall/current"
      - run: node scripts/smoke.js           # 部署后冒烟
```
