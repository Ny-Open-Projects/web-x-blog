---
title: [OPS-091] 依赖挂了（npm registry / 第三方 script）怎么预案？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-091：依赖挂了（npm registry / 第三方 script）怎么预案？
**答**：
- npm registry 挂：CI 装依赖失败全线阻塞。预案：CI 走私有 registry（verdaccio/nexus）做上游代理缓存 + 本地 pnpm store 缓存；配置 fallback 镜像源。
- 第三方 script（统计/地图/客服 SDK）挂：不能让它阻塞主应用。预案：异步加载 + 超时降级 + 自托管关键 SDK（下载到自有 CDN）。
- 加载策略纪律：第三方脚本一律 defer/async + onerror 降级，禁止同步阻塞渲染的外链脚本。
- 定期演练：CI 里随机注入"registry 不可用"，验证离线缓存路径有效。

```bash
#!/usr/bin/env bash
# dependency_resilience.sh：依赖挂了的预案落地
set -euo pipefail

# 1. CI 依赖安装走私有 registry（verdaccio 代理缓存 npmjs），挂了走镜像源 fallback
cat > .npmrc.ci <<'NPMRC'
registry=https://verdaccio.internal:4873/
//verdaccio.internal:4873/:_authToken=${VERDACCIO_TOKEN}
always-auth=true
fetch-retries=3
fetch-retry-mintimeout=2000
NPMRC

install_deps() {
  pnpm install --frozen-lockfile --registry https://verdaccio.internal:4873/ \
    || { echo "私有 registry 不可用，降级到镜像源";
         pnpm install --frozen-lockfile --registry https://registry.npmmirror.com; }
}

# 2. 离线兜底：发布产物时同步产出依赖快照，极端情况可离线安装
pnpm store add $(node -p "Object.keys(require('./package.json').dependencies).join(' ')") || true
tar -czf /artifacts/pnpm-store-$(date +%F).tgz .pnpm-store

# 3. 第三方 script 自托管检查：扫描 index.html 中外链脚本，
#    标记非自有域名的脚本，提醒下载到自有 CDN 并改为容错加载
grep -oE '<script[^>]+src="https?://[^"]+"' index.html | \
  grep -vE 'example\.com' | while read -r line; do
    echo "WARN: 第三方脚本未自托管: $line"
    echo "      预案：download 到 /vendor/ 并用 defer + onerror 降级加载"
  done

install_deps
```
