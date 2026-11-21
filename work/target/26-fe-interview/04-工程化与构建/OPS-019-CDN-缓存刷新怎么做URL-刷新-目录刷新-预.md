---
title: [OPS-019] CDN 缓存刷新怎么做？URL 刷新、目录刷新、预热分别什么时候用？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-019：CDN 缓存刷新怎么做？URL 刷新、目录刷新、预热分别什么时候用？
**答**：
- URL 刷新：强制失效指定文件，最精准、配额最贵，用于 index.html、manifest.json 等入口文件。
- 目录刷新：整目录失效，用于批量更新，配额有限且会给源站带来回源风暴，慎用。
- 预热（prefetch）：把新版本资源提前拉到边缘节点，用于大版本发布/大促前，让首个用户请求就能命中缓存。
- hash 命名的资源不需要刷新（新内容新文件名），只需要预热；这是"发布后只刷 html、只预热 assets"策略的依据。

```bash
#!/usr/bin/env bash
# cdn_refresh.sh：发布后的刷新与预热（以通用 CDN API 为例，各厂商参数类似）
set -euo pipefail
CDN_API="https://cdn.console.example.com/api"
AUTH="Authorization: Bearer $CDN_PURGE_TOKEN"

VERSION=$(cat /tmp/build/VERSION)

# 1. URL 刷新：入口 html（必做，量小）
curl -fsS -X POST "$CDN_API/purge/url" -H "$AUTH" -H "Content-Type: application/json" -d '{
  "urls": [
    "https://www.example.com/index.html",
    "https://www.example.com/m/index.html"
  ]
}'

# 2. 目录刷新：仅当有大量非 hash 文件更新时使用（有回源风暴风险）
# curl -fsS -X POST "$CDN_API/purge/dir" -H "$AUTH" \
#   -d '{"dir": "https://www.example.com/static/config/"}'

# 3. 预热：从构建产物提取 assets 清单，提前推到边缘节点
jq -r '.assets[].url' /tmp/build/dist/manifest.json |
  sed 's|^|https://cdn.example.com/|' > /tmp/prefetch.list
head -n 500 /tmp/prefetch.list |   # 预热有配额，按关键资源优先
  jq -R . | jq -s '{urls: .}' > /tmp/prefetch.json
curl -fsS -X POST "$CDN_API/prefetch" -H "$AUTH" \
  -H "Content-Type: application/json" -d @/tmp/prefetch.json

echo "refresh+prefetch done for $VERSION"
```
