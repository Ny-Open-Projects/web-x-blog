---
title: [OPS-053] CI 构建缓存策略有哪些层次？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-053：CI 构建缓存策略有哪些层次？
**答**：
- 依赖缓存：pnpm/yarn store 按锁文件 hash 缓存，安装从几分钟降到几十秒。
- 构建缓存：构建工具内置缓存（vite 缓存目录、webpack filesystem cache）+ Turborepo/Nx 远程缓存，团队共享"任何人构建过的产物"。
- CI 平台缓存：GitHub Actions 的 gha 缓存类型直连 buildx 层缓存（见 OPS-047）。
- 缓存纪律：key 必须含 lockfile hash 与工具版本，否则会踩"缓存了旧构建工具导致产物不一致"的深坑；远程缓存只对可复现构建开启。

```bash
#!/usr/bin/env bash
# ci_cache_setup.sh：三层缓存的 CI 初始化脚本
set -euo pipefail

# 1. 依赖缓存：pnpm store 目录固定，CI 用 key=lockfile-hash 挂载
pnpm config set store-dir .pnpm-store
echo "cache key: $(sha256sum pnpm-lock.yaml | cut -c1-16)"

# 2. Turborepo 远程缓存：团队共享构建产物（需签名验证，防缓存投毒）
export TURBO_TOKEN="$TURBO_TOKEN"          # 从 CI Secret 注入
export TURBO_TEAM="frontend"
npx turbo login --token="$TURBO_TOKEN" || true
npx turbo run build test \
  --filter=web-mall \
  --cache-dir=.turbo/cache \
  --output-hashes=true                     # 输出 hash 用于远程命中

# 3. 构建缓存目录：vite/webpack 缓存纳入 CI 缓存 key
mkdir -p .turbo/cache node_modules/.vite
echo "vite cache dir: node_modules/.vite (key 含 vite 版本)"
node -e "console.log('vite', require('vite/package.json').version)"

# turbo.json 关键配置（json）：
# { "remoteCache": { "signature": true },   // 签名防投毒
#   "tasks": { "build": { "outputs": ["dist/**"] } } }
```
