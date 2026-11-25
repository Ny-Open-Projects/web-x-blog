---
title: [BLD-094] 什么是构建确定性？如何用 lockfile、Node 版本锁定与缓存 key 设计保证？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-094：什么是构建确定性？如何用 lockfile、Node 版本锁定与缓存 key 设计保证？
**答**：
- 定义：同一 commit 在任何机器、任何时间构建出"哈希一致"的产物；这是缓存复用、安全审计、灰度回滚的前提。
- 三支柱：lockfile（依赖解析确定）+ Node/包管理器版本锁定（engines、volta、corepack）+ 构建配置与环境变量收敛（禁用时间戳、随机 id、绝对路径进产物）。
- 常见破坏源：构建脚本写入 Date.now()、__dirname 进产物、依赖 semver 漂移（无 lock）、css 顺序不稳定（并行插件输出顺序不确定）。
- 缓存 key 设计：CI 缓存 key 应含 lockfile hash + 工具版本 + 配置文件 hash；产物级 key 用内容哈希（contenthash）而不是构建号。

```yaml
# .github/workflows/build.yml：确定性构建三件套
name: build
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Node 版本锁定
        uses: actions/setup-node@v4
        with: { node-version-file: '.nvmrc', cache: 'pnpm' } # 缓存 key 自动含 lockfile hash
      - run: corepack enable && pnpm install --frozen-lockfile   # lockfile 不一致直接失败
      - name: 环境注入只取受控字段
        run: echo "BUILD_COMMIT=$GITHUB_SHA" >> $GITHUB_ENV      # 禁止 BUILD_TIME 之类
      - run: pnpm build
      - name: 产物哈希清单 用于跨机器比对
        run: find dist -type f -exec shasum -a 256 {} + | sort > dist/manifest.sha256
      - uses: actions/upload-artifact@v4
        with: { name: dist, path: dist }
```

```json
// package.json：engines + volta 锁定工具链
{
  "engines": { "node": ">=20.0.0 <21", "pnpm": ">=9" },
  "volta": { "node": "20.11.0", "pnpm": "9.1.0" },
  "scripts": { "preinstall": "npx only-allow pnpm" }
}
```
