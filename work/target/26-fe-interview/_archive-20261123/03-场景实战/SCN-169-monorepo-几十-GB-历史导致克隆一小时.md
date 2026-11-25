---
title: [SCN-169] monorepo 几十 GB 历史导致克隆一小时起步，新同学与 CI 如何提速？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-169：monorepo 几十 GB 历史导致克隆一小时起步，新同学与 CI 如何提速？
**答**：
- 三板斧：浅克隆（`--depth=1` 砍历史）、部分克隆（`--filter=blob:none` 按需拉 blob）、sparse-checkout（只检需要的子目录），组合使用克隆时间从小时级降到分钟级。
- CI 优先用缓存 + 浅克隆：构建只需要最新提交与增量 diff，`fetch-depth: 1` 是默认该做的事。
- Git 镜像/内部代理加速大文件：LFS 或构建产物不要进 git 历史，用制品库。
- 文档化"开发者默认克隆姿势"，新人引导脚本内置这些参数，而不是靠口口相传。

```bash
# 大仓库克隆优化：浅克隆 + blob 按需 + 子目录稀疏检出
# 1. 部分克隆：不下载历史 blob，检出时按需拉取
git clone --depth=1 --filter=blob:none --sparse git@git.example.com:corp/monorepo.git
cd monorepo

# 2. 只检出本团队负责的子目录
git sparse-checkout set packages/web-app apps/h5

# 3. 需要追溯历史时按需加深（只拉取近 30 条）
git fetch --deepen=30

# 4. 查看某文件历史：自动按需下载对应 blob，不用全量历史
git log --oneline -- packages/web-app/src/index.ts

# CI 侧（以 GitHub Actions 为例）：单提交 + sparse
# jobs.build.steps:
#   - uses: actions/checkout@v4
#     with:
#       fetch-depth: 1        # 浅克隆
#       sparse-checkout: packages/web-app
#       filter: blob:none     # blob 按需

# 5. 构建产物与设计资源走制品库，禁止进 git（仓库瘦身守则）
find . -size +10M -not -path './.git/*'   # CI 定期扫大文件报警
```
