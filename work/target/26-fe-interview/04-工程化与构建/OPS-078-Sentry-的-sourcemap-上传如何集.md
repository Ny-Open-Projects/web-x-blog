---
title: [OPS-078] Sentry 的 sourcemap 上传如何集成到 CI？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-078：Sentry 的 sourcemap 上传如何集成到 CI？
**答**：
- 标准流程：构建 → sentry-cli 创建 release → 上传 map（带 url 前缀匹配）→ finalize release → 从产物剔除 map。
- 认证用 SENTRY_AUTH_TOKEN（CI Secret 注入，权限只给 project:releases），org/project/project 写进环境变量。
- url 前缀（~/assets 与 CDN 域名）必须与线上一致，否则 Sentry 匹配不到 map，栈还是混淆的——这是最常见的集成坑。
- 上传后校验：Sentry 后台或 API 检查该 release 的 artifacts 数量与预期一致。

```bash
#!/usr/bin/env bash
# ci_upload_sourcemap.sh：Sentry sourcemap 上传（CI 中运行）
set -euo pipefail

VERSION="${APP_VERSION:?need APP_VERSION, e.g. git sha}"
export SENTRY_ORG="my-org"
export SENTRY_PROJECT="web-mall"
export SENTRY_AUTH_TOKEN="${SENTRY_AUTH_TOKEN:?set from CI secret}"

# 0. 版本号一致性防呆：运行时代码上报的 release 与这里上传的必须同源
echo "release: $VERSION"

# 1. 创建 release（幂等：已存在会提示但继续）
sentry-cli releases new "$VERSION"

# 2. 注入 release 提交信息（Sentry 里可看该版本改动范围）
sentry-cli releases set-commits "$VERSION" --auto

# 3. 上传 sourcemap：url 前缀必须与线上资源 URL 一致
#    ~/assets 匹配同域 /assets/，https://cdn.example.com 匹配 CDN 域名
sentry-cli sourcemaps upload \
  --release "$VERSION" \
  --url-prefix "~/assets" \
  dist/assets

# 4. 关联部署环境（触发"该版本已部署"事件）
sentry-cli releases deploys "$VERSION" new -e production

# 5. finalize：之后该版本的错误统计开始聚合
sentry-cli releases finalize "$VERSION"

# 6. 校验上传数量
expected=$(find dist -name '*.map' | wc -l | tr -d ' ')
actual=$(sentry-cli releases files "$VERSION" list | wc -l)
echo "map expected=$expected uploaded=$actual"
[ "$actual" -ge "$expected" ] || { echo "WARN: sourcemap 可能上传不全"; exit 1; }
```
